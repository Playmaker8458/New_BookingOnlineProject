from DB.db import get_connection

def admin_table():
    conn = get_connection()

    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        user_id SERIAL PRIMARY KEY,
                        user_name VARCHAR(100) UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                        email VARCHAR(100) UNIQUE,
                        created_date TIMESTAMP DEFAULT NOW()
                    )
                """)
        print("สร้างตารางสำเร็จ")
    
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

    finally:
        conn.close()


if __name__ == "__main__":
    admin_table()