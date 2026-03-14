<script setup>
    import axios from 'axios';
    import { ref } from 'vue';
    import { useUserStore } from '../stores/user';

    const role = ref('');
    const prefix = ref('');
    const fristname = ref('');   
    const lastname = ref('');


    const user = useUserStore();

    const PostDataProfile = async () => {
        await axios.post('http://localhost:8000/register/api/test',{
            UserID: user.profile.userId,
            prefix: prefix.value,
            fristname: fristname.value,
            lastname: lastname.value,
            imageURL: user.profile.pictureUrl
        })

        .then(res => {
            console.log(res.data);
        })
    }

</script>

<template>
    <div class="min-h-screen bg-[#1C6EA4] flex flex-col items-center justify-center p-4">
        <div class="card bg-base-100 shadow-2xl w-full max-w-3xl rounded-md">
            <div class="p-5 bg-blue-500 rounded-t-md">
                <h1 class="text-white text-xl font-bold">กรอกข้อมูลผู้ใช้งานเพิ่มเติม</h1>
            </div>
            <div class="card-body gap-4 p-6">
                <!-- Role -->
                <fieldset class="fieldset">
                    <legend class="fieldset-legend text-sm">สิทธิ์ของผู้ใช้งาน</legend>
                    <select class="select select-bordered w-full rounded-md" v-model="role">
                        <option value="" disabled>เลือกสิทธิ์ผู้ใช้งาน</option>
                        <option value="student">นักศึกษา</option>
                        <option value="teacher">อาจารย์</option>
                    </select>
                </fieldset>

                <!-- Teacher Fields -->
                <template v-if="role == 'teacher'">
                    <div class="divider text-xs text-base-content/50 my-0">ข้อมูลอาจารย์</div>
                    <div class="grid grid-cols-3 gap-3 items-center">
                        <div class="w-full">
                            <h1 class="">ตำแหน่งทางวิชาการ</h1>
                            <select class="select select-bordered w-full rounded-md" v-model="prefix">
                                <option value="" disabled selected>เลือกตำแหน่ง</option>
                                <option value="ศาสตราจารย์">ศาสตราจารย์</option>
                                <option value="รองศาสตราจารย์">รองศาสตราจารย์</option>
                                <option value="ผู้ช่วยศาสตราจารย์<">ผู้ช่วยศาสตราจารย์</option>
                                <option value="อาจารย์">อาจารย์</option>
                            </select>
                        </div>
                        <div class="w-full">
                            <h1 class="text-sm">ชื่อจริง</h1>
                            <input type="text" class="input input-bordered w-full rounded-md" placeholder="First name" v-model="fristname"/>
                        </div>
                        <div class="w-full">
                            <h1 class="text-sm">นามสกุล</h1>
                            <input type="text" class="input input-bordered w-full rounded-md" placeholder="Last name" v-model="lastname"/>
                        </div>
                    </div>
                </template>

                <!-- Teacher Fields -->
                <template v-if="role == 'student'">
                    <div class="divider text-xs text-base-content/50 my-0">ข้อมูลนักศึกษา</div>
                    <div class="flex gap-4  items-center">
                        <div class="w-full">
                            <h1 class="">คำนำหน้าชื่อ</h1>
                            <select class="select select-bordered w-full rounded-md" v-model="prefix">
                                <option value="" disabled selected>เลือกคำนำหน้าชื่อ</option>
                                <option value="นาย">นาย</option>
                                <option value="นาง">นาง</option>
                                <option value="นางสาว">นางสาว</option>
                            </select>
                        </div>
                        <div class="w-full">
                            <h1 class="text-sm">ชื่อจริง</h1>
                            <input type="text" class="input input-bordered w-full rounded-md" placeholder="First name" v-model="fristname"/>
                        </div>
                        <div class="w-full">
                            <h1 class="text-sm">นามสกุล</h1>
                            <input type="text" class="input input-bordered w-full rounded-md" placeholder="Last name" v-model="lastname"/>
                        </div>
                    </div>
                </template>

                <!-- Footer -->
                <div class="card-actions justify-end mt-2 w-full">
                    <button 
                        class="btn btn-secondary text-white px-8 w-full rounded-md" 
                        @click="PostDataProfile()">
                        บันทึกข้อมูล
                    </button>
                </div>

            </div>
        </div>
    </div>
</template>