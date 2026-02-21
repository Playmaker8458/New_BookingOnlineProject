<script setup>
    import { RouterLink } from 'vue-router';
</script>

<template>
    <header class="flex flex-col lg:flex-row justify-center items-center bg-[#09153F] gap-8 lg:gap-20 p-6">
        <div class="w-full p-6 order-2 lg:w-auto lg:order-1 lg:pr-25">
            <div class="text-white mb-8 lg:mb-5">
                <h1 class="text-3xl text-center lg:text-4xl lg:text-left mb-3 font-bold">
                    จัดการช่วงเวลาให้คำปรึกษา
                </h1>
                <p class="text-center lg:text-lg lg:text-left">
                  อาจารย์สามารถจัดการช่วงเวลาให้คำปรึกษา <br class="hidden lg:block" /> 
                  แก่นักศึกษาได้เพื่อให้นักศึกษาจองคิวตามช่วงเวลา <br class="hidden lg:block" />
                  ที่อาจารย์กำหนดทั้งหมด 
                </p>
            </div>
            <RouterLink to="#" 
                class="btn rounded-md border-none text-xl p-6 bg-[#FFC107] text-black font-semibold w-full lg:w-auto lg:text-xl lg:p-6"> 
                จัดการช่วงเวลา >> 
            </RouterLink>
        </div>

        <img class="w-full max-w-sm rounded-md order-1 lg:w-100"  src="/image-Advisor.jpg" alt="image-admin">
    </header>
</template>