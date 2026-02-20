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
                <ul tabindex="-1" class="menu menu-md dropdown-content bg-base-100 rounded-sm z-1 mt-3 w-52 p-2 shadow">
                    <li><RouterLink to="/homepageAdmin">หน้าหลัก</RouterLink></li>
                    <li><RouterLink to="/loginrights">ยืนยันสิทธิ์การเข้าสู่ระบบ</RouterLink></li>
                    <li><RouterLink to="/manageuseraccounts">จัดการบัญชี</RouterLink></li>
                </ul>
            </div>
            <img class="w-40 h-12 lg:h-13 lg:w-45" src="../assets/Logo_BORC.png" alt="Logo-BORC">
        </div>
        <div class="navbar-center hidden lg:flex">
            <ul class="flex px-1 text-white gap-10 text-lg">
                <li class="hover:text-gray-300"><RouterLink to="/homepageAdmin">หน้าหลัก</RouterLink></li>
                <li class="hover:text-gray-300"><RouterLink to="/loginrights">ยืนยันสิทธิ์การเข้าสู่ระบบ</RouterLink></li>
                <li class="hover:text-gray-300"><RouterLink to="/manageuseraccounts">จัดการบัญชี</RouterLink></li>
            </ul>
        </div>

        <div class="navbar-end mr-5">
            <a href="/loginadmin" class="btn bg-red-600 rounded-md border-none shadow-none text-white p-5 text-sm lg:text-[16px] lg:p-5">ออกจากระบบ</a>
        </div>
    </nav>
</template>