<script setup>
    import { useUserStore } from '../stores/user';
    const user = useUserStore();
    console.log(user.profile)
</script>

<template>
    <main class="flex justify-center items-center min-h-screen bg-[#1C6EA4]">
        <div class="text-center font-bold text-white">
            <h1 class="text-3xl mb-4">รอผู้ดูแลระบบยืนยันสิทธิ์การเข้าสู่ระบบ</h1>
            <h1 class="text-lg">กรุณารอการยืนยันสิทธิ์การเข้าสู่ระบบสักครู่ ผู้ดูแลระบบกำลังดำเนินการให้</h1>
        </div>
    </main>
</template>