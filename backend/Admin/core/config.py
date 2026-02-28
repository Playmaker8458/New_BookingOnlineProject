import os
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY") # คือ key ลับ ใช้เข้ารหัสและถอดรหัส JWT (JASON Web token)