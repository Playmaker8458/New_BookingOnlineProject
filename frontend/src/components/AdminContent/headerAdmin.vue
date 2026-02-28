<script setup>
    import { RouterLink } from 'vue-router';
</script>

<template>
    <header class="flex flex-col lg:flex-row justify-center items-center bg-[#09153F] gap-8 lg:gap-20 p-6">
        <div class="w-full p-6 order-2 lg:w-auto lg:order-1 lg:pr-25">
            <div class="text-white mb-8 lg:mb-5">
                <h1 class="text-3xl text-center lg:text-4xl mb-5 font-bold">กำหนดสิทธิ์การเข้าสู่ระบบ</h1>
                <p class="text-center lg:text-lg lg:text-left">
                  ผู้ดูแลระบบสามารถกำหนดสิทธิ์การเข้าสู่ระบบ <br class="hidden lg:block" /> 
                  ให้กับผู้ใช้ได้ว่าเป็นนักศึกษา หรืออาจารย์ <br class="hidden lg:block" />
                  หลังจากผู้ดูแลระบบกำหนดและยืนยันสิทธิ์ <br class="hidden lg:block" />
                  ผู้ใช้ถึงสามารถเข้าไปใช้งานระบบได้ตามปกติ
                </p>
            </div>
            <RouterLink 
                to="#" 
                class="btn rounded-md border-none text-xl p-6 bg-[#FFC107] text-black font-semibold w-full lg:w-auto lg:text-xl lg:p-6"> 
                กำหนดสิทธิ์ >> 
            </RouterLink>
        </div>
        <img class="w-full max-w-sm rounded-md order-1 lg:w-100"  src="/image-admin.png" alt="image-admin">
    </header>
</template>