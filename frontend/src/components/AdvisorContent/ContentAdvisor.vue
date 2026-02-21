<script setup>
    import { onMounted, ref } from "vue";
    import Chart from "chart.js/auto";

    const Register1 = ref(null); // กำหนดค่าของสถานะ (เป็นค่าว่าง)

    onMounted(() => {
        // สร้างข้อมูลของกราฟจำนวนสถานะคิว
        new Chart(Register1.value, {
            type: "bar",
            data: {
                labels: ["รอนุมัติ", "อนุมัติแล้ว", "สำเร็จ", "ยกเลิก"],
                datasets: [{
                    label: "จำนวนสถานะคิว",
                    data: [15, 30, 40, 10],
                    backgroundColor: "#0f1f5c",
                    borderRadius: 6
                }]
            }
        });
    });
</script>

<template>
    <section>
        <div class="grid justify-center p-10">
            <h1 class="text-xl mb-5 font-bold">
                <v-icon name="bi-app-indicator" scale="1.5" />
                สถานะคิวทั้งหมด
            </h1>
            <div class="flex flex-col justify-center gap-5 min-w-75 font-bold md:flex-row md:min-w-150 lg:min-w-200">
                <div class="flex justify-between items-center bg-white rounded-md h-25 w-full shadow-sm md:w-60 lg:w-63">
                    <div class="ml-7">
                        <h1 class="text-md md:text-md lg:text-lg">รออนุมัติ</h1>
                        <h1 class="text-2xl md:text-3xl lg:text-4xl">1</h1>
                    </div>
                    <div class="mr-5 bg-yellow-200 rounded-full p-2">
                        <v-icon name="bi-clock" scale="1.5" />
                    </div>
                </div>
            
                <div class="flex justify-between items-center bg-white rounded-md h-25 w-full shadow-sm md:w-60 lg:w-63">
                    <div class="ml-7">
                        <h1 class="text-md md:text-md lg:text-lg">อนุมัติแล้ว</h1>
                        <h1 class="text-2xl md:text-3xl lg:text-4xl">8</h1>
                    </div>
                    <div class="mr-5 bg-green-300 rounded-full p-2">
                        <v-icon name="bi-check2-circle" scale="1.5" />
                    </div>
                </div>
            
                <div class="flex justify-between items-center bg-white rounded-md h-25 w-full shadow-sm md:w-60 lg:w-63">
                    <div class="ml-7">
                        <h1 class="text-md md:text-md lg:text-lg">สัปดาห์นี้</h1>
                        <h1 class="text-2xl md:text-3xl lg:text-4xl">2</h1>
                    </div>
                    <div class="mr-5 bg-green-300 rounded-full p-2">
                        <v-icon name="bi-calendar4" scale="1.5" />
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section>
        <div class="grid justify-center mb-10">
            <h1 class="text-xl font-bold mb-5">
                <v-icon name="bi-clock" scale="1.5" />
                คิววันนี้
            </h1>
            <div class="bg-base-100 rounded-t-lg border border-gray-200 shadow-sm">
                <div class="flex justify-between items-center h-15">
                    <h1 class="ml-5 text-md text-gray-500 font-bold">รายการคิวทั้งหมด</h1>
                    <div class="badge bg-blue-800 h-7 mr-5">
                        <h1 class="text-white font-bold"><span>3</span> คิว</h1>
                    </div>
                </div>
            
                <div class="overflow-y-scroll max-h-70 w-75 md:max-h-50 md:w-180 lg:max-h-80 lg:w-200"> 
                    <div class="border border-gray-200 grid justify-center p-5 lg:flex lg:items-center">
                        <div class="flex flex-col items-center gap-5 p-5 md:flex-row lg:flex-row">
                            <div class="alert alert-info alert-soft">
                                <div class="ml-4 font-bold text-blue-800">
                                    <h1 class="text-lg">11:00</h1>
                                    <h1 class="text-lg">12:00</h1>
                                </div>
                            </div>
                            <div class="hidden bg-gray-300 w-0.5 h-15 lg:block"></div>
                            <div class="font-bold w-50 md:w-100 lg:w-100">
                                <h1 class="text-xl">นายแดง อร่อยเลิศ</h1>
                                <h1 class="text-lg text-gray-500">เรื่อง: <span>ปรึกษาวิจัย</span></h1>
                            </div>
                        </div>
                        <div class="badge bg-green-300 p-4.5">
                            <div class="status bg-green-600 p-1.5"></div>
                            <h1 class="text-lg">อนุมัติแล้ว</h1>
                        </div>
                    </div>
                    <div class="border border-gray-200 grid justify-center p-5 lg:flex lg:items-center">
                        <div class="flex flex-col items-center gap-5 p-5 md:flex-row lg:flex-row">
                            <div class="alert alert-info alert-soft">
                                <div class="ml-4 font-bold text-blue-800">
                                    <h1 class="text-lg">11:00</h1>
                                    <h1 class="text-lg">12:00</h1>
                                </div>
                            </div>
                            <div class="hidden bg-gray-300 w-0.5 h-15 lg:block"></div>
                            <div class="font-bold w-50 md:w-100 lg:w-100">
                                <h1 class="text-xl">นายแดง อร่อยเลิศ</h1>
                                <h1 class="text-lg text-gray-500">เรื่อง: <span>ปรึกษาวิจัย</span></h1>
                            </div>
                        </div>
                        <div class="badge bg-green-300 p-4.5">
                            <div class="status bg-green-600 p-1.5"></div>
                            <h1 class="text-lg">อนุมัติแล้ว</h1>
                        </div>
                    </div>
                    <div class="border border-gray-200 grid justify-center p-5 lg:flex lg:items-center">
                        <div class="flex flex-col items-center gap-5 p-5 md:flex-row lg:flex-row">
                            <div class="alert alert-info alert-soft">
                                <div class="ml-4 font-bold text-blue-800">
                                    <h1 class="text-lg">11:00</h1>
                                    <h1 class="text-lg">12:00</h1>
                                </div>
                            </div>
                            <div class="hidden bg-gray-300 w-0.5 h-15 lg:block"></div>
                            <div class="font-bold w-50 md:w-100 lg:w-100">
                                <h1 class="text-xl">นายแดง อร่อยเลิศ</h1>
                                <h1 class="text-lg text-gray-500">เรื่อง: <span>ปรึกษาวิจัย</span></h1>
                            </div>
                        </div>
                        <div class="badge bg-green-300 p-4.5">
                            <div class="status bg-green-600 p-1.5"></div>
                            <h1 class="text-lg">อนุมัติแล้ว</h1>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section>
        <div class="grid justify-center items-center font-bold ">    
            <h1 class="text-xl mb-5 font-bold">
                <v-icon name="bi-bar-chart-fill" scale="2" />
                สถิติสถานะคิวทั้งหมด
            </h1>
            
            <div class="w-75 mb-10 shadow-sm md:w-175 lg:w-200">
                <div class="bg-white rounded-lg p-6">
                    <h2 class="text-black font-bold mb-4">สถิติการการจองคิวรายเดือน</h2>
                    <canvas ref="Register1"></canvas>
                </div>
            </div>
        </div>
    </section>
</template>