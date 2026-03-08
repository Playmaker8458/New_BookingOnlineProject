<script setup>
import { ref, computed } from 'vue'
import NavbarAdmin from '../../components/NavbarAdmin.vue'
import Footer from '../../components/Footer.vue'

const searchQuery = ref(''); // ดึงข้อมูลชื่อผู้ใช้จาก input และกำหนดลงในตัวแปร searchQuery

//  กำหนดข้อมูลผู้ใช้ทั้งหมดที่จะแสดงในตาราง มีทั้งหมด 5 row กับอีก 6 column
const users = ref([
    { id: 1, firstName: 'นิมิต', lastName: 'อะไรก็ว่าไป', status: 'ยืนยันสิทธิ์แล้ว', permission: 'อาจารย์', major: 'วิทยาการคอมพิวเตอร์และปัญญาประดิษฐ์'},
    { id: 2, firstName: 'นางโตะ', lastName: 'ซาโตชิ', status: 'ลบบัญชีแล้ว', permission: 'อาจารย์', major: 'วิทยาการคอมพิวเตอร์และปัญญาประดิษฐ์' },
    { id: 3, firstName: 'ณัฐพงศ์', lastName: 'พันธะลา', status: 'แก้ไขข้อมูลแล้ว', permission: 'นักศึกษา', major: 'วิทยาการคอมพิวเตอร์และปัญญาประดิษฐ์' },
]);


// filteredUser ตัวดึงข้อมูลหรือการกรองข้อมูล "ชื่อผู้ใช้" ทั้งหมด
const filteredUser = computed(() => {
    const query = searchQuery.value;
    if (!searchQuery.value) {
        return users.value; // ส่งข้อมูลผู้ใช้กลับไปแสดงผลในตารางทั้งหมด 
    } else {
        return users.value.filter(user =>
            user.firstName.includes(query) || user.lastName.includes(query)
        ); // ส่งข้อมูลผู้ใช้ 1 คนในตารางกลับไปแสดงผล (ตามการรับค่า)
    }
});

// ฟังก์ชันกำหนดสีสถานะ
const getStatusClass = (status) => {
    if (status === 'ยืนยันสิทธิ์แล้ว') return 'text-green-600 font-semibold'
    if (status === 'ลบบัญชีแล้ว') return 'text-red-600 font-semibold'
    if (status === 'แก้ไขข้อมูลแล้ว') return 'text-yellow-500 font-semibold'
    return ''
}
</script>

<template>
    <NavbarAdmin />

    <main class="bg-[#E5E2E2] min-h-[calc(100vh-120px)] py-14 px-6 flex justify-center">
        <section class="w-full max-w-6xl">

            <!-- หัวข้อ -->
            <div class="mb-10 ">
                <h1 class="text-4xl font-bold mb-2">ประวัติบัญชีผู้ใช้งาน</h1>
                <p class="text-gray-600 text-lg">รายละเอียดข้อมูลประวัติบัญชีผู้ใช้งานทั้งหมด</p>
            </div>

            <!-- กล่องค้นหา -->
            <div class="bg-[#FFFFFF] rounded-xl p-8 mb-10 ">
                <p class="text-lg font-semibold mb-4">ค้นหาข้อมูลผู้ใช้</p>

                <div class="relative">
                    <input
                        v-model="searchQuery"
                        type="text"
                        placeholder="-- ตัวเลือกกลุ่มผู้ใช้งาน --"
                        class="w-full border border-gray-400 rounded-lg py-3 px-4 pr-12 bg-white "
                        id="Search-Input"
                    />
                    <span class="absolute right-4 top-1/2 -translate-y-1/2 text-gray-600 text-xl">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" />
                        </svg>

                    </span>
                </div>
            </div>
            <!-- ตาราง -->
            <div class="bg-white p-4 md:p-6 lg:p-10 rounded-lg">

                <!-- Mobile/Tablet Card View (แสดงบนหน้าจอเล็กกว่า 1024px) -->
                <div class="lg:hidden space-y-4">

                    <div 
                        v-for="user in filteredUser" 
                        :key="user.id"
                        class="bg-[#E9E2E2] rounded-lg p-5 shadow-sm"
                    >
                        <!-- ชื่อ-นามสกุล -->
                        <div class="mb-3 border-b pb-2">
                            <p class="text-sm text-gray-500">ชื่อ-นามสกุล</p>
                            <p class="font-semibold">
                                {{ user.firstName }} {{ user.lastName }}
                            </p>
                        </div>

                        <!-- สถานะ -->
                        <div class="flex justify-between py-1">
                            <span class="text-sm text-gray-500">สถานะ</span>
                            <span :class="getStatusClass(user.status)">
                                {{ user.status }}
                            </span>
                        </div>

                        <!-- ประเภท/สิทธิ์ -->
                        <div class="flex justify-between py-1">
                            <span class="text-sm text-gray-500">ประเภท/สิทธิ์</span>
                            <span>{{ user.permission }}</span>
                        </div>

                        <!-- สาขาวิชา -->
                        <div class="flex justify-between py-1">
                            <span class="text-sm text-gray-500">สาขาวิชา</span>
                            <span class="text-right">
                                {{ user.major }}
                            </span>
                        </div>
                    </div>

                    <!-- ข้อความเมื่อไม่มีข้อมูล -->
                    <div v-if="filteredUser.length === 0" class="text-center py-6 text-gray-500">
                        ไม่พบข้อมูลที่ค้นหา
                    </div>
                </div>


                <!-- Desktop Table View (แสดงบนหน้าจอ 1024px ขึ้นไป) -->
                <div class="hidden lg:block">
                    <div class="overflow-x-auto">
                        <table class="w-full">
                            <!-- Table Header -->
                            <thead class="bg-gray-400 text-black">
                                <tr>
                                    <th class="py-4 text-center text-lg font-semibold">ชื่อจริง</th>
                                    <th class="py-4 text-center text-lg font-semibold">นามสกุล</th>
                                    <th class="py-4 text-center text-lg font-semibold">สถานะ</th>
                                    <th class="py-4 text-center text-lg font-semibold">ประเภท/สิทธิ์</th>
                                    <th class="py-4 text-center text-lg font-semibold">สาขาวิชา</th>
                                </tr>
                            </thead>

                            <tbody>
                                <!-- v-for จะนำชื่อที่เก็บเป็น object ที่ผ่านการกรองมาแสดงผลที่ละตัว -->
                                <tr
                                    v-for="(user, index) in filteredUser"
                                    :key="user.id"
                                    class="bg-[#E9E2E2]"
                                >
                                    <td class="py-4 text-center">{{ user.firstName }}</td>
                                    <td class="py-4 text-center">{{ user.lastName }}</td>
                                    <td class="py-4 text-center" :class="getStatusClass(user.status)">
                                        {{ user.status }}
                                    </td>
                                    <td class="py-4 text-center">{{ user.permission }}</td>
                                    <td class="py-4 text-center">{{ user.major }}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <!-- Pagination -->
                    <div class="flex justify-end items-center mt-6 gap-3">
                        <button class="px-3 py-1 border rounded">←</button>
                        <span class="px-4 py-1 border rounded bg-white">1</span>
                        <button class="px-3 py-1 border rounded">→</button>
                    </div>
                </div>

            </div>

        </section>
    </main>

    <Footer />
</template>


<style scoped>
#Search-Input {
    border: 2px solid bg-[#E9E2E2] !important;
}
</style>