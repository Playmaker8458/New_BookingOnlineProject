<script setup>
    import { RouterLink } from 'vue-router';
</script>

<template>
    <nav class="navbar sticky top-0 h-20 bg-[#1C6EA4] shadow-sm">
        <div class="navbar-start gap-5">
            <div class="dropdown bg-white m-2 rounded">
                <div tabindex="0" role="button" class="btn btn-ghost w-13 rounded-sm lg:hidden">
                   <v-icon name="bi-list" scale="1.5"/>
                </div>
                <ul tabindex="-1" class="menu dropdown-content bg-base-100 rounded-md z-1 mt-3 w-52 p-2 shadow">
                    <li><RouterLink to="/HomepageAdvisor">หน้าหลัก</RouterLink></li>
                    <li><RouterLink to="/ConsultationTimeSlot">จัดการช่วงเวลา</RouterLink></li>
                    <li><RouterLink to="/ManageQueueAdvisor">จัดการคิว</RouterLink></li>
                    <li><RouterLink to="/ConsultationTimeControl">เปิด-ปิดวันให้คำปรึกษา</RouterLink></li>
                </ul>
            </div>
            <img class="w-40 h-12 lg:h-13 lg:w-45" src="../assets/Logo_BORC.png" alt="Logo-BORC">
        </div>

        <div class="navbar-center hidden lg:flex">
            <ul class="flex px-1 text-white gap-10 text-lg">
                <li class="hover:text-gray-300">
                    <RouterLink to="/HomepageAdvisor">หน้าหลัก</RouterLink>
                </li>
                <li class="hover:text-gray-300">
                    <RouterLink to="/ConsultationTimeSlot">จัดการช่วงเวลา</RouterLink>
                </li>
                <li class="hover:text-gray-300">
                    <RouterLink to="/ManageQueueAdvisor">จัดการคิว</RouterLink>
                </li>
                <li class="hover:text-gray-300">
                    <RouterLink to="/ConsultationTimeControl">เปิด-ปิดวันให้คำปรึกษา</RouterLink>
                </li>
            </ul>
        </div>

        <div class="navbar-end mr-5">
            <div class="dropdown dropdown-end">
                <div tabindex="0" role="button" class="cursor-pointer">
                    <img class="w-14 rounded-full" src="https://img.daisyui.com/images/profile/demo/yellingcat@192.webp" />
                </div>
                <ul tabindex="-1" class="menu dropdown-content bg-white rounded-md mt-4 w-62 p-3">
                    <div class="flex items-center">
                        <v-icon name="bi-person-circle" scale="1.5"/>
                        <li><a href="#" class="font-bold hover:bg-gray-200 hover:text-gray-400">แก้ไขโปรไฟล์</a></li>
                    </div>
                    <li class="mt-2 mb-4"></li>
                    <li><a href="/LoginUser" class="btn bg-red-600 text-white rounded-md">ออกจากระบบ</a></li>
                </ul>
            </div>
        </div>
    </nav>
</template>