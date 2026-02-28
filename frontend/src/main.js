import { createApp } from 'vue'
import  router  from './router'
import App from './App.vue'

// setup tailwindcss and daisyui
import './assets/style.css'

import { OhVueIcon, addIcons } from "oh-vue-icons";
import * as FaIcons from "oh-vue-icons/icons";

const Fa = Object.values({ ...FaIcons })
addIcons(...Fa)

const app = createApp(App) // กำหนดตัว render app เป็นค่าเริ่มต้น
app.component("v-icon", OhVueIcon) // กำหนดแท็ก icon ของ oh-vue-icons ให้กับ components vue
 
app.use(router) // ดึงตัวนำทางของหน้าต่างๆ กลับไปแสดงผลใน app.vue ที่มีการเรียกใช้ RouterView
app.mount('#app') // render หน้า page ทั้งหมดกลับไปให้ไฟล์ HTML ที่มีการกำหนด id app 