<script setup>
    import liff from '@line/liff'
    import { useUserStore } from '../stores/user'
    import { useRouter } from 'vue-router'


    const user = useUserStore() // กำหนด user store ที่ใช้ในการเก็บข้อมูล
    const router = useRouter() // กำหนด router เพื่อเรียกใช้ path ในนำทางไปยังหน้าที่กำหนด

    const Login = async () => {
        await liff.init({ liffId: import.meta.env.VITE_LIFF_ID });
        if (!liff.isLoggedIn()) {
            liff.login()
        }
        const data = await liff.getProfile() // กำหนดข้อมูลโปรไฟล์ ให้กับตัวแปร data
        user.setProfile(data)
        router.push('/LoginVerification')
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

                <!-- ✅ เปลี่ยนจาก onclick="main()" เป็น @click="main" -->
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