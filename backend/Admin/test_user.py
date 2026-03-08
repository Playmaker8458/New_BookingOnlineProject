from DB.db import get_connection
from password_check import hash_password

def add_user(user_name: str,plain_password: str, email: str):
    """ ฟังก์ชั่นนี้ รับ 3 ค่า user_name, password, email"""
    hashed_pw = hash_password(plain_password)
    #เชื่อมฐานข้อมูล
    conn = get_connection()
    # insert ค่า user_name password email
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """ INSERT INTO users (user_name, password,email,created_date)
                    VALUES (%s, %s, %s, NOW())
                    RETURNING user_id """,
                    (user_name,hashed_pw,email)
            )
            user_id = cursor.fetchone() [0]
        
        conn.commit() 
        print(f" เพิ่ม Admin สำเร็จ user_id = {user_id} สำเร็จ")

    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

    finally:
        conn.close()

if __name__ == "__main__":
    # ทดลอง user
    add_user("admin2","Parkphoom@23","parkphoom151@gmail.com") 