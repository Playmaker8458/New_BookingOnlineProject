<script setup>
import axios from 'axios';
import { onMounted } from 'vue';
import { useUserStore } from '../stores/user';
import { useRouter } from 'vue-router';
import { API_BASE_URL } from '@/assets/config.js';

const user = useUserStore();
const router = useRouter();

const CreateData_API = async () => {
    const response = await axios.post(`${API_BASE_URL}/Login/LoginVerification`, {
        UserID: user.profile.userId,
        DisplayName: user.profile.displayName,
        ImageUrl: user.profile.pictureUrl,
    });
    console.log(response.data);
};

const CheckLoginRights = async () => {
    if (!user.profile) return; //  เช็คว่ามีผู้ใช้ไหม ถ้าไม่มีจะอยู่หน้าเดิม
    try {
        const res = await axios.post(`${API_BASE_URL}/Table/LoginRights`);
        // console.log("ข้อมูลทั้งหมด:", res.data)

        const approvedUsers = res.data.filter(
            u => u.status_permissions === "ยืนยันแล้ว"
        );

        // ใช้ find เพื่อได้ object ของ user คนนั้น
        const currentUser = approvedUsers.find(
            u => u.uuid_line === user.profile.userId
        );

        // console.log(" currentUser:", currentUser)

        if (!currentUser) return; // ยังไม่ได้รับสิทธิ์

        user.setRole(currentUser.role_user); //  เอา role จาก object ที่ find ได้ ตั้งจาก stores 

        // console.log(" role_user:", user.role_user)

        if (user.role_user === "นักศึกษา") {
            router.push("/Students/HomepageStudent");
        } else if (user.role_user === "อาจารย์") {
            router.push("/Advisor/HomepageAdvisor");
        }

    } catch (error) {
        console.error("เกิดข้อผิดพลาด", error);
    }
};

onMounted(() => {
    CreateData_API();
    CheckLoginRights();
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