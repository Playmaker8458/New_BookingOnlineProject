from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# กำหนดข้อมูลโปรไฟล์ให้ตรงกับ LineLiff
class UserProfile(BaseModel):
    UserID: str # UserID กำหนดข้อมูล "UUID" ที่จะส่งเข้ามาเก็บ string  
    DisplayName: str # DisplayName กำหนดข้อมูล "ชื่อผู้ใช้" ที่จะส่งเข้ามาเก็บเป็น sting
    ImageUrl: str # ImageUrl กำหนดข้อมูล "URL:รูปภาพ" ที่จะส่งเข้ามาเก็บเป็น sting


# ส่งข้อมูลแบบ post โดยจะส่งกลับไปแสดงในหน้า console (Dev-tool: F12) ของเว็ปเพจ
@app.post("/api")
async def receive_profile(data: UserProfile):
    global Profile_Data  # กำหนดให้ตัวแปร Profile_Data เรียกใช้งานจากด้านนอกได้
    # กำหนดข้อมูลโปลไฟล์ของไลน์ให้ตรงกับที่ดึงมาจาก Axios API ของฝั่ง frontend
    Profile_Data = {
        "UserID": data.UserID,
        "DisplayName": data.DisplayName,
        "ImageUrl": data.ImageUrl,
    }
    # ส่งข้อมูลโปรไฟล์ของไลน์กลับไปแสดงใน localhost ของฝั่ง frontend
    return {"userId": Profile_Data["UserID"], "DisplayName": Profile_Data["DisplayName"], "ImageUrl": Profile_Data["ImageUrl"]}

# 
@app.get("/api")
async def get_profile():
    return {
        "DisplayName": Profile_Data['DisplayName'],
        "ImageUrl" : Profile_Data['ImageUrl'], 
        "UserID" : Profile_Data['UserID']
    }