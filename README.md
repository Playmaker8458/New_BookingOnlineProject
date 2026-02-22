---
# 📦 เครื่องมือที่ใช้ทั้งหมด
## Javascript
- Vite: ตัวติดตั้ง framework ทั้งหมด
- Vue 3: framework font-end
- vue-router: ตัวกำหนด path ในการนำทางไปยังหน้าเพจต่างๆของผู้ใช้ 
- Tailwind CSS และ Daysi UI: ตัวตกแต่งหน้าเว็ป
- oh-vue-icons: ไอคอนสำหรับตกแต่งหน้าเว็ป
- Axios: API สำหรับส่งข้อมูลของฟังก์ชั่น Frontend
- chart.js: กราฟแท่งสถิติสำหรับแสดงหน้าหลักของผู้ใช้แต่ละคน
- cally: ปฎิทินของผู้ใช้
- pinia: ใช้จัดการสถานะ ในการส่งค่าไปเก็บในตัวกลาง

## Python
- fastapi: API สำหรับส่งข้อมูลของฟังก์ชั่น Backend
- uvicorn: เป็น server ที่ใช้ในการรัน API เมื่อมีการเรียกใช้ --reload จะรีสตาร์สอัตโนมัติเมื่่อโค้ดมีการเปลี่ยนแปลง
---


# ⚙️ วิธีติดตั้งและรันโปรเจค
### 1️⃣ ติดตั้งส่วนเสริมทั้งหมดจาก package.json
```bash
npm install
```
### 2️⃣ รันโปรเจค
```bash
npm run dev
```

---
# 📘 วิธีอัปเดตโปรเจคขึ้น GitHub
#### เมื่อมีการแก้ไขไฟล์ในโปรเจคของเรา เวลาทำการอัพเดตขึ้น github ให้ใช้คำสั่งตามด้านล่าง

### 1️. ดึงไฟล์ในโฟลเดอร์ทั้งหมด เพื่อเตรียมไฟล์สำหรับการ Commit
```bash
git add .
```

### 2. สร้างโน๊ตสำหรับเปลี่ยนแปลงของไฟล์ที่ดึงมาทั้งหมด
```bash
git commit -m "ข้อความที่จะให้บันทึกสำหรับการอัพเดต"
```

### 3. ดึงไฟล์จากการ commit ทั้งหมดอัพเดตขึ้น github
```bash
git push
```
---

# 📘 วิธีการสร้าง Virtual Environment
#### ก่อนสร้าง env เราจะต้องสร้างโฟรเดอร์ก่อน เพื่อเก็บไฟล์ python กับ env ในการเก็บส่วนเสริม ให้ใช้คำสั่งตามด้านล่าง

### 1️. สร้างโฟรเดอร์
```bash
mkdir my_project
```

### 2. เข้าถึงโฟรเดอร์ที่เราสร้างก่อนหน้านี้
```bash
cd my_project
```

### 3. สร้าง Environment หรือ ตัวจำลองในการเก็บส่วนเสริมของ python
```bash 
python -m venv env
```
```bash 
python3 -m venv env
```
---
# 📘 วิธีเข้าถึง Virtual Environment
#### เมื่อสร้าง env เสร็จแล้วจะต้องทำการเรียกใช้งาน Environment ให้ใช้คำสั่งต่อไปนี้

### 1️. Activate venv สำหรับ Windows
```bash
env\Scripts\activate
```

### 2. Activate venv สำหรับ macOS/Linux
```bash
source env/bin/activate
```
---
# 📘 การ activate สำเร็จ
#### เมื่อ activate หรือ เข้าถึง Environment สำเร็จจะสามารถเข้าไปใช้งานได้ตามตัวอย่างด้านล่าง

### 1️. activate สำเร็จ ใน Windows 
```bash
(env) PS C:Users\playmaker\Downloads\my_project>
```
### 2. activate สำเร็จ ใน macOS/Linux
```bash
(env) playmaker@playmaker8458 my_project % 
```
---

# 📘 วิธีการออกจาก Virtual Environment (env)
#### วิธีการออกจาก Virtual Environment ให้ใช้คำสั่งตามด่านล่าง
### 1️. activate สำเร็จ ใน Windows 
```bash
deactivate
```
---