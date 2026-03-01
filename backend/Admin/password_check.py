import bcrypt # ใช้เข้ารหัสผ่าน และตรวจสอบรหัสผ่านด้วย bcrypt

def hash_password(plain_password: str) ->str:
    """ แปลงรหัส """
    salt= bcrypt.gensalt()
    hashed = bcrypt.hashpw(plain_password.encode("utf8"),salt)

    return hashed.decode("utf-8")

def check_password(plain_password: str,hashed_password: str) -> bool:
    """ เช็คการเข้ารหัสที่ผ่านการแปลงแล้ว"""
    return bcrypt.checkpw(
        plain_password.encode("utf-8"),
        hashed_password.encode("utf-8"),
        
    )