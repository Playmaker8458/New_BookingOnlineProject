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
    cnn = get_connectionDB()
    cur = cnn.cursor()

    UserProfile = {
        "Prefix": user.prefix,
        "FristName": user.fristname,
        "LastName": user.lastname,
        "Major": user.major,
        "UUID": user.UserID, 
        "imageURL": user.imageURL
    }

    SQL_INSERT = """
        INSERT INTO "LoginUser" ("prefix", "fristName", "LastName", "major", "uuid_line", "profile_image", "status")
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT ("uuid_line") DO NOTHING
    """
    cur.execute(
        SQL_INSERT,
        (UserProfile['Prefix'], UserProfile['FristName'], UserProfile['LastName'], UserProfile['Major'], UserProfile['UUID'], UserProfile['imageURL'], "Pending")
    )

    SQL_SELECT = """
        SELECT "role_user", "status" 
        FROM "LoginUser"
        WHERE "uuid_line"=%s
    """
    cur.execute(
        SQL_SELECT,
        (UserProfile['UUID'],)
    )

    user = cur.fetchone()
    cnn.commit() # บันทึกการส่งเมื่อมีการเปลี่ยนแปลงฐานข้อมูล
    
    # ปิดการเข้าถึงฐานข้อมูล และ ปิดตัวรันฐานข้อมูล
    cnn.close()
    cur.close()

    return user