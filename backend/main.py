from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from Database.ConnectDB import get_connectionDB
from Admin.auth.auth import router as auth_router


# สร้างตัวอย่าง fastAPI เพื่อใช้ในการจัดการข้อมูลที่ส่งมาด้วย API ทั้งหมด
app = FastAPI()

# กำหนดสิทธิ์เพื่อให้รับข้อมูล หรือ เข้าถึงข้อมูลใน fontend ด้วย API 
app.add_middleware(
    # โดยเลือกใช้เป็น CORS เพิ่อใช้สำหรับส่งข้อมูลผ่าน API
    CORSMiddleware,
    allow_origins=["*"], # ตรงนี้เปลี่ยนเป็น frontend domain จริงตอน production
    allow_credentials=True,
    allow_methods=["*"], # อนุญาตให้เข้าถึง HTTP Method ทั้งหมด (GET, POST, PUT, DELETE)
    allow_headers=["*"], # อนุญาตให้เข้าถึง Header URL ทุกๆตัวที่ส่งมาทั้งหมด
)

# กำหนดข้อมูลในการส่งแบบ Requeate API 
class UserProfile(BaseModel):
    UserID: str  
    DisplayName: str 
    ImageUrl: str

# include router คือรวม route จากไฟล์อื่น ตรงนี้ที่เขียนไว้ในไฟล์อื่นมาใช้งานใน app หลักเป็น /auth/Login สำหรับ login
app.include_router(auth_router, prefix="/auth")

# ส่งข้อมูลแบบ post โดยจะส่งกลับไปแสดงในหน้า console (Dev-tool: F12) ของเว็ปเพจ
@app.post("/profile")
async def Show_profile(data: UserProfile):

    # กำหนดข้อมูลโปลไฟล์ของไลน์ให้ตรงกับที่ดึงมาจาก Axios API ของฝั่ง frontend
    Profile_Data = {
        "UserID": data.UserID,
        "DisplayName": data.DisplayName,
        "ImageUrl": data.ImageUrl,
    }
    
    conn = get_connectionDB()
    cur = conn.cursor()

    # ชุดคำสั่งที่ใช้ในการแทรกข้อมูลในตาราง "LoginPermissions" (ห้ามซ้ำ)
    SQL_insert = """
        INSERT INTO "LoginPermissions" (uuid_line, fullname, profile_image)  
        VALUES (%s,%s,%s) 
        ON CONFLICT (uuid_line) DO NOTHING;
    """

    cur.execute(
        SQL_insert,
        (Profile_Data['UserID'], Profile_Data['DisplayName'], Profile_Data['ImageUrl'])
    )
    conn.commit()

    cur.close()
    conn.close()
    

    # ส่งข้อมูลโปรไฟล์ของไลน์กลับไปแสดงใน localhost ของฝั่ง frontend
    return Profile_Data