<script setup>
    import { RouterLink } from 'vue-router';
</script>

<template>
    <nav class="navbar sticky top-0 h-30 bg-[#1C6EA4] shadow-sm">
        <div class="navbar-start gap-5">
            <div class="dropdown bg-white m-2 rounded">
                <div tabindex="0" role="button" class="btn btn-ghost rounded-sm lg:hidden">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h8m-8 6h16" /> </svg>
                </div>
                <ul tabindex="-1" class="menu menu-md dropdown-content bg-base-100 rounded-sm z-1 mt-3 w-52 p-2 shadow">
                    <li><RouterLink to="/homepageAdmin">หน้าหลัก</RouterLink></li>
                    <li><RouterLink to="/loginrights">ยืนยันสิทธิ์การเข้าสู่ระบบ</RouterLink></li>
                    <li><RouterLink to="/manageuseraccounts">จัดการบัญชี</RouterLink></li>
                </ul>
            </div>
            <img class="sm:h-17 lg:h-17 w-55" src="../../assets/Logo_BORC.png"  alt="Logo-BORC">
        </div>
        <div class="navbar-center hidden lg:flex">
            <ul class="flex px-1 text-white gap-10 text-xl">
                <li class="hover:text-gray-300"><RouterLink to="/homepageAdmin">หน้าหลัก</RouterLink></li>
                <li class="hover:text-gray-300"><RouterLink to="/loginrights">ยืนยันสิทธิ์การเข้าสู่ระบบ</RouterLink></li>
                <li class="hover:text-gray-300"><RouterLink to="/manageuseraccounts">จัดการบัญชี</RouterLink></li>
            </ul>
        </div>

        <div class="navbar-end mr-5">
            <a href="/loginadmin" class="btn bg-red-600 rounded-md border-none shadow-none text-white text-sm lg:text-lg lg:p-6.5 p-5">ออกจากระบบ</a>
        </div>
    </nav>
</template>