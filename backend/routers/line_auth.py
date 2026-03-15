import os
import requests

from dotenv import load_dotenv
from fastapi import APIRouter
from pydantic import BaseModel
from Database.ConnectDB import get_connectionDB

# ดึงตัวแปรในไฟล์ env ทั้งหมดเข้ามาใช้งาน
load_dotenv()

# กำหนดตัวชี้ path เพื่อเชื่อมต่อกับตัว app ภายนอก
router = APIRouter()

# กำหนด Token เอาไว้รับข้อมูลจากหน้า frontend แบบ requests
class LineToken(BaseModel):
    token : str

# ROUTE Login
@router.post('/auth/VerifyRole')
async def check_role(data: LineToken):
    # กำหนด url ของ Line api ในการตรวจสอบความถูกต้องมาเก็บลงในตัวแปร verify_url
    verify_url = 'https://api.line.me/oauth2/v2.1/verify'

    """
    กำหนด payload สำหรับรอส่ง Token_ID ของผู้ใช้ไปตรวจสอบความถูกต้องใน LINE
    - กำหนด token_ID ของ Liff login ที่ได้จากการรับข้อมูลแบบ requests
    - กำหนด Channel_ID ของ LINE Login ที่ดึงมาจากไฟล์ .env
    """
    payload = {
        "id_token": data.token,
        "client_id": os.getenv('LINE_CHANNEL_ID')
    }

    """
    กำหนดข้อมูลสำหรับส่งคำขอไปยัง Line API เพื่อใช้ในการตรวจสอบ Token Id ของผู้ใช้งาน
    - ดึงตัวแปร verify_url ที่เก็บ URL สำหรับตรวจสอบ token มาใช้งาน
    - ดึง payload ที่เก็บ token_Id ของผู้ใช้ และ channel id ของช่องทาง LoginLiff มาใช้งาน
    - กำหนดเป็น post เพื่อส่งคำขอตรวจสอบข้อมูลผู้ใช้ใน Line ด้วย requests
    """
    res = requests.post(verify_url, data=payload)
    
    # แปลงข้อมูลที่เก็บในตัวแปร res เป็น json และเก็บลงในตัวแปร LineUser 
    LineUser = res.json()
    UUID_line = LineUser['sub']
    

    cnn = get_connectionDB() # ดึงตัวเชื่อมต่อฐานข้อมูลมาใช้งาน (BORC_Project Database)
    cur = cnn.cursor() # กำหนดตัวรันฐานข้อมูล หรือตัวเข้าถึงฐานข้อมูล (ใช้กับ execute เพื่อรอส่งชุดคำสั่ง SQL)

    # ส่งชุดคำสั่ง SQL ไปยังฐานข้อมูลเพื่อค้นหา UUID_line ของผู้ใช้ที่ส่งเข้าไปตรวจสอบว่ามีหรือไม่
    cur.execute(
        """
           SELECT "role_user", "status" 
           FROM "LoginUser"
           WHERE "uuid_line"=%s
        """,
        (UUID_line,)
    )
    
    user = cur.fetchone() # ดึงข้อมูล 1 แถวที่เป็นของ column [role_user status และ  uuid_line] 
    
    # ถ้าไม่พบข้อมูลผู้ใช้ในฐานข้อมูล
    if not user:
        # จะส่งสิทธิ์ และ สถานะของผู้ใช้ใหม่กลับไปแสดงใน path /auth/VerifyRole (fastapi)
        return {"Role": "new_user", "status": "No_Status"}
    else:
        # จะส่งสิทธิ์ และ สถานะข้อมูลของผู้ใช้ที่ถูกบันทึกในฐานข้อมูล กลับไปแสดงใน path /auth/VerifyRole (fastapi)
        return {"Role": user[0], "status": user[1]}