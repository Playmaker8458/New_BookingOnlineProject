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
                label: "จำนวนคนลงทะเบียน",
                data: [12, 19, 25, 17, 30],
                backgroundColor: "#0f1f5c",
                borderRadius: 6
            }]
        }
    });
});
</script>

<template>
    <div>
        <section>
            <div class="grid justify-center items-center font-bold m-10 gap-5">
                <div class="flex items-center text-lg mb-5">
                    <v-icon name="bi-people-fill" scale="3" />
                    <h1 class="text-2xl">ผู้ใช้งานระบบทั้งหมด</h1>
                </div>

                <div class="flex justify-center gap-10 md:flex-row md:gap-30">
                    <div
                        class="bg-white w-[180px] p-6 rounded-xl border border-gray-200 shadow-sm text-left md:w-[320px] md:p-8">
                        <div class="mb-5"><v-icon name="bi-person-fill" scale="2" /></div>
                        <h1 class="text-black text-sm md:text-xl lg:text-xl font-semibold mb-2">
                            จำนวนนักศึกษา
                        </h1>
                        <p class="text-black text-md md:text-2xl lg:text-2xl font-bold">
                            มีจำนวน 29 คน
                        </p>
                    </div>

                    <div
                        class="bg-white w-[180px] p-6 rounded-xl border border-gray-200 shadow-sm text-left md:w-[320px] md:p-8">
                        <div class="mb-5"><v-icon name="bi-person-fill" scale="2" /></div>
                        <h1 class="text-black text-sm md:text-xl lg:text-xl font-semibold mb-2">
                            จำนวนอาจารย์
                        </h1>
                        <p class="text-black text-md md:text-2xl lg:text-2xl font-bold">
                            มีจำนวน 5 คน
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <section>
            <div class="grid justify-center items-center font-bold ">
                <div class="flex items-center text-lg mb-5">
                    <v-icon name="bi-people-fill" scale="3" />
                    <h1 class="text-2xl">แดชบอร์ด</h1>
                </div>
                <div class="w-100 md:w-190 lg:w-190 mb-10">
                    <div class="bg-white rounded-lg p-6 shadow">
                        <h2 class="text-black font-bold mb-4">สถิติการลงทะเบียน</h2>
                        <canvas ref="Register"></canvas>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>