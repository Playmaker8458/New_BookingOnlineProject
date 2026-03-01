<script setup>
    import { RouterLink } from 'vue-router';
</script>

<template>
    <div class="flex justify-center items-center min-h-100 gap-10">
        <RouterLink to="/loginUser" class="btn bg-blue-600 rounded-md text-white p-7">เข้าสู่ระบบ user</RouterLink> <br>
        <RouterLink to="/admin/loginadmin" class="btn bg-[#bd9c17] rounded-md text-white p-7">เข้าสู่ระบบ Admin</RouterLink>
    </div>
</template>