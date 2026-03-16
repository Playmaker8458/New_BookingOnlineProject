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
class LineAccessToken(BaseModel):
    Token: str

# ROUTE /auth/VerifyRole
@router.post('/auth/VerifyRole')
async def Line_Login(data: LineAccessToken):

    # กำหนด url ของ Line api ในการตรวจสอบความถูกต้องมาเก็บลงในตัวแปร url
    url = 'https://api.line.me/v2/profile'

    # ดึง Access Token จาก LineToken ที่รับข้อมูลแบบ requests เก็บลงในตัวแปร Access_token
    Access_token = data.Token
    
    headers = {
        "Authorization": f"Bearer {Access_token}"
    }

    # กำหนดข้อมูลสำหรับส่งคำขอไปยัง Line API เพื่อใช้ในการตรวจสอบ AccessToken ของผู้ใช้งาน
    res = requests.post(url, headers=headers)

    # แปลงข้อมูลที่เก็บในตัวแปร res เป็น json และเก็บลงในตัวแปร UserProfile
    UserProfile = res.json() 
    # ดึง userid จากตัวแปร UserProfile มาเก็บไว้ที่ตัวแปร UUID_line
    UUID_line = UserProfile['userId']     

    # ดึงตัวเชื่อมต่อฐานข้อมูลมาใช้งาน (BORC_Project Database)
    cnn = get_connectionDB() 
    # กำหนดตัวรันฐานข้อมูล หรือตัวเข้าถึงฐานข้อมูล (ใช้กับ execute เพื่อรอส่งชุดคำสั่ง SQL)
    cur = cnn.cursor() 

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
        # ถ้ายังไม่มีข้อมูลผู้ใช้ จะส่งข้อมูลใหม่กลับไปยัง path /auth/VerifyRole 
        return {"Role": "new_user", "status": "No_Status", "profile": UserProfile}
    else:
        # ถ้ามีข้อมูลผู้ใช้ จะส่งข้อมูลที่สมัครสมาชิกแล้วกลับไปยัง path /auth/VerifyRole 
        return {"Role": user[0], "status": user[1]}