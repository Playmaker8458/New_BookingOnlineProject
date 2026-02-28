<script setup>
    import axios from 'axios';
    import { onMounted } from 'vue';
    import { useUserStore } from '../stores/user';

    const user = useUserStore()

    const CreateData_API = async () => {
        await axios.post('http://localhost:8000/profile', {
            UserID: user.profile.userId,
            DisplayName: user.profile.displayName,
            ImageUrl: user.profile.pictureUrl,
        })

        .then(response_post => {
            console.log(response_post.data)
        })
    };
    onMounted(() => {
        CreateData_API();
    });
</script>

<template>
    <main class="flex justify-center items-center min-h-screen bg-[#1C6EA4]">
        <div class="text-center font-bold text-white">
            <h1 class="text-3xl mb-4">รอยืนยันสิทธิ์การเข้าสู่ระบบ</h1>
            <h1 class="text-lg">กรุณารอสักครู่ ผู้ดูแลระบบกำลังยืนยันสิทธิ์และเข้าสู่ระบบให้อัตโนมัติเมื่อได้รับสิทธิ์แล้ว</h1>
        </div>
    </main>
</template>