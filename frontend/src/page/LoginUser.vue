<script setup>
    import axios from 'axios';
    import liff from '@line/liff';
    import { useUserStore } from '../stores/user';
    import { useRouter } from 'vue-router';
    
    const user = useUserStore(); // กำหนด useUserStore สำหรับส่งข้อมูลไปใช้งานภายนอกให้กับตัวแปร user
    const router = useRouter();

    // Login ใช้สำหรับเข้าสู่ระบบหน้าเว็ปด้วย Line  
    const Login = async () => {
        try{
            await liff.init({liffId: import.meta.env.VITE_LIFF_ID});
            if (!liff.isLoggedIn()){
                liff.login()
            };
            
            const profile = await liff.getProfile(); // ดึงข้อมูลโปรไฟล์ของไลน์ เข้าไปเก็บในตัวแปร data 
            const TokenId = liff.getIDToken(); // ดึง Token ผู้ใช้ของไลน์ที่เข้ารหัส เข้าไปเก็บในกับตัวแปร TokenId
            user.setProfile(profile);
            await axios.post('http://localhost:8000/Login/auth/VerifyRole',{
                token : TokenId
            })
            
            .then(res => {        
                if (res.data.Role == "new_user" && res.data.status == "No_Status"){
                    router.push('/RegisterForm')
                } else if (res.data.Role == "student" && res.data.status == "Taken_Action"){
                    router.push('/HomepageStudent')
                } else if (res.data.Role == "Advisor" && res.data.status == "Taken_Action"){
                    router.push('/HomepageAdvisor')
                } else {
                    router.push('/WaitingApproval')
                }
            })
        } catch (error) {
            console.log(`Line Liff Error: ${error}`);
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