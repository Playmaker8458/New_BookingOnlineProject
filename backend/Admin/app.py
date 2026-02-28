from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Admin.auth.auth import router as auth_router
from Admin.core.config import JWT_SECRET_KEY

app = FastAPI()

# CORS อนุญาตให้ frontend เรียก API ได้
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # ตรงนี้เปลี่ยนเป็น frontend domain จริงตอน production
    allow_credentials=True,
    allow_methods=["*"], #อนุญาต HTTP method ทุกแบบ
    allow_headers=["*"],#อนุญาต header ทุกชนิด
)

# include router คือรวม route จากไฟล์อื่น ตรงนี้ที่เขียนไว้ในไฟล์อื่นมาใช้งานใน app หลักเป็น /auth/Login สำหรับ login
app.include_router(auth_router, prefix="/auth")
# 

# favicon route นี้ใช้ป้องกัน error
@app.get("/favicon.ico")
def favicon():
    return {}

# root
@app.get("/")
def read_root():
    return {"Hello": "World"}