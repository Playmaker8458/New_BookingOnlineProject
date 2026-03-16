from fastapi import APIRouter
from pydantic import BaseModel
from Database.ConnectDB import get_connectionDB

# กำหนดตัวชี path เพื่อเชื่อมต่อกับตัวภายนอก
router = APIRouter()

# กำหนดข้อมูล UserProfile ในการรับข้อมูลจากภายนอกแบบ Requeate 
class UserProfile(BaseModel):
    prefix: str
    fristname: str
    lastname: str
    major: str
    UserID: str
    imageURL: str

@router.post('/InsertProfile')
async def InsertUserProfile(user: UserProfile):
    
    # กำหนดชุดข้อมูลผู้ใช้ใหม่ ในตัวแปร UserProfile
    UserProfile = {
        "Prefix": user.prefix,
        "FristName": user.fristname,
        "LastName": user.lastname,
        "Major": user.major,
        "UUID": user.UserID, 
        "imageURL": user.imageURL
    }
    
    cnn = get_connectionDB()
    cur = cnn.cursor()

    # กำหนดชุดคำสั่ง SQL สำหรับการเพิ่มข้อมูลผู้ใช้ใหม่ ลงในตาราง LoginUser 
    SQL_INSERT = """
        INSERT INTO "LoginUser" ("prefix", "fristName", "LastName", "major", "uuid_line", "profile_image", "status")
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT ("uuid_line") DO NOTHING
    """
    # ส่งชุดคำสั่ง SQL สำหรับการเพิ่มข้อมูลผู้ใช้ใหม่เข้าไปประมวลผลในตาราง LoginUser
    cur.execute(
        SQL_INSERT,
        (UserProfile['Prefix'], UserProfile['FristName'], UserProfile['LastName'], UserProfile['Major'], UserProfile['UUID'], UserProfile['imageURL'], "Pending")
    )

    # บันทึกการส่งเมื่อมีการเปลี่ยนแปลงฐานข้อมูล
    cnn.commit() 
    
    # ปิดการเข้าถึงฐานข้อมูล และ ปิดตัวรันฐานข้อมูลทั้งหมด
    cnn.close()
    cur.close()

    return {"Message": "เสร็จสิ้นการเพิ่มข้อมูลผู้ใช้ใหม่"}