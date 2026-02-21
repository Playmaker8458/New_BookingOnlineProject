<script setup>
    import { RouterLink } from 'vue-router';
</script>

<template>
    <section>
        <div class="grid justify-center px-4 mb-10 md:mb-0 lg:mb-0 lg:px-6">
            <div class="font-bold mb-6 mt-5 lg:mb-4">
                <h1 class="text-xl sm:text-2xl md:text-3xl">จัดการคิว</h1>
                <h2 class="text-lg sm:text-base md:text-xl text-gray-600">รายละเอียดข้อมูลจัดการคิวทั้งหมด</h2>
            </div>
            <div class="bg-white rounded-md p-5 sm:p-4 md:p-6 lg:p-10">
                <div class="hidden gap-2 mb-4 md:flex md:justify-center  lg:flex lg:justify-center md:gap-5 lg:gap-40 lg:w-200">
                    <div class="text-gray-500 font-bold md:text-lg lg:text-xl ">
                        <h1>ชื่ออาจารย์ที่ปรึกษา:</h1>
                        <h1>วันที่จองคิว:</h1>
                        <h1>เวลาให้คำปรึกษา:</h1>
                        <h1>ประเภทหัวข้อที่จะปรึกษา:</h1>
                        <h1>สถานะปัจจุบัน:</h1>
                    </div>
                    <div class="font-bold md:text-lg lg:text-xl">
                        <h1 class="text-gray-500 break-words">ผู้ช่วยศาสตราจารย์นิมิต อะไรก็ว่าไป</h1>
                        <h1 class="text-gray-500">18 มกราคม 2569</h1>
                        <h1 class="text-gray-500">12:00-13:30</h1>
                        <h1 class="text-gray-500">ตรวจวิจัย</h1>
                        <h1 class="text-yellow-500">รออนุมัติการจองคิว</h1>
                    </div>
                </div>

                <div class="grid justify-center min-w-40 md:hidden lg:hidden text-sm">
                    <div class="font-bold mb-3">
                        <h1 class="text-gray-500">ชื่ออาจารย์ที่ปรึกษา:</h1>
                        <h1 class="text-gray-500">ผู้ช่วยศาสตราจารย์นิมิต อะไรก็ว่าไป</h1>
                    </div>
                    <div class="font-bold mb-3">
                        <h1 class="text-gray-500">วันที่จองคิว:</h1>
                        <h1 class="text-gray-500">18 มกราคม 2569</h1>
                    </div>
                    <div class="font-bold mb-3">
                        <h1 class="text-gray-500">เวลาให้คำปรึกษา:</h1>
                        <h1 class="text-gray-500">12:00-13:30</h1>
                    </div>
                    <div class="font-bold mb-3">
                        <h1 class="text-gray-500">ประเภทหัวข้อที่จะปรึกษา:</h1>
                        <h1 class="text-gray-500">ตรวจวิจัย</h1>
                    </div>
                    <div class="font-bold mb-5">
                        <h1 class="text-gray-500">สถานะปัจจุบัน:</h1>
                        <h1 class="text-yellow-600">รออนุมัติการจองคิว</h1>
                    </div>
                </div>

                <div class="grid gap-3 lg:flex lg:justify-center">
                    <button class="btn bg-red-800 text-white rounded-sm lg:w-87 lg:h-13">ยกเลิกการจองคิว</button>
                    <RouterLink to="/RescheduleAppointmentStudent" class="btn bg-teal-600 text-white rounded-sm lg:w-87 lg:h-13">เลื่อนการจองคิว</RouterLink>
                </div>
            </div>
        </div>
    </section>
</template>