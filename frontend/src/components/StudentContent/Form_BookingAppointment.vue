<script setup>
    import 'cally'
</script>
<template>
    <section>
        <div class="grid justify-center items-center p-5 md:p-10 lg:p-10">
            <div class="font-bold mt-2 lg:mt-5">
                <h1 class="text-lg md:text-2xl lg:text-3xl">จองคิวปรึกษาวิจัย</h1>
                <h1 class="text-sm md:text-base lg:text-lg text-gray-600">รายละเอียดฟอร์มสำหรับจองคิวเพื่อปรึกษาวิจัย</h1>
            </div>

            <div class="bg-white min-w-80 mt-5 rounded-md md:min-w-100 lg:min-w-200">
                <div class="rounded-md p-5 lg:p-10">
                    <div class="font-bold">
                        <h1 class="mb-2">อาจารย์ที่ปรึกษา</h1>
                        <select class="select w-full rounded-md font-thin cursor-pointer border border-base-400 !static">
                            <option disabled selected>กรุณาเลือกชื่อ อาจารย์</option>
                            <option>ผู้ช่วยศาสตร์จารย์นิมิต อะไรก็ว่าไป</option>
                            <option>รองศาสตราจารย์กายสิทธิ์ จิตติรังสรรค์</option>
                            <option>ศาสตราจารย์ชัยอนันต์ ดีวง</option>
                        </select>
                    </div>
                    
                    <div class="flex flex-col lg:flex-row lg:justify-between lg:gap-8">
                        <!-- ส่วนซ้าย: ปฏิทินและเวลา -->
                        <div class="w-full lg:w-1/2">
                            <div class="mt-8" id="calendar">
                                <h1 class="text-md font-bold mb-2">เลือกวันที่</h1>
                                <calendar-date class="flex justify-center bg-base-100 border border-base-300 rounded-md w-full p-5">
                                    <svg aria-label="Previous" class="fill-current size-4" slot="previous" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="currentColor" d="M15.75 19.5 8.25 12l7.5-7.5"></path></svg>
                                    <svg aria-label="Next" class="fill-current size-4 " slot="next" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="currentColor" d="m8.25 4.5 7.5 7.5-7.5 7.5"></path></svg>
                                    <calendar-month ></calendar-month>
                                </calendar-date>
                            </div>
                            
                            <div class="mt-5">
                                <h1 class="text-md font-bold mb-2">เลือกช่วงเวลา</h1>
                                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 ">
                                    <div class="flex gap-5 items-center">
                                        <input type="radio" name="radio-1" class="radio !static" checked="checked" />
                                        <p>12:00-14:00</p>
                                    </div>
                                    <div class="flex gap-5 items-center">
                                        <input type="radio" name="radio-1" class="radio !static" />
                                        <p>15:00-17:00</p>
                                    </div>
                                    <div class="flex gap-5 items-center">
                                        <input type="radio" name="radio-1" class="radio !static"/>
                                        <p>18:00-20:00</p>
                                    </div>
                                    <div class="flex gap-5 items-center">
                                        <input type="radio" name="radio-1" class="radio !static" />
                                        <p>21:00-23:00</p>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- ส่วนขวา: ประเภทและรายละเอียด -->
                        <div class="w-full lg:w-1/2 mt-8 lg:mt-0">
                            <div class="lg:mt-8">
                                <h1 class="mb-2 font-bold">ประเภทหัวข้อการปรึกษาวิจัย</h1>
                                <select class="select w-full rounded-md font-thin cursor-pointer border border-base-400 !static">
                                    <option disabled selected>เลือกประเภทการปรึกษาวิจัย</option>
                                    <option>ปรึกษาหัวข้อวิจัย</option>
                                    <option>ปรึกษาสโค็ปงานวิจัย</option>
                                    <option>ตรวจวิจัย [บทที่1-บทที่5]</option>
                                </select>
                            </div>
                            
                            <div class="mt-3">
                                <h1 class="mb-2 font-bold">รายละเอียดปัญหาวิจัย</h1>
                                <textarea class="textarea resize-y rounded-md w-full h-40 lg:h-93 border border-base-400"></textarea>
                            </div>
                        </div>
                    </div>

                    <div class="flex flex-col sm:flex-row gap-3 sm:gap-5 justify-end mt-8">
                        <button class="btn w-full sm:w-25 bg-gray-500 text-white rounded-md">ยกเลิก</button>
                        <button class="btn w-full sm:w-45 bg-indigo-800 text-white rounded-md">ยืนยันการจองคิว</button>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>