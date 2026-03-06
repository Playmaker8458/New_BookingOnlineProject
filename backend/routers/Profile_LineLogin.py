from fastapi import APIRouter
from pydantic import BaseModel
from Database.ConnectDB import get_connectionDB

router = APIRouter()

# กำหนดข้อมูลในการส่งแบบ Requeate API 
class UserProfile(BaseModel):
    UserID: str  
    DisplayName: str 
    ImageUrl: str


# ส่งข้อมูลแบบ post โดยจะส่งกลับไปแสดงในหน้า console (Dev-tool: F12) ของเว็ปเพจ
@router.post("/LoginVerification")
async def Show_profile(data: UserProfile):

    # กำหนดข้อมูลโปลไฟล์ของไลน์ให้ตรงกับที่ดึงมาจาก Axios API ของฝั่ง frontend
    Profile_Data = {
        "UserID": data.UserID,
        "DisplayName": data.DisplayName,
        "ImageUrl": data.ImageUrl,
    }
    
    conn = get_connectionDB()
    cur = conn.cursor()

    # ชุดคำสั่งที่ใช้ในการแทรกข้อมูลในตาราง "LoginPermissions" (กำหนดไม่ให้มีข้อมูลซ้ำกัน)
    SQL_insert = """
        INSERT INTO "LoginPermissions" (uuid_line, fullname, profile_image, status_permissions, role_user)  
        VALUES (%s,%s,%s,%s,%s) 
        ON CONFLICT (uuid_line) DO NOTHING;
    """

    cur.execute(
        SQL_insert,
        (Profile_Data['UserID'], Profile_Data['DisplayName'], Profile_Data['ImageUrl'], 'ยังไม่ยืนยัน', 'ยังไม่ได้กำหนดสิทธิ์')
    )
    conn.commit()

    cur.close()
    conn.close()
    

    # ส่งข้อมูลโปรไฟล์ของไลน์กลับไปแสดงใน localhost ของฝั่ง frontend
    return Profile_Data