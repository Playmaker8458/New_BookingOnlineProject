<script setup>
    import axios from 'axios';
    import { ref, onMounted } from 'vue';

    const tableData = ref([]); // กำหนดตัวจัดเก็บข้อมูล LineLogin ของผู้ใช้งานทั้งหมด (กำหนดเก็บเป็น List)

    const isdisabled = ref(false); // กำหนดตัวปิดการใช้งานปุ่มเป็น false
    const btn_style = ref({}); // กำหนดสีตัวปิดการใข้งานปุ่มเป็น ค่าว่าง หรือ ปีกกา(เปล่า)

    // ดึงข้อมูล LineLogin ของผู้ใช้จาก API ฝั่ง backend
    const ShowData_API = async () => {
        await axios.get("http://localhost:8000/Users/get_all_profiles")
            .then(response_data => {
                // เข้าถึงข้อมูลใน tableData และส่งข้อมูลผู้ใช้จาก LineLogin เข้าไปเก็บใน List
                tableData.value = response_data.data;
            });
    
        // เช็คสถานะการเข้าสู่ระบบของผู้ใช้ว่าเป็น "นักศึกษา" หรือ "อาจารย์" 
        if (tableData.value[0].role_user == "นักศึกษา" || tableData.value[0].role_user == "อาจารย์"){
            // กำหนดค่าตัวปิดการใช้งานปุ่มเป็น true [ปิดปุ่ม]
            isdisabled.value = true
            // กำหนดค่าสีตัวปิดการใช้งานปุ่มเป็นสี "CadetBlue" 
            btn_style.value = {backgroundColor : '#9CADAE'}; 
        } else {
            // กำหนดค่าตัวปิดการใช้งานปุ่มเป็นค่าเดิมกลับไป [เปิดปุ่ม]
            isdisabled.value = false 
        }
    };

    // Update ข้อมูลสิทธิ์การเข้าสู่ระบบ ของผู้ใช้ผ่าน API ฝั่ง backend
    const UpdateData_API = async (user) => {
        await axios.put(`http://localhost:8000/Update/LoginRightsData/${user.id}`,{
            role_user: user.role_user
        })
        // เมื่อส่งข้อมูลไปอัพเดตสำเร็จ จะบังคับ reload หน้าเว็ปทันที
        location.reload();
    }

    onMounted(() => {
        ShowData_API();
    });
</script>

<template>
    <div class="flex justify-center items-center min-h-screen">
        <table class="table-sm w-200">
            <thead class="bg-blue-600 text-white">
                <tr>
                    <!-- Table Header -->
                    <th class="px-4 py-3 text-center text-base md:text-lg font-semibold">ชื่อผู้ใช้งาน</th>
                    <th class="px-4 py-3 text-center text-base md:text-lg font-semibold">สถานะ</th>
                    <th class="px-4 py-3 text-center text-base md:text-lg font-semibold">ประเภท/สิทธิ์</th>
                    <th class="px-4 py-3 text-center text-base md:text-lg font-semibold">จัดการ</th>
                </tr>
            </thead>
            <tbody class="bg-white border border-gray-200">
                <tr v-for="user in tableData"">
                    <td class="px-4 py-3 text-center text-sm font-bold md:text-base">{{ user.fullname }}</td>
                    <td class="px-4 py-3 text-center text-sm font-bold md:text-base">{{ user.status_permissions }}</td>
                    <td class="px-4 py-3 text-center text-sm font-bold md:text-base">{{ user.role_user }}</td>
                    <td class="text-center">

                        <!-- ปุ่มยืนยันสิทธิ์การเข้าสู่ระบบ -->
                        <button 
                            class="btn bg-orange-500 text-white rounded-md w-full" 
                            :disabled="isdisabled" 
                            :style="btn_style"
                            @click="$refs['modal_'+user.id][0].showModal()">
                            กำหนดสิทธิ์
                        </button>

                        <!-- card หรือ popup กำหนดสิทธิ์การเข้าสู่ระบบ -->
                        <dialog :ref="'modal_'+user.id" class="modal">
                            <div class="modal-box">
                                <div class="flex flex-col items-center gap-5 mb-5">
                                    <h3 class="text-2xl font-bold mt-3">กำหนดสิทธิ์การเข้าสู่ระบบ</h3>
                                    <img class="w-60 h-60" :src="user.profile_image" alt="Image_LineLogin">
                                </div>

                                <!-- card ลายละเอียดข้อมูล LineLogin ของผู้ใช้งาน -->
                                <div class="text-left bg-neutral-300 p-4 ">
                                    <h1 class="text-lg font-bold">ข้อมูลผู้ใช้งานจาก LINE</h1>
                                    <div class="text-[14px]">
                                        <h1>ชื่อ: {{ user.fullname }}</h1>
                                        <h1>สถานะการยืนยันสิทธิ์: {{ user.status_permissions }}</h1>
                                        <h1>สิทธิ์การเข้าสู่ระบบ: {{ user.role_user }}</h1>
                                    </div>
                                </div>
                                
                                <!-- from กำหนดสิทธิ์การเข้าสู่ระบบของผู้ใช้งานระบ -->
                                <div class="modal-action">
                                    <form method="dialog" class="w-full">
                                        <div class="text-left">
                                            <label class="text-lg font-bold">กำหนดสิทธิ์ในการเข้าสู่ระบบ</label>
                                            <select class="select rounded-md w-full mb-5 mt-2" v-model="user.role_user">
                                                <option disabled>เลือกสิทธิ์</option>
                                                <option>นักศึกษา</option>
                                                <option>อาจารย์</option>
                                            </select>
                                        </div>
                                        <!-- if there is a button in form, it will close the modal -->
                                        <div class="flex flex-col gap-3">
                                            <button 
                                                type="button"
                                                class="btn bg-neutral-300 w-full rounded-md hover:bg-neutral-400"
                                                @click="UpdateData_API(user)">
                                                ยืนยันสิทธิ์การเข้าสู่ระบบ
                                            </button>
                                            <button class="btn bg-red-600 text-white w-full rounded-md hover:bg-red-500">ยกเลิก</button>
                                        </div>
                                    </form>
                                </div>
                            </div>
                        </dialog>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>