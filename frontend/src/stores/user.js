// stores/user.js
import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useUserStore = defineStore('user', () => {
    const profile = ref(null);

    const setProfile = (data) => {
        profile.value = data;
    };

    return { profile, setProfile } ;
});