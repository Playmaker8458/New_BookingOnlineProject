<script setup>
    import { ref, computed } from 'vue'
    import { RouterLink } from 'vue-router';

    const searchQuery = ref(''); // ดึงข้อมูลชื่อผู้ใช้จาก input และกำหนดลงในตัวแปร searchQuery

    //  กำหนดข้อมูลผู้ใช้ทั้งหมดที่จะแสดงในตาราง มีทั้งหมด 5 row กับอีก 6 column
    const users = ref([
        { id: 1, firstName: 'แดง', lastName: 'อร่อยเลิศ', date: '18 ม.ค. 2569', time: '12:00 - 14:00', status: 'รออนุมัติ'},
        { id: 2, firstName: 'ชายชาติ', lastName: 'นครหลวง', date: '18 ม.ค. 2569', time: '15:00 - 17:00', status: 'รออนุมัติ'}
    ]);


    // filteredUser ตัวดึงข้อมูลหรือการกรองข้อมูล "ชื่อผู้ใช้" ทั้งหมด
    const filteredUser = computed(() => {
        const query = searchQuery.value;
        if (!searchQuery.value) {
            return users.value; // ส่งข้อมูลผู้ใช้กลับไปแสดงผลในตารางทั้งหมด 
        } else {
            return users.value.filter(user =>
                user.firstName.includes(query) || user.lastName.includes(query)
            ); // ส่งข้อมูลผู้ใช้ 1 คนในตารางกลับไปแสดงผล (ตามการรับค่า)
        }
    });
</script>

<template>
    <section class="min-h-screen px-4 py-8">
        <div class="flex flex-col items-center">
            <!-- Header -->
             <div class="w-full max-w-5xl font-bold mb-10">
                <h1 class="text-lg md:text-3xl lg:text-3xl">จัดการคิว</h1>
                <h1 class="text-sm text-gray-500 lg:text-lg">แสดงรายละเอียดข้อมูลจัดการคิวทั้งหมด</h1>
            </div>

            <!-- Card Container -->
            <div class="w-full max-w-5xl rounded-md bg-white shadow-sm p-4 p-8">

                <!-- Search -->
                <label class="input border border-gray-300 bg-white w-full mb-6 rounded-md lg:w-96 !static">
                    <v-icon name="bi-search" scale="1" class="text-gray-500" />
                    <input 
                        type="search" 
                        class="w-full outline-none placeholder:font-bold"
                        v-model="searchQuery"
                        placeholder="ค้นหารายชื่อ" 
                    />
                </label>

                <!-- Mobile & Tablet Card View  -->
                <div class="flex flex-col gap-4 lg:hidden">
                    <!-- Card Item -->
                    <div v-for="user in filteredUser" :key="user.id" 
                        class="rounded-md border border-gray-200 p-4 mb-5">
                        <!-- Info -->
                        <div class="mb-4 space-y-2 text-sm md:text-base">
                            <div class="flex justify-between">
                                <span class="text-gray-500">ชื่อนักศึกษา</span>
                                <span class="font-bold">{{ user.firstName }} {{ user.lastName }}</span>
                            </div>
                            <div class="flex justify-between">
                                <span class="text-gray-500">วันที่</span>
                                <span class="font-bold">{{user.date}}</span>
                            </div>
                            <div class="flex justify-between">
                                <span class="text-gray-500">เวลา</span>
                                <span class="font-bold">{{user.time}}</span>
                            </div>
                            <div class="flex justify-between items-center">
                                <span class="text-gray-500">สถานะ</span>
                                <span class="badge badge-warning font-bold gap-1">
                                    <div class="h-2 w-2 rounded-full bg-black"></div>
                                    {{user.status}}
                                </span>
                            </div>
                        </div>
                        <div class="my-5 h-0.5 bg-gray-200"></div>
                        <!-- Action Buttons -->
                        <div class="flex flex-col gap-4">
                            <button class="btn btn-sm w-full h-10 bg-blue-400 text-white w-auto rounded-md">
                                <v-icon name="bi-eye" scale="1" />
                                ดูรายละเอียด
                            </button>
                            <div class="dropdown dropdown-end w-full">
                                <div tabindex="0" role="button"
                                    class="btn btn-sm w-full h-10 bg-blue-700 text-white rounded-md">
                                    จัดการคิวนักศึกษา
                                    <v-icon name="bi-caret-down-fill" scale="1" />
                                </div>
                                <ul tabindex="0"
                                    class="dropdown-content menu mt-3 w-full rounded-md bg-base-100">
                                    <li><RouterLink to="/RescheduleAppointmentAdvisor">เลื่อนคิว</RouterLink></li>
                                    <li><a>อนุมัติ</a></li>
                                    <li><a>ยกเลิกคิว</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>

                    <!-- ข้อความเมื่อไม่มีข้อมูล -->
                    <div v-if="filteredUser.length === 0" class="text-center py-8 text-gray-500">
                        ไม่พบข้อมูลที่ค้นหา
                    </div>
                </div>

                <!-- Desktop Table View -->
                <div class="hidden  lg:block">
                    <table class="table w-full !static">
                        <thead>
                            <tr class="bg-blue-900 text-center text-lg text-white">
                                <th>ชื่อนักศึกษา</th>
                                <th>วันที่</th>
                                <th>เวลา</th>
                                <th>สถานะ</th>
                                <th>จัดการ</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(user, index) in filteredUser" :key="user.id" 
                                class='bg-base-200 text-center'>
                                <td class="font-bold">{{ user.firstName }} {{ user.lastName }}</td>
                                <td class="font-bold">{{user.date}}</td>
                                <td class="font-bold">{{user.time}}</td>
                                <td>
                                    <span class="badge badge-warning font-bold gap-1">
                                        <div class="h-2 w-2 rounded-full bg-black"></div>
                                        {{user.status}}
                                    </span>
                                </td>
                                <td>
                                    <div class="flex justify-center items-center gap-3">
                                        <button class="btn bg-blue-400 text-white rounded-md">
                                            <v-icon name="bi-eye" scale="1" />
                                            ดูรายละเอียด
                                        </button>
                                        <div class="dropdown dropdown-end relative">
                                            <div tabindex="0" role="button"
                                                class="btn bg-blue-700 text-white rounded-md">
                                                จัดการคิวนักศึกษา
                                                <v-icon name="bi-caret-down-fill" scale="1" />
                                            </div>
                                            <ul tabindex="0"
                                                class="dropdown-content menu absolute z-[9999] mt-1 w-52 rounded-box bg-base-100 p-2 shadow top-full">
                                                <li><RouterLink to="/RescheduleAppointmentAdvisor">เลื่อนคิว</RouterLink></li>
                                                <li><a>อนุมัติ</a></li>
                                                <li><a>ยกเลิกคิว</a></li>
                                            </ul>
                                        </div>
                                    </div>
                                </td>
                            </tr>
                            <div v-if="filteredUser.length === 0" class="text-center font-bold  py-8 text-gray-500">
                                ไม่พบข้อมูลที่ค้นหา
                            </div>
                        </tbody>
                    </table>
                </div>

            </div>
        </div>
    </section>
</template>