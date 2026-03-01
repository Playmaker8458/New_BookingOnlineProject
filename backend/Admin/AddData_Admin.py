from Database.ConnectDB import get_connectionDB
from password_check import hash_password

def add_Admin(user_name: str, plain_password: str):
    """ ฟังก์ชั่นนี้ รับ 3 ค่า user_name, password, email"""
    hashed_pw = hash_password(plain_password)
    #เชื่อมฐานข้อมูล
    conn = get_connectionDB()
    # insert ค่า user_name password email
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """ INSERT INTO "AdminProfile" (username, password)
                    VALUES (%s, %s)
                    RETURNING id """,
                    (user_name, hashed_pw)
            )
            user_id = cursor.fetchone()[0]
        
        conn.commit() 
        print(f" เพิ่ม Admin สำเร็จ id = {user_id} สำเร็จ")

    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

    finally:
        conn.close()

if __name__ == "__main__":
    # ทดลอง user
    add_Admin("admin2","Parkphoom@23") 