from fastapi import APIRouter, HTTPException   # ใช้สร้าง route และจัดการ error
from pydantic import BaseModel                 # ใช้กำหนดรูปแบบข้อมูล request
from jose import jwt                           # ใช้สร้าง JWT token
from datetime import datetime, timedelta       # ใช้กำหนดเวลา token หมดอายุ
from ..Database.ConnectDB import get_connectionDB            # ฟังก์ชันเชื่อมต่อฐานข้อมูล
import bcrypt                                  # ใช้ตรวจสอบรหัสผ่าน
from Admin.core.config import JWT_SECRET_KEY   # secret key สำหรับเข้ารหัส token


# สร้าง router (แทน blueprint ของ fast API)
router = APIRouter()

# ตั้งค่าการสร้าง JWT
ALGORITHM = "HS256"                 # model สำหรับการสำหรับเข้ารหัสของ token
ACCESS_TOKEN_EXPIRE_MINUTES = 60    # กำหนดเวลาวันหมดอายุ token โดยกำหนดอยู่ที่ 60 นาที

# MODEL รูปแบบข้อมูลที่ client ต้องส่งมา
class LoginRequest(BaseModel):
    username: str
    password: str

# ฟังก์ชันสร้าง JWT token
def create_access_token(data: dict):
    """
    รับข้อมูล user แล้วสร้าง token พร้อมวันหมดอายุ
    """
    to_encode = data.copy()

    # กำหนดเวลาหมดอายุ token
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    # เพิ่ม exp ลงใน payload
    to_encode.update({"exp": expire})

    # เข้ารหัสและสร้าง token
    return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)


# ROUTE LOGIN
@router.post("/login")
def login(data: LoginRequest):
    global access_token
    
    # ตรวจสอบว่ามี username และ password หรือไม่
    if not data.username or not data.password:
        raise HTTPException(status_code=400, detail="username และ password ไม่มีค่า")

    try:
        # เชื่อมต่อฐานข้อมูล
        conn = get_connectionDB()

        # ดึงข้อมูล user จาก database
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id, username, password
                    FROM "AdminProfile"
                    WHERE username = %s
                    """,
                    (data.username,)
                )
                
                user = cursor.fetchone()

        # ถ้าไม่พบ user
        if not user:
            raise HTTPException(status_code=404, detail="ไม่มีผู้ใช้")

        # แยกค่าที่ได้จาก database
        user_id, user_name, hashed_password = user
        

        # ตรวจสอบรหัสผ่านด้วย bcrypt 
        if not bcrypt.checkpw(
            data.password.encode("utf-8"),      # รหัสที่ user กรอก
            hashed_password.encode("utf-8")     # hash รหัสที่เก็บใน DB
        ):
            #ถ้ารหัสไม่ถูกต้องจะฟ้องสถานะ 401 ว่า "รหัสผ่านไม่ถูกต้อง"
            raise HTTPException(status_code=401, detail="รหัสผ่านไม่ถูกต้อง") 


        # ถ้ารหัสถูกต้อง → สร้าง JWT token
        access_token = create_access_token({
            "sub": user_name,   # subject (ชื่อ user)
            "user_id": user_id  # id user
        })

        # ส่ง token กลับ client กลับไปแสดงใน path /login (fastapi)
        return {"access_token": access_token}

    # error ที่เราสร้างเอง client จะเห็น
    except HTTPException:
        raise

    # error อื่น ๆ (เช่น DB error)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))