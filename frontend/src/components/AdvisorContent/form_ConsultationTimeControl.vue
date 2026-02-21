<template>
    <section>
        <div class="flex flex-col items-center px-4 py-10">
            <!-- Header -->
            <div class="w-full max-w-2xl mb-6">
                <h1 class="text-2xl sm:text-3xl font-bold">หน้าเปิด-ปิดช่วงเวลาวันให้คำปรึกษา</h1>
                <p class="text-sm sm:text-base text-gray-500 mt-1">รายละเอียดตัวเปิด-ปิดวันให้คำปรึกษาทั้งหมด</p>
            </div>

            <!-- Card -->
            <div class="w-full max-w-2xl bg-white rounded-xl shadow-sm overflow-hidden">
                <!-- Date Picker Section -->
                <div class="p-5 sm:p-6 border-b border-gray-100">
                    <label class="block text-sm sm:text-base font-medium text-gray-700 mb-2">เลือกวันที่</label>
                    <input type="date" class="w-full text-sm border p-2 rounded-md cursor-pointer" />
                </div>

                <!-- Status Section -->
                <div class="flex flex-col items-center py-6 sm:py-8 bg-gray-100 border-b border-gray-100 gap-2">
                    <p class="text-sm sm:text-base text-gray-500">สถานะสำหรับวันที่</p>
                    <h2 class="text-2xl sm:text-3xl font-bold">22 มกราคม 2569</h2>
                    <span class="flex items-center gap-1 text-sm sm:text-base font-medium mt-1 bg-green-200 rounded-4xl p-2">
                        <v-icon name="bi-check-circle" scale="1.1" />
                        เปิดรับจอง 3 ช่วงเวลา
                    </span>
                </div>

                <!-- Time Slot Section -->
                <div class="p-5 sm:p-8">
                    <h3 class="text-center text-sm sm:text-base font-semibold mb-5 sm:mb-6 text-gray-700">
                        เลือกช่วงเวลาที่ต้องการจะเปิด-ปิด
                    </h3>

                    <!-- Time Slots -->
                    <div class="flex flex-col sm:flex-row justify-center gap-3 sm:gap-5 mb-6 sm:mb-8">
                        <!-- Slot 1 -->
                        <label class="flex items-center justify-between border border-gray-200 rounded-lg p-4 cursor-pointer hover:border-green-400 transition w-full sm:w-1/2">
                            <div class="flex items-center gap-3">
                                <input type="radio" name="timeslot" class="radio radio-sm radio-neutral" />
                                <span class="text-sm sm:text-base font-medium">12:00-14:00</span>
                            </div>
                            <span class="badge badge-sm bg-gray-100 text-gray-500 border-0">ว่าง</span>
                        </label>

                        <!-- Slot 2 -->
                        <label class="flex items-center justify-between border border-gray-200 rounded-lg p-4 cursor-pointer hover:border-green-400 transition w-full sm:w-1/2">
                            <div class="flex items-center gap-3">
                                <input type="radio" name="timeslot" class="radio radio-sm radio-neutral" />
                                <span class="text-sm sm:text-base font-medium">12:00-14:00</span>
                            </div>
                            <span class="badge badge-sm bg-gray-100 text-gray-500 border-0">ว่าง</span>
                        </label>
                    </div>

                    <!-- Action Buttons -->
                    <div class="flex flex-col sm:flex-row justify-center gap-3 sm:gap-5">
                        <button class="btn bg-red-500 hover:bg-red-600 text-white rounded-lg w-full sm:w-56 gap-2">
                            <v-icon name="fa-ban" scale="1" />
                            ปิดช่วงเวลา
                        </button>
                        <button class="btn bg-green-500 hover:bg-green-600 text-white rounded-lg w-full sm:w-56 gap-2">
                            <v-icon name="bi-check-circle-fill" scale="1" />
                            เปิดช่วงเวลา
                        </button>
                    </div>
                </div>

            </div>
        </div>
    </section>
</template>