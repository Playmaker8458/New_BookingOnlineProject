from fastapi import APIRouter
from pydantic import BaseModel
from Database.ConnectDB import get_connectionDB

# กำหนดตัวชี path เพื่อเชื่อมต่อกับตัวภายนอก
router = APIRouter()

# กำหนดข้อมูล RoleUpdate ในการรับข้อมูลจากภายนอกแบบ Requeate 
class RoleUpdate(BaseModel):
    role_user: str

# ส่งข้อมูลแบบ PUT โดยนำข้อมูลที่ได้มาส่งกลับไปเก็บในฐานข้อมูลผ่าน URL นี้
@router.put("/LoginRightsData/{id}")
async def UpdateRole(id: int, date: RoleUpdate):

    # เชื่อมต่อฐานข้อมูล PostgresSQL
    conn = get_connectionDB()
    # กำหนดตัวชี้ไปยังฐานข้อมูล เพื่อเปลี่ยนแปลงข้อมูลด้านใน
    cur = conn.cursor()

    # กำหนดชุดคำสั่ง UPDATE ของตาราง "LoginPermissions" ให้กับตัวแปร UpdateSQL
    UpdateSQL = """
        UPDATE "LoginPermissions"
        SET "status_permissions" = %s, "role_user" = %s 
        WHERE id = %s
    """

    # ส่งชุดคำสั่ง SQL พร้อมกับข้อมูลที่จะทำการอัพเดตเข้าไปประมวลในฐานข้อมูล
    cur.execute(
        UpdateSQL,
        ("ยืนยันแล้ว", date.role_user, id)
    )

    # ใช้ในการยืนยันการเปลี่ยนแปลงในฐานข้อมูล
    conn.commit()

    # ปิดการเข้าถึงฐานข้อมูล และ ตารางทั้งหมด
    cur.close()
    conn.close()

    return {"message":"User updated"}