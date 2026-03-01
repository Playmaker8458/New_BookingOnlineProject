import os
import psycopg2
from dotenv import load_dotenv

# เข้าถึงเพื่อดึงข้อมูลจากไฟล์ environment มาใช้งาน
load_dotenv()

# ฟังก์ชั่นเชื่อมต่อฐานข้อมูล postgresSQL
def get_connectionDB():
    try:
        return psycopg2.connect(
            user = os.getenv('POSTGRES_USER'),
            password = os.getenv('POSTGRES_PASSWORD'),
            database = os.getenv('POSTGRES_DB'),
            host = "localhost",
            port = 5432
        )
    except:
        return False 