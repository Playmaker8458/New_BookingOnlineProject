<script setup>
    import { RouterLink } from 'vue-router';
</script>

<template>
    <header class="flex flex-col lg:flex-row justify-center items-center bg-[#09153F] gap-8 lg:gap-15 p-6">
        <div class="w-full lg:w-auto p-6 order-2 lg:order-1">
            <div class="text-white mb-8  lg:mb-10 ">
                <h1 class="text-3xl text-center lg:text-4xl mb-3 font-bold">กำหนดสิทธิ์การเข้าสู่ระบบ</h1>
                <p class="text-center lg:text-lg lg:text-left ">
                  ผู้ดูแลระบบสามารถกำหนดสิทธิ์การเข้าสู่ระบบ <br class="hidden lg:block" /> 
                  ให้กับผู้ใช้ได้ว่าเป็นนักศึกษา หรืออาจารย์ <br class="hidden lg:block" />
                  หลังจากผู้ดูแลระบบกำหนดและยืนยันสิทธิ์ <br class="hidden lg:block" />
                  ผู้ใช้ถึงสามารถเข้าไปใช้งานระบบได้ตามปกติ
                </p>
            </div>
            <RouterLink 
                to="#" 
                class="btn rounded-md border-none text-2xl p-8 bg-[#FFC107] text-black font-semibold w-full lg:w-auto"> 
                กำหนดสิทธิ์ >> 
            </RouterLink>
        </div>

        <img class="w-full max-w-sm lg:w-85 order-1 lg:order-2"  src="/image-admin.png" alt="image-admin">
    </header>
</template>