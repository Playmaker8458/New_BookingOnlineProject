from fastapi import APIRouter
from Database.ConnectDB import get_connectionDB

router = APIRouter()

@router.post("/LoginPermissions")
async def Table_DataProfile():

    conn = get_connectionDB()
    cur = conn.cursor()

    # ชุดคำสั่งในการดึงข้อมูลทั้งหมดจากตาราง LoginPermission และ เลียงลำดับ id จากน้อยไปหามาก
    SQL_Select = """
        SELECT *
        FROM "LoginPermissions"
        ORDER BY "id" ASC
    """
    # ส่งชุดคำสั่งดึงข้อมูล กลับไปประมวลใน pgadmin
    cur.execute(
       SQL_Select 
    )

    # ดึงชุดข้อมูลจากตาราง LoginPermission ในฐานข้อมูลกำหนดให้กับตัวแปร rows
    rows = cur.fetchall()

    result = []
    for row in rows:
        result.append({
            "id": row[0],
            "uuid_line": row[1],
            "fullname": row[2],
            "profile_image": row[3],
            "status_permissions": row[4],
            "role_user": row[5],
            "admin_id": row[6]
        })

    cur.close()
    conn.close()

    return result