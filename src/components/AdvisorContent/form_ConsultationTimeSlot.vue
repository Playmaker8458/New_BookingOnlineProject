<template>
    <section>
        <div class="flex flex-col items-center px-3 sm:px-6">
            <div class="mt-13 mb-10 w-full max-w-3xl">
                <h1 class="text-xl sm:text-2xl lg:text-3xl font-bold">จัดการช่วงเวลาให้คำปรึกษา</h1>
                <h1 class="text-sm sm:text-base lg:text-lg text-gray-500">แสดงรายละเอียดจัดการช่วงเวลาให้คำปรึกษาทั้งหมด
                </h1>
            </div>

            <div class="bg-white p-4 sm:p-7 w-full max-w-3xl rounded-md mb-5">
                <h1 class="mb-2 font-bold text-sm sm:text-base">เลือกวันที่สำหรับจัดการช่วงเวลา</h1>
                <div class="flex flex-col sm:flex-row gap-3 sm:gap-6">
                    <input type="date"
                        class="border-1 border-gray-400 p-2 w-full rounded-md cursor-pointer text-sm sm:text-base">
                    <button
                        class="btn bg-blue-500 text-white px-4 py-2 sm:w-60 rounded-md text-sm sm:text-base whitespace-nowrap">แสดงช่วงเวลา</button>
                </div>
            </div>

            <div class="bg-white p-4 sm:p-7 w-full max-w-3xl rounded-md">
                <h1 class="mb-3 font-bold text-sm sm:text-base">+ เพิ่มช่วงเวลาใหม่</h1>
                <div class="flex flex-col sm:flex-row gap-3 sm:gap-6 mb-10">
                    <input type="time"
                        class="border-1 border-gray-400 p-2 w-full rounded-md cursor-pointer text-sm sm:text-base" />
                    <input type="time"
                        class="border-1 border-gray-400 p-2 w-full rounded-md cursor-pointer text-sm sm:text-base" />
                    <button
                        class="btn bg-green-600 text-white px-4 py-2 sm:w-60 rounded-md text-sm sm:text-base whitespace-nowrap">เพิ่มช่วงเวลา</button>
                </div>

                <div class="w-full max-w-3xl bg-white rounded-md shadow-sm mb-10 overflow-hidden">
                    <div class="bg-blue-800 px-4 sm:px-6 py-4">
                        <h2 class="text-white text-sm sm:text-lg font-semibold tracking-wide">
                            ช่วงเวลาให้คำปรึกษาทั้งหมด - วันที่ 19 มกราคม 2569
                        </h2>
                    </div>

                    <div class="overflow-x-auto">
                        <table class="w-full text-center">
                            <thead>
                                <tr
                                    class="bg-gray-50 border-b border-gray-200 text-gray-600 text-xs sm:text-sm font-semibold">
                                    <th class="py-3 sm:py-4 px-3 sm:px-6 text-left">เวลาเริ่มต้น</th>
                                    <th class="hidden sm:table-cell py-3 sm:py-4 px-3 sm:px-6">เวลาสิ้นสุด</th>
                                    <th class="py-3 sm:py-4 px-3 sm:px-6">สถานะ</th>
                                    <th class="py-3 sm:py-4 px-3 sm:px-6 text-right">จัดการช่วงเวลา</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-gray-100 text-gray-800 text-sm sm:text-base font-medium">
                                <tr class="row-anim hover:bg-blue-50 transition-colors duration-200">
                                    <td class="py-4 sm:py-5 px-3 sm:px-6 text-left font-bold">12:00</td>
                                    <td class="hidden sm:table-cell py-4 sm:py-5 px-3 sm:px-6">14:00</td>
                                    <td class="py-4 sm:py-5 px-3 sm:px-6">
                                        <span
                                            class="inline-block bg-green-100 text-green-700 text-xs sm:text-sm font-semibold px-2 sm:px-4 py-1 rounded-full">
                                            ว่าง
                                        </span>
                                    </td>
                                    <td class="py-4 sm:py-5 px-3 sm:px-6 text-right">
                                        <button
                                            class="inline-flex items-center gap-1 sm:gap-2 bg-red-500 hover:bg-red-600 active:scale-95 text-white text-xs sm:text-sm font-semibold px-3 sm:px-4 py-1.5 sm:py-2 rounded-lg transition-all duration-150">
                                            <v-icon name="bi-trash3" scale="1" />
                                            ลบ
                                        </button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <div id="summary"
                        class="bg-gray-50 border-t border-gray-200 px-4 sm:px-6 py-3 flex flex-col sm:flex-row flex-wrap items-start sm:items-center justify-between gap-2 text-xs sm:text-sm text-gray-600 font-medium">
                        <span id="total-label">รวมทั้งหมด 3 ช่วงเวลา</span>
                        <div class="flex gap-3 sm:gap-4">
                            <span id="available-label" class="text-green-600 font-semibold">ว่าง 2 ช่วงเวลา</span>
                            <span id="busy-label" class="text-yellow-600 font-semibold">ไม่ว่าง 1 ช่วงเวลา</span>
                        </div>
                    </div>
                </div>

                <button
                    class="btn w-full py-4 h-15 bg-blue-900 text-white rounded-md text-sm sm:text-base">บันทึกช่วงเวลาให้คำปรึกษา</button>
            </div>
        </div>
    </section>

    <section>
        <div class="flex flex-col items-center mt-10 px-3 sm:px-6">

            <div class="alert bg-blue-100 w-full max-w-3xl mb-5 border-1 border-gray-300 rounded-md shadow-sm p-0">
                <div class="bg-blue-800 w-0.5 h-full"></div>
                <div class="flex flex-col gap-2 p-4 sm:p-5">
                    <div class="flex items-center gap-2 font-bold">
                        <v-icon name="bi-info-circle" scale="1.5" />
                        <span class="text-lg sm:text-xl">หมายเหตุ</span>
                    </div>
                    <div class="ml-7 sm:ml-10 text-sm sm:text-md font-bold">
                        <li>ช่วงเวลาที่เพิ่มจะปรากฎในปฎิทินการจองคิวของนักศึกษาทันที</li>
                        <li class="text-red-600">ไม่สามารถลบช่วงเวลาที่มีสถานะ <span
                                class="text-green-600">"ไม่ว่าง"</span> ได้เพื่อป้องกันการกระทบต่อการจองคิวของนักศึกษา
                        </li>
                    </div>
                </div>
            </div>

            <div class="alert bg-red-100 w-full max-w-3xl mb-15 border-1 border-gray-300 rounded-md shadow-sm p-0">
                <div class="bg-red-800 w-0.5 h-full"></div>
                <div class="flex flex-col gap-2 p-4 sm:p-5">
                    <div class="flex items-center gap-2 font-bold">
                        <v-icon name="bi-lock" scale="1.5" />
                        <span class="text-lg sm:text-xl text-red-600">ระบบป้องกันการ <span>"ลบช่วงเวลา"</span>
                            ที่มีการจอง</span>
                    </div>
                    <div class="text-sm sm:text-base font-bold">
                        <h1>เพื่อป้องกันการลบช่วงเวลาที่นักศึกษาจองไว้
                            ระบบจะทำการล็อคช่วงเวลาและไม่สามารถลบช่วงเวลานั้นได้</h1>
                        <h1>เหตุผล: เพื่อป้องกันการยกเลิกช่วงเวลาที่มีการจองแล้วโดยไม่ได้ตั้งใจ</h1>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>
