import { ref } from 'vue';
import { defineStore } from 'pinia';

export const useUserStore = defineStore('user', () => {
    const profile = ref(null); // กำหนดค่าว่างให้กับตัวแปร profile เพื่อรอรับค่าจากภายนอก
    const token = ref(null);

    // setProfile ใช้เก็บข้อมูลที่ส่งเข้ามาจากภายนอก
    const setProfile = (data) => {
        profile.value = data;
    };

    // setToken ใช้เก็บ token ที่ส่งเข้ามาจากภายนอก
    const setToken = (Token) => {
        token.value = Token
    }

    // ส่งข้อมูล profile และ กลับไปใช้งานภายนอก
    return { profile, setProfile,  token, setToken } ;
});