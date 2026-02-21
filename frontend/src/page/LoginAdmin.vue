<script setup>
    import { ref } from 'vue';

    const password = ref(''); // กำหนดรหัสผ่าน เป็นค่าว่าง
    const isVisible = ref(false); //กำหนดค่าให้กับ input tag เป็นค่าเท็จ

    // TogglePassword เป็นตัวที่ให้ input tag แสดงรหัสผ่านออกมา
    const TogglePassword = () => {
        isVisible.value = !isVisible.value;
    } 
</script>

<template>
    <div class="flex justify-center items-center min-h-screen bg-[#1C6EA4]">
        <div class="min-h-full flex-col px-10">
            <div class="sm:mx-auto sm:w-full sm:max-w-sm">
                <img 
                    src="../assets/Logo_BORC.png" 
                    alt="LOGO-BORC" 
                    class="mx-auto h-30 w-auto" 
                />
            </div>

            <div class="mt-13 sm:mx-auto sm:w-full sm:max-w-sm">
                <h1 class="text-white text-lg mb-4">กรูณาลงชื่อเข้าใช้สำหรับผู้ดูแลระบบ</h1>
                <form action="/homepageAdmin" method="GET" class="space-y-6">
                    <div class="mt-2">
                        <input 
                            type="text"
                            v-model="username"
                            placeholder="ชื่อผู้ดูแลระบบ" 
                            required
                            autocomplete="on"
                            class="input w-full rounded-md h-12  placeholder:font-bold " 
                        />
                    </div>

                    <div class="mt-2">
                        <input 
                            :type="isVisible ? 'text' : 'password'"
                            v-model="password"
                            placeholder="รหัสผ่าน" 
                            required
                            minlength="8"
                            pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}"  
                            class="input validator w-full rounded-md h-12 placeholder:font-bold" 
                        />
                    </div>


                    <div class="flex gap-2 text-white text-lg">
                        <input @click="TogglePassword"  type="checkbox" class="cursor-pointer w-5">
                        <h1>แสดงรหัสผ่าน</h1>
                    </div>

                    <div>
                        <button 
                            type="submit" 
                            class="flex w-full justify-center rounded-md px-3 py-4 text-lg font-bold text-[#707070] bg-[#FFD43B] cursor-pointer hover:bg-[#DDC778] hover:text-[#707070] "
                        >
                        เข้าสู่ระบบ
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
