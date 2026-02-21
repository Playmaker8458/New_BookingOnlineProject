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
        <div class="grid justify-center items-center p-10">
            <h1 class="text-xl mb-5 font-bold">
                <v-icon name="bi-app-indicator" scale="1.5" />
                สถานะคิวทั้งหมด
            </h1>

            <div class="flex flex-col justify-center gap-5 min-w-75 font-bold md:flex lg:flex md:flex-row md:min-w-150 lg:min-w-200">
                <div class="flex justify-between items-center bg-white rounded-md p-5 shadow-sm md:w-70 lg:w-97.5 md:gap-10 lg:gap-35">
                    <div class="ml-7">
                        <h1 class="text-md md:text-md lg:text-lg">รออนุมัติ</h1>
                        <h1 class="text-2xl md:text-3xl lg:text-4xl">1</h1>
                    </div>
                    <div class="mr-5 bg-yellow-200 rounded-full p-2"><v-icon name="bi-clock" scale="1.5" /></div>
                </div>

                <div class="flex justify-between items-center bg-white rounded-md p-5 shadow-sm md:w-70 lg:w-97.5 md:gap-10 lg:gap-35">
                    <div class="ml-7">
                        <h1 class="text-md md:text-md lg:text-lg">อนุมัติแล้ว</h1>
                        <h1 class="text-2xl md:text-3xl lg:text-4xl">2</h1>
                    </div>
                    <div class="mr-5 bg-green-300 rounded-full p-2"><v-icon name="bi-calendar4" scale="1.5" /></div>
                </div>
            </div>
        </div>
    </section>

    <section>
        <div class="grid justify-center items-center mb-10 ">
            <h1 class="text-xl mb-5 font-bold">
                <v-icon name="bi-hourglass-top" scale="1.5" />
                ข้อมูลการจองคิวของนักศึกษา
            </h1>
            <!-- ขนาดหน้าจอมือถือ (300px - 600px ลงไป) -->
            <div class="bg-white min-w-75 rounded-md p-6 shadow-sm md:hidden lg:hidden">
                <div class="text-gray-500 mb-3 font-bold">
                    <h1>ชื่ออาจารย์ที่ปรึกษา:</h1>
                    <h1>ผู้ช่วยศาสตราจารย์นิมิต อะไรก็ว่าไป</h1>
                </div>  
                <div class="bg-gray-100 h-0.5 mb-3"></div> 
                <div class="text-gray-500 mb-3 font-bold">
                    <h1>วันที่จองคิว:</h1>
                    <h1>18 มกราคม 2569</h1>
                </div>  
                <div class="bg-gray-100 h-0.5 mb-3"></div> 
                <div class="text-gray-500 mb-3 font-bold">
                    <h1>เวลาให้คำปรึกษา:</h1>
                    <h1>12:00-13:30</h1>
                </div>  
                <div class="bg-gray-100 h-0.5 mb-3"></div>
                <div class="text-gray-500  font-bold">
                    <h1>ประเภทหัวข้อที่จะปรึกษา:</h1>
                    <h1>ตรวจวิจัย</h1>
                </div>  
            </div>
            <!-- ขนาดจอใหญ่ + ขนาดจอแท็บเล็ต (600px - 1000px ขึ้นไป) -->
            <div class="hidden bg-white rounded-md shadow-sm md:flex md:justify-around lg:flex lg:justify-around md:min-w-150 md:p-5 lg:min-w-200">
                <div class="text-gray-500 font-bold md:text-md lg:text-lg">
                    <h1>ชื่ออาจารย์ที่ปรึกษา:</h1>
                    <h1>วันที่จองคิว:</h1>
                    <h1>เวลาให้คำปรึกษา:</h1>
                    <h1>ประเภทหัวข้อที่จะปรึกษา:</h1>
                </div>    
                <div class="text-gray-500 font-bold md:text-md lg:text-lg">
                    <h1>ผู้ช่วยศาสตราจารย์นิมิต อะไรก็ว่าไป</h1>
                    <h1>18 มกราคม 2569</h1>
                    <h1>12:00-13:30</h1>
                    <h1>ตรวจวิจัย</h1>
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
            
            <div class="w-75 shadow-sm md:w-150 lg:w-200 mb-10">
                <div class="bg-white rounded-lg p-6 shadow">
                    <h2 class="text-black font-bold mb-4">สถิติการการจองคิวรายเดือน</h2>
                    <canvas ref="Register"></canvas>
                </div>
            </div>
        </div>
    </section>
</template>