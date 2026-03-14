from fastapi import APIRouter
from pydantic import BaseModel
from Database.ConnectDB import get_connectionDB

# กำหนดตัวชี path เพื่อเชื่อมต่อกับตัวภายนอก
router = APIRouter()

# กำหนดข้อมูล UserProfile ในการรับข้อมูลจากภายนอกแบบ Requeate 
class UserProfile(BaseModel):
    UserID: str
    prefix: str
    fristname: str
    lastname: str
    imageURL: str


@router.post('/api/test')
async def show(user: UserProfile):
    return {
        "UUID": user.UserID, 
        "Prefix": user.prefix,
        "FristName": user.fristname, 
        "LastName": user.lastname,
        "imageURL": user.imageURL
    }

# @router.get('/api/test')
# async def getdata_profile():
#     return {"test": "Hello World!"}