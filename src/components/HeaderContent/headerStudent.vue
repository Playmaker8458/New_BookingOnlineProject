<script setup>
    import { RouterLink } from 'vue-router';
</script>

<template>
    <header class="flex flex-col lg:flex-row justify-center items-center bg-[#09153F] gap-8 lg:gap-15 p-6">
        <div class="w-full lg:w-auto p-6 order-2 lg:order-1">
            <div class="text-white mb-8  lg:mb-10 ">
                <h1 class="text-3xl text-center lg:text-4xl lg:text-left mb-3 font-bold">จองคิวปรึกษาวิจัย</h1>
                <p class="text-center lg:text-lg lg:text-left ">
                  ระบบของเราจะให้คำปรึกษาในด้านการทำวิจัย <br class="hidden lg:block" /> 
                  ปรึกษาเรื่องโปรเจ็ค รองรับการจองล่วง <br class="hidden lg:block" />
                  และแจ้งเตือนผ่านไลน์
                </p>
            </div>
            <RouterLink 
                to="/BookAppointment" 
                class="btn rounded-md border-none text-2xl p-8 bg-[#FFC107] text-black font-semibold w-full lg:w-auto"> 
                จองคิวปรึกษาวิจัย >> 
            </RouterLink>
        </div>

        <img class="w-full max-w-sm lg:w-85 order-1 lg:order-2"  src="/image-student.png" alt="image-admin">
    </header>
</template>