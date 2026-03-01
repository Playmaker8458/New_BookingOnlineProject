from Database.ConnectDB import get_connectionDB


conn = get_connectionDB() # เรียกใช้งานตัวเชื่อมต่อฐานข้อมูล 
cur = conn.cursor() # สร้างตัวชี้ไปยังฐานข้อมูล

# ใช้สำหรับอ่านไฟล์ SQl และ ดึงข้อมูลไฟล์ SQl กลับไปใช้งาน
def ReadSQL_File():
    # อ่านไฟล์ SQL จากโฟรเดอร์ Database ทั้งหมด
    with open('./Database/BORC.sql', 'r', encoding='utf8') as file_Sql:
        return file_Sql.read()

# ส่งชุดคำสั่ง SQl ไปประมวลผลในฐานข้อมูลทั้งหมด
cur.execute(
    ReadSQL_File()
)

conn.commit() # บันทึกเมื่อมีการเปลี่ยนแปลงข้อมูล ในฐานข้อมูล
print("สร้างตารางทั้งหมด และ เชื่อมต่อตารางทั้งหมดสำเร็จ")