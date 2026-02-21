<script setup>
import liff from '@line/liff';
import { ref, onMounted } from 'vue';

const isLoggedIn = ref(false);
const profile = ref(null); // เก็บข้อมูล profile

const initLiff = async () => {
    try {
        await liff.init({ liffId: import.meta.env.VITE_LIFF_ID});
        isLoggedIn.value = liff.isLoggedIn();

        // ถ้า login อยู่แล้ว ให้ดึง profile ทันที
        if (liff.isLoggedIn()) {
            profile.value = await liff.getProfile(); 
            console.log(profile.value);
        }
    } catch (error) {
        console.log(`Liff Init Error : ${error}`);
    }
};

const login = () => {
    if (!liff.isLoggedIn()) {
        liff.login(); // redirect ไป LINE login แล้วกลับมา
    }
};

const logout = () => {
    if (liff.isLoggedIn()) {
        liff.logout();
        isLoggedIn.value = false;
        window.location.reload(); // reload เพื่อ clear session
    }
};

onMounted(() => {
    initLiff();
});
</script>

<template>
    <div class="flex justify-center items-center min-h-screen bg-[#1C6EA4]">
        <div class="min-h-full flex-col px-10">
            <div class="sm:mx-auto sm:w-full sm:max-w-sm">
                <img src="../assets/Logo_BORC.png" alt="LOGO-BORC" class="mx-auto h-25 w-auto" />
            </div>
            <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
                <h1 class="text-white mb-4">ล็อคอินผ่านไลน์สำหรับนักศึกษา และ อาจารย์</h1>

                <!-- ปุ่ม Login -->
                <button v-if="!isLoggedIn" type="button" @click="login"
                    class="w-full p-2 gap-5 bg-[#1ABE4C] text-white font-semibold rounded-md cursor-pointer hover:bg-[#559167]">
                    <div class="flex justify-center items-center gap-2">
                        <v-icon name="bi-line" scale="2" />
                        <h1>เข้าสู่ระบบ</h1>
                    </div>
                </button>

                <!-- ปุ่ม Logout -->
                <button v-else type="button" @click="logout"
                    class="w-full p-2 gap-5 bg-red-500 text-white font-semibold rounded-md cursor-pointer hover:bg-red-700">
                    <div class="flex justify-center items-center gap-2">
                        <v-icon name="bi-box-arrow-right" scale="2" />
                        <h1>ออกจากระบบ</h1>
                    </div>
                </button>
            </div>
        </div>
    </div>
</template>