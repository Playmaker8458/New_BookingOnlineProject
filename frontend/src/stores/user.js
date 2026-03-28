import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useUserStore = defineStore('user', () => {
    const profile = ref(null); // กำหนดค่าว่างให้กับตัวแปร profile เพื่อรอรับค่าจากภายนอก
    const role_user = ref(null); // กำหนดเก็บ role
    // setProfile ใช้เก็บข้อมูลที่ส่งเข้ามาจากภายนอก
    const setProfile = (data) => {
        // อัปเดตค่าใหม่ใหักับ profile ด้วยข้อมูลจากตัวแปร data
        profile.value = data;
    };

       const setRole = (role) => { // เพิ่ม
        role_user.value = role;
    };

    // ส่งตัวแปร profile และฟังก์ชั่น setProfile กลับไปใช้งานภายนอก
    return { profile, setProfile, role_user, setRole  } ;
});