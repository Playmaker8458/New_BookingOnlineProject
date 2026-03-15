from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Admin.routers.auth import router as auth_router

from routers.line_auth import router as line_auth
from routers.InsertProfile import router as InsertProfile_router


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


# Admin
# include router คือรวม route จากไฟล์อื่น ตรงนี้ที่เขียนไว้ในไฟล์อื่นมาใช้งานใน app หลักเป็น /auth/Login สำหรับ login ฝั่ง Admin
app.include_router(auth_router, prefix="/auth")


# User [Student and Advisor]
# include router คือรวม route จากไฟล์อื่น ตรงนี้ที่เขียนไว้ในไฟล์อื่นมาใช้งานใน app หลักเป็น /Login/LoginVerification สำหรับ login User
app.include_router(line_auth, prefix="/Login")
app.include_router(InsertProfile_router, prefix="/register")

