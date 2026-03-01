<script setup>
    import { ref } from 'vue';
    import { useRouter } from 'vue-router';
    import axios  from 'axios';
    import { API_BASE_URL } from '../assets/config';

    const password = ref(''); // กำหนดรหัสผ่าน เป็นค่าว่าง
    const isVisible = ref(false); //กำหนดค่าให้กับ input tag เป็นค่าเท็จ

    const username = ref('');
    const message = ref('')
    const router = useRouter();

    const loading = ref(false);
    // TogglePassword เป็นตัวที่ให้ input tag แสดงรหัสผ่านออกมา
    const TogglePassword = () => {
        isVisible.value = !isVisible.value;
    };

    const handleLogin = async () => {
        loading.value = true;
        message.value = "";
        // ตรงนี้ต้องตรงกับ Backend router api
        try {
            const res = await axios.post(`${API_BASE_URL}/auth/login`,
                {
                    username: username.value,
                    password: password.value,
                },
                {
                    headers: {
                        "Content-Type": "application/json"
                    },
                }
            );

            if (res.data.access_token) {
                // token key
                const token = res.data.access_token;
                // ชื่อ key ตรง backend
                const expiresAt = Date.now() + 2 * 60 * 60 * 1000; // token อยู่ได้ 2 ชั่วโมง ุ60 นาทีต่อชั่วโมง 60 วินาทีต่อหนึ่งนาที 1000 มิลลิวินาทีต่อหนึ่งนาที = 1756568878973 วินาที         
                localStorage.setItem("access_token", token) //เก็บ toen ชื่อเดียวกัน
                localStorage.setItem("expiresAt", expiresAt)
                message.value = "เข้าสู่ระบบสำเร็จ";
                await router.push('/admin/homepageAdmin')
            } else {
                message.value = "เกิดข้อผิดพลาด Token ไม่ถูกต้อง"
            }
        } catch (err) {
            if (err.response && err.response.data && err.response.data.message) {
                message.value = err.response.data.message;
            } else if (err.response && err.response.data && err.response.data.error) {
                message.value = err.response.data.error;
            } else {
                message.value = "คุณไม่ใช่ Admin"; // เกิดข้อผิดพลาดในการเชื่อมต่อเซิร์ฟเวอร์
                alert(message.value)
            };

        } finally {
            loading.value = false
        }
    };
</script>

<template>
    <div class="flex justify-center items-center min-h-screen bg-[#1C6EA4]">
        <div class="min-h-full flex-col px-10">
            <div class="sm:mx-auto sm:w-full sm:max-w-sm">
                <img src="../assets/Logo_BORC.png" alt="LOGO-BORC" class="mx-auto h-30 w-auto" />
            </div>

            <div class="mt-13 sm:mx-auto sm:w-full sm:max-w-sm">
                <h1 class="text-white text-lg mb-4">กรูณาลงชื่อเข้าใช้สำหรับผู้ดูแลระบบ</h1>
                <form @submit.prevent="handleLogin" method="GET" class="space-y-6">
                    <div class="mt-2">
                        <input type="text" v-model="username" placeholder="ชื่อผู้ดูแลระบบ" required autocomplete="on"
                            class="input w-full rounded-md h-12  placeholder:font-bold " />
                    </div>

                    <div class="mt-2">
                        <input :type="isVisible ? 'text' : 'password'" v-model="password" placeholder="รหัสผ่าน"
                            required minlength="8" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}"
                            class="input validator w-full rounded-md h-12 placeholder:font-bold" />
                    </div>


                    <div class="flex gap-2 text-white text-lg">
                        <input @click="TogglePassword" type="checkbox" class="cursor-pointer w-5">
                        <h1>แสดงรหัสผ่าน</h1>
                    </div>

                    <div>
                        <button 
                            type="submit" :disabled="loading"
                            class="flex w-full justify-center rounded-md px-3 py-4 text-lg font-bold text-[#707070] bg-[#FFD43B] cursor-pointer hover:bg-[#DDC778] hover:text-[#707070] "
                            >
                        {{loading ? "กำลังเข้าสู่ระบบ":"เข้าสู่ระบบ"}}
                        </button>
                    </div>
                </form>
                <p class="mt-10 text-center text-md text-white">
                    กลับไปที่หน้าเพจหลัก?
                    <a href="/" class="font-bold hover:text-gray-400">หน้าเพจหลัก</a>
                </p>
            </div>
        </div>
    </div>
</template>
