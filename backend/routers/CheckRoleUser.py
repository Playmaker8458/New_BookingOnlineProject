from fastapi import APIRouter
from Database.ConnectDB import get_connectionDB

router = APIRouter()

@router.get('/CheckRoleUser')
async def CheckRoleUser():
    cnn = get_connectionDB()
    cur = cnn.cursor()

    SQL_SELECT = """
        SELECT "role_user", "status" FROM "LoginUser"
    """

    cur.execute(SQL_SELECT)
    user = cur.fetchone()
    
    cnn.commit()

    cnn.close()
    cur.close()
    
    return user