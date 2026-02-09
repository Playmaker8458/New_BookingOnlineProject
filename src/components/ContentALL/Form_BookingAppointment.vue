<script setup>
    import "cally";
</script>

<template>
    <section>
        <div class="grid justify-center items-center p-10">
            <div class="font-bold">
                <h1 class="text-3xl">จองคิวปรึกษาวิจัย</h1>
                <h1 class="text-lg text-gray-600">รายละเอียดฟอร์มสำหรับจองคิวเพื่อปรึกษาวิจัย</h1>
            </div>

            <div class="min-w-110 lg:min-w-200 mt-5">
                <div class="bg-white rounded-md p-10 ">
                    <div class="font-bold">
                        <h1 class="mb-2">อาจารย์ที่ปรึกษา</h1>
                        <select class="select w-full rounded-md font-thin cursor-pointer !static">
                            <option disabled selected>กรุณาเลือกชื่ออาจารย์</option>
                            <option>ผู้ช่วยศาสตร์จารย์นิมิต อะไรก็ว่าไป</option>
                            <option>รองศาสตราจารย์กายสิทธิ์ จิตติรังสรรค์</option>
                            <option>ศาสตราจารย์ชัยอนันต์ ดีวง</option>
                        </select>
                    </div>
                    
                    <div class="flex justify-between items-center">
                        <div>
                            <div class="mt-5 font-bold">
                                <h1 class="mb-3">เลือกวันที่</h1>
                                <calendar-date class="cally rounded-md border border-gray-300 w-75">
                                    <svg aria-label="Previous" class="fill-current size-4" slot="previous" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="currentColor" d="M15.75 19.5 8.25 12l7.5-7.5"></path></svg>
                                    <svg aria-label="Next" class="fill-current size-4" slot="next" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="currentColor" d="m8.25 4.5 7.5 7.5-7.5 7.5"></path></svg>
                                    <calendar-month class="text-lg"></calendar-month>
                                </calendar-date>
                            </div>

                            <div class="mt-5 font-bold">
                                <h1 class="mb-3">เลือกช่วงเวลา</h1>

                                <div class="flex gap-3 mb-3 font-thin">
                                    <div class="flex gap-2 mr-3">
                                        <input type="radio" name="radio-1" class="radio"/>
                                        <h1>12:00-14:00</h1>
                                    </div>
                                    <div class="flex gap-2">
                                        <input type="radio" name="radio-1" class="radio"/>
                                        <h1>12:00-14:00</h1>
                                    </div>
                                </div>

                                <div class="flex gap-3 font-thin">
                                    <div class="flex gap-2 mr-3">
                                        <input type="radio" name="radio-1" class="radio"/>
                                        <h1>15:00-17:00</h1>
                                    </div>
                                    <div class="flex gap-2">
                                        <input type="radio" name="radio-1" class="radio"/>
                                        <h1>21:00-23:00</h1>
                                    </div>
                                </div>

                            </div>
                        </div>
                        
                    </div>
                </div>
            </div>

        </div>
    </section>
</template>

<style>
</style>