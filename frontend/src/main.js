import { createApp } from 'vue'
import { router } from './router'
import { createPinia } from 'pinia'
import App from './App.vue'

// setup tailwindcss and daisyui
import './assets/style.css'


// Setup icon Defalse
import { OhVueIcon, addIcons } from "oh-vue-icons";
import * as FaIcons from "oh-vue-icons/icons/";

const Fa = Object.values({ ...FaIcons })
addIcons(...Fa)

const pinia = createPinia() // สร้างตัวจัดการสถานะ สำหรับส่งข้อมูลไปยังเพจต่างๆ
const app = createApp(App) // สร้างตัว render สำหรับใช้ในการแสดงหน้าเว็ปทั้งหมด
app.component("v-icon", OhVueIcon) // กำหนดแท็ก icon ของ oh-vue-icons ให้กับ components vue
app.use(pinia) // ดึงตัวจัดการสถานะ กลับไปใช้งานใน app.vue เพื่อให้ส่งข้อมูลกลับไปแสดงในเพจต่างๆได้
app.use(router) // ดึงตัวนำทางของหน้าต่างๆ กลับไปแสดงผลใน app.vue ที่มีการเรียกใช้ RouterView
app.mount('#app') // render หน้า page ทั้งหมดกลับไปให้ไฟล์ HTML ที่มีการกำหนด id app 