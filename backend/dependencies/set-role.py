# from Admin.DB.db import get_connection

# def users_table():
#     conn = get_connection()

#     try:
#         with conn:
#             with conn.cursor() as cursor:
#                 cursor.execute("""
#                     CREATE TABLE IF NOT EXISTS LoginPermissions (
#                         id int PRIMARY KEY,
#                         uuid_line uuid NOT NULL,
#                         fullname VARCHAR(255) NOT NULL,
#                         password TEXT NOT NULL,
#                         email VARCHAR(100) UNIQUE,
#                         user_id
#                     )
#                 """)
#         print("สร้างตารางสำเร็จ")
    
#     except Exception as e:
#         print(f"เกิดข้อผิดพลาด: {e}")

#     finally:
#         conn.close()

# Table LoginPermissions{
#   id integer [pk, increment]
#   uuid_line uuid [not null]
#   fullname varchar(255) [not null]
#   profile_image varchar(255) [not null]
#   status_permissions StatusPermissions
#   role_user Role [note: "สิทธิ์การเข้าสู่ระบบ (ผู้ใช้ทั่วไป)"]
#   admin_id integer 

# if __name__ == "__main__":
#     users_table()