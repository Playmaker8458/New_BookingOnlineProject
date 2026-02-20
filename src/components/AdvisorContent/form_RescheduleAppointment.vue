<template>
    <section class="grid justify-center mb-10">
        <div class="mt-10 mb-10 font-bold">
            <h1 class="text-lg md:text-xl lg:text-3xl">เลื่อนการจองคิว</h1>
            <h1 class="text-sm text-gray-600 md:text-lg lg:text-lg">กรุณากรอกวันและเวลาที่ต้องการเลื่อนคิวใหม่อีกครั้ง</h1>
        </div>

        <!-- ขนาดหน้าจอคอม + ขนาดหน้าจอ ipad (600px - 1000px ขึ้นไป) -->
        <div class="hidden bg-white p-5 w-full rounded-md md:flex md:justify-center lg:flex lg:justify-center md:w-150 lg:w-200 md:gap-10 lg:gap-20">
            <div class="font-bold md:text-md lg:text-lg">
                <h1 class="text-gray-600">ชื่อนักศึกษา:</h1>
                <h1 class="text-gray-600">วันที่จองคิว:</h1>
                <h1 class="text-gray-600">เวลาที่จองคิว:</h1>
                <h1 class="text-gray-600">ประเภทหัวข้อที่จะปรึกษา:</h1>
                <h1 class="text-gray-600">สถานะปัจจุบัน:</h1>
            </div>
            <div class="font-bold md:text-md lg:text-lg">
                <h1 class="text-gray-600 break-words">แดง อร่อยเลิศ</h1>
                <h1 class="text-gray-600">18 มกราคม 2569</h1>
                <h1 class="text-gray-600">12:00-13:30</h1>
                <h1 class="text-gray-600">ตรวจวิจัย</h1>
                <h1 class="text-yellow-600">รอการเลื่อนคิว</h1>
            </div>
        </div>

        <!-- ขนาดหน้าจอมือถือ (324px - 600px) -->
        <div class="grid justify-start min-w-40 bg-white p-5 rounded-md text-sm md:hidden lg:hidden">
            <div class="font-bold mb-3">
                <h1 class="text-gray-500">ชื่ออาจารย์ที่ปรึกษา:</h1>
                <h1 class="text-gray-500">ผู้ช่วยศาสตราจารย์นิมิต อะไรก็ว่าไป</h1>
            </div>
            <div class="font-bold mb-3">
                <h1 class="text-gray-500">วันที่จองคิว:</h1>
                <h1 class="text-gray-500">18 มกราคม 2569</h1>
            </div>
            <div class="font-bold mb-3">
                <h1 class="text-gray-500">เวลาที่จองคิว:</h1>
                <h1 class="text-gray-500">12:00-13:30</h1>
            </div>
            <div class="font-bold mb-3">
                <h1 class="text-gray-500">ประเภทหัวข้อที่จะปรึกษา:</h1>
                <h1 class="text-gray-500">ตรวจวิจัย</h1>
            </div>
            <div class="font-bold">
                <h1 class="text-gray-500">สถานะปัจจุบัน:</h1>
                <h1 class="text-yellow-600">รอการเลื่อนคิว</h1>
            </div>
            </div>
    </section>

    <section class="grid justify-center px-4">
        <div class="bg-white p-10 w-83 rounded-md mb-10 md:w-150 lg:w-200">
            <div class="w-full mb-5">
                <h1 class="mb-2 font-bold text-sm sm:text-base">วันที่เลื่อนคิว</h1>
                <input type="date" class="bg-gray-100 border-1 border-gray-300 p-2.5 w-full text-sm rounded-md cursor-pointer">
            </div>

            <div class="w-full mb-5">
                <h1 class="mb-2 font-bold text-sm sm:text-base">เวลาเลื่อนคิว</h1>
                <div class="flex gap-2 sm:gap-3 w-full bg-gray-200 p-2.5 sm:p-3 rounded-md mb-3">
                    <input type="radio" name="radio-1" class="radio !static flex-shrink-0" disabled/>
                    <h1 class="text-gray-400 font-bold text-sm sm:text-base">12:00-14:00 (เต็ม)</h1>
                </div>
                <div class="flex gap-2 sm:gap-3 w-full bg-gray-200 border-1 border-gray-300 p-2.5 sm:p-3 rounded-md mb-3">
                    <input type="radio" name="radio-1" class="radio !static flex-shrink-0" disabled/>
                    <h1 class="text-gray-400 font-bold text-sm sm:text-base">15:00-17:00 (ไม่ว่าง)</h1>
                </div>
                <div class="flex gap-2 sm:gap-3 w-full border-1 border-gray-300 p-2.5 sm:p-3 rounded-md mb-3">
                    <input type="radio" name="radio-1" class="radio !static flex-shrink-0"/>
                    <h1 class="text-gray-400 font-bold text-sm sm:text-base">18:00-20:00</h1>
                </div>
                <div class="flex gap-2 sm:gap-3 w-full border-1 border-gray-300 p-2.5 sm:p-3 rounded-md">
                    <input type="radio" name="radio-1" class="radio !static flex-shrink-0"/>
                    <h1 class="text-gray-400 font-bold text-sm sm:text-base">21:00-23:00</h1>
                </div>
            </div>

            <div class="w-full mb-6 sm:mb-10">
                <h1 class="mb-2 font-bold text-sm sm:text-base">เหตุผลในการเลื่อนคิว</h1>
                <select class="select w-full bg-gray-100 rounded-md cursor-pointer !static text-sm sm:text-base p-2.5">
                    <option disabled selected>กรุณาเลือกเหตุผลในการเลื่อนคิว</option>
                    <option>ติดประชุม</option>
                    <option>ติดสอน</option>
                    <option>ติดคุมสอบ</option>
                </select>
            </div>

            <div class="grid justify-center gap-3 lg:gap-5 lg:flex lg:justify-end">
                <button class="btn bg-gray-500 text-white rounded-md px-14 md:px-47 lg:px-10">ยกเลิก</button>
                <button class="btn bg-[#0A1B5E] text-white rounded-md px-14 md:px-47 lg:px-10">ยืนยันเลื่อนการจองคิว</button>
            </div>
        </div>
    </section>
</template>