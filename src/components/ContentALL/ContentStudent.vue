<script setup>
import { onMounted, ref } from "vue";
import Chart from "chart.js/auto";

const Register = ref(null); // กำหนดค่าของการจอง (เป็นค่าว่าง)

onMounted(() => {
    // สร้างข้อมูลของกราฟจำนวนการจองคิว
    new Chart(Register.value, {
        type: "bar",
        data: {
            labels: ["ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค."],
            datasets: [{
                label: "จำนวนการจอง",
                data: [12, 19, 25, 17, 30],
                backgroundColor: "#0f1f5c",
                borderRadius: 6
            }]
        }
    });
});
</script>


<template>
    <section>
        <div class="grid justify-center items-center p-10 ">
            <h1 class="text-xl mb-5 font-bold">
                <v-icon name="bi-app-indicator" scale="1.5" />
                สถานะคิวทั้งหมด
            </h1>
            <div class="min-w-105 md:min-w-150 lg:min-w-200 font-bold">
                <div class="flex justify-between items-center bg-white rounded-md mb-5 p-5">
                    <div class="ml-7">
                        <h1 class="text-lg">รออนุมัติ</h1>
                        <h1 class="text-4xl">1</h1>
                    </div>
                    <div class="mr-5 bg-yellow-200 rounded-full p-2"><v-icon name="bi-clock" scale="2" /></div>
                </div>
                <div class="flex justify-between items-center bg-white rounded-md p-5">
                    <div class="ml-7">
                        <h1 class="text-lg">อนุมัติแล้ว</h1>
                        <h1 class="text-4xl">2</h1>
                    </div>
                    <div class="mr-5 bg-green-300 rounded-full p-2"><v-icon name="bi-calendar4" scale="2" /></div>
                </div>
            </div>
        </div>
    </section>

    <section>
        <div class="grid justify-center items-center p-10">
            <h1 class="text-xl mb-5 font-bold">
                <v-icon name="bi-hourglass-top" scale="1.5" />
                ข้อมูลการจองคิวของนักศึกษา
            </h1>

            <div class="min-w-105 md:min-w-150 lg:min-w-200 font-bold">
                <div class="flex justify-center bg-white rounded-md mb-5 gap-20 text-gray-500 p-5 lg:p-10">
                    <div class="text-[11.5px] md:text-sm lg:text-lg">
                        <h1>ชื่ออาจารย์ที่ปรึกษา:</h1>
                        <h1>วันที่จองคิว:</h1>
                        <h1>เวลาให้คำปรึกษา:</h1>
                        <h1>ประเภทหัวข้อที่จะปรึกษา:</h1>
                    </div>
                    <div class="text-[11px] md:text-sm lg:text-lg">
                        <h1>ผูัช่วยศาสตร์จารย์นิมิต อะไรก็ว่าไป</h1>
                        <h1>18 มกราคม 2569</h1>
                        <h1>12:00-13:30</h1>
                        <h1>ตรวจวิจัย</h1>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section>
        <div class="grid justify-center items-center font-bold ">    
            <h1 class="text-xl mb-5 font-bold">
                <v-icon name="bi-bar-chart-fill" scale="2" />
                สถิติการจองคิว
            </h1>
            
            <div class="w-105 md:w-150 lg:w-200 mb-10">
                <div class="bg-white rounded-lg p-6 shadow">
                    <h2 class="text-black font-bold mb-4">สถิติการการจองคิวรายเดือน</h2>
                    <canvas ref="Register"></canvas>
                </div>
            </div>
        </div>
    </section>
</template>