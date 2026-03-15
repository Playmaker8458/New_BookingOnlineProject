import os
import requests

from dotenv import load_dotenv
from fastapi import APIRouter
from pydantic import BaseModel
from Database.ConnectDB import get_connectionDB

# ดึงตัวแปรในไฟล์ env ทั้งหมดเข้ามาใช้งาน
load_dotenv()

# กำหนดตัวชี้ path เพื่อเชื่อมต่อกับตัว app router path ภายนอก
router = APIRouter()

# กำหนด Token เอาไว้รับข้อมูลจากหน้า frontend แบบ requests
class LineToken(BaseModel):
    token : str

# ROUTE /auth/VerifyRole
@router.post('/auth/VerifyRole')
async def Line_Login(data: LineToken):
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

    SQL_SELECT = """
        SELECT "role_user", "status" 
        FROM "LoginUser"
        WHERE "uuid_line"=%s
    """

    # ส่งชุดคำสั่ง SQL ไปยังฐานข้อมูลเพื่อค้นหา UUID_line ของผู้ใช้ที่ส่งเข้าไปตรวจสอบว่ามีหรือไม่
    cur.execute(
        SQL_SELECT,
        (UUID_line,)
    )
    
    # ดึงข้อมูล 1 แถวของผู้ใช้ที่ส่งเข้าไปออกมา และกำหนดให้กับตัวแปร user  
    user = cur.fetchone()  
    
    # ตรวจสอบข้อมูลผู้ใช้ 
    if not user:
        # ถ้ายังไม่มีข้อมูลผู้ใช้ จะส่งสิทธิ์ และ สถานะของผู้ใช้ใหม่กลับยัง path /auth/VerifyRole (fastapi)
        return {"Role": "new_user", "status": "No_Status", "profile": LineUser}
    elif user[0] == "Student" and user[1] == "Processed":
        # ถ้าข้อมูลผู้ใช้เป็นของนักศึกษา จะส่งข้อมูลกลับไปยัง path /auth/VerifyRole (fastapi)
        return {"Role": user[0], "status": user[1]}
    elif user[0] == "Advisor" and user[1] == "Processed":
        # ถ้าข้อมูลผู้ใช้เป็นของอาจารย์ จะส่งข้อมูลกลับไปยัง path /auth/VerifyRole (fastapi)
        return {"Role": user[0], "status": user[1]}
    else:
        # ถ้ายังไม่ได้ยืนยันสิทธิ์ในการเข้าสู่ระบบ จะส่งข้อมูลกลับไปยัง path /auth/VerifyRole (fastapi)
        return {"Role": user[0], "status": user[1]}