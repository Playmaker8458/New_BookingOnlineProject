from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# สร้างตัวอย่าง fastAPI เพื่อใช้ในการจัดการข้อมูลที่ส่งมาด้วย API ทั้งหมด
app = FastAPI()

# กำหนดสิทธิ์เพื่อให้รับข้อมูล หรือ เข้าถึงข้อมูลใน fontend ด้วย API 
app.add_middleware(
    # โดยเลือกใช้เป็น CORS เพิ่อใช้สำหรับส่งข้อมูลผ่าน API
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # อนุญาตให้เข้าถึง Vue dev server localhost
    allow_methods=["*"], # อนุญาตให้เข้าถึง HTTP Method ทั้งหมด (GET, POST, PUT, DELETE)
    allow_headers=["*"], # อนุญาตให้เข้าถึง Header URL ทุกๆตัวที่ส่งมาทั้งหมด
)

# กำหนดข้อมูลโปรไฟล์ให้ตรงกับ LineLiff สำหรับใช้ในการรับและส่งข้อมูลผ่าน API
class UserProfile(BaseModel):
    UserID: str  # รับข้อมูล "UserID" ของผู้ใช้จาก Line 
    DisplayName: str # รับข้อมูล "ชื่อจริง" ของผู้ใช้จาก Line 
    ImageUrl: str # รับข้อมูล "path-รูปภาพ" ของผู้ใช้จาก Line 


# ส่งข้อมูลแบบ post โดยจะส่งกลับไปแสดงในหน้า console (Dev-tool: F12) ของเว็ปเพจ
@app.post("/profile")
async def Show_profile(data: UserProfile):
    global Profile_Data  # กำหนดให้ตัวแปร Profile_Data เรียกใช้งานจากด้านนอกได้

    # กำหนดข้อมูลโปลไฟล์ของไลน์ให้ตรงกับที่ดึงมาจาก Axios API ของฝั่ง frontend
    Profile_Data = {
        "UserID": data.UserID,
        "DisplayName": data.DisplayName,
        "ImageUrl": data.ImageUrl,
    }

    # ส่งข้อมูลโปรไฟล์ของไลน์กลับไปแสดงใน localhost ของฝั่ง frontend
    return {"userId": Profile_Data["UserID"], "DisplayName": Profile_Data["DisplayName"], "ImageUrl": Profile_Data["ImageUrl"]}


# ส่งข้อมูลแบบ get โดยส่งข้อมูลโปรไฟล์จาก LINE Liff กลับไปแสดงใน doc ของ API
@app.get("/profile/show")
async def get_profile():
    # ส่งข้อมูลลโปรไฟล์จาก LINE Liff กลับไปเป็น dictionary
    return {
        "DisplayName": Profile_Data['DisplayName'], 
        "ImageUrl" : Profile_Data['ImageUrl'],  
        "UserID" : Profile_Data['UserID']
    }