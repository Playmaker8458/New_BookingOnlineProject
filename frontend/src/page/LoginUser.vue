<script setup>
    import liff from '@line/liff'
    import { useUserStore } from '../stores/user'
    import { useRouter } from 'vue-router'

    const user = useUserStore(); // กำหนด useUserStore สำหรับส่งข้อมูลไปใช้งานภายนอกให้กับตัวแปร user
    const router = useRouter(); // กำหนด useRouter ที่ใช้สำหรับนำทางไปยังหน้าต่างให้กับตัวแปร router

    // Login ใช้สำหรับเข้าสู่ระบบหน้าเว็ปด้วย Line  
    const Login = async () => {
        try{
            await liff.init({ liffId: import.meta.env.VITE_LIFF_ID }); // กำหนด Liff ID ที่เก็บในไฟล์ .env สำหรับเริ่มต้นใช้งาน LINE Login
            console.log("LIFF init done")
            // เช็คสถานะการเข้าสู่ระบบของ Line
            if (!liff.isLoggedIn()) {
                liff.login();
                return;   // หากยังไม่เข้าสู่ระบบ ให้ทำการ Login ทันที
            };

            const data = await liff.getProfile(); // ดึงข้อมูลโปรไฟล์ของไลน์ เข้าไปเก็บในตัวแปร data 
            
            user.setProfile(data); // ส่งข้อมูลโปรไฟล์ของตัวแปร data เข้าไปเก็บใน useUserStore เพื่อให้สามารถเรียกใช้งานข้อมูลจากภายนอกได้
            router.push('/LoginVerification'); // ถ้า login แล้วก็จะนำทางไปยังหน้า "รอยืนยันสิทธิ์การเข้าสู่ระบบ"

        } catch (error) {
            console.log(`Line Liff Error: ${error}`)
        }
    };
</script>

<template>
    <div class="flex justify-center items-center min-h-screen bg-[#1C6EA4]">
        <div class="min-h-full flex-col px-10">
            <div class="sm:mx-auto sm:w-full sm:max-w-sm">
                <img src="../assets/Logo_BORC.png" alt="LOGO-BORC" class="mx-auto h-25 w-auto" />
            </div>

            <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
                <h1 class="text-white mb-4">ล็อคอินผ่านไลน์สำหรับนักศึกษา และ อาจารย์</h1>
                <button type="button" @click="Login()"
                    class="btn w-full bg-green-500 p-6 text-white border-none rounded-md shadow">
                    <div class="flex justify-center items-center gap-2">
                        <v-icon name="bi-line" scale="1.6" />
                        <h1 class="text-lg">เข้าสู่ระบบ</h1>
                    </div>
                </button>
            </div>
        </div>
    </div>
</template>