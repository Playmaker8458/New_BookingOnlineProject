<script setup>
import { ref, computed, onMounted, onActivated } from 'vue'
import axios from 'axios'
import NavbarAdmin from '../../components/NavbarAdmin.vue'
import Footer from '../../components/Footer.vue'
import { API_BASE_URL } from '@/assets/config.js';
import { watch } from 'vue'


const searchQuery = ref('')
const users = ref([])

const paginatedUsers = computed(() => {
    const start = (currentPage.value - 1) * perPage
    const end = start + perPage
    return filteredUser.value.slice(start, end)
})

// ดึงข้อมูลจาก Backend
    const fetchUsers = async () => {
    try {

        const res = await axios.post(`${API_BASE_URL}/Table/LoginRights`)

        //  filter เฉพาะคนที่ยืนยันแล้ว ถึงจะเข้ามายังหน้านี้ได้
        const approvedUsers = res.data.filter(
            user => user.status_permissions === "ยืนยันแล้ว"
        )

        // map field ให้ตรงกับหน้าเว็บ ตรงนี้ยังไม่เสร็จ
        users.value = approvedUsers.map(user => ({
            id: user.id,
            firstName: user.first_name,
            lastName: user.last_name,
            status: user.status_permissions,   
            permission: user.role_user,
            // major: user.major
        }))

    } catch (error) {
        console.error("ดึงข้อมูลไม่สำเร็จ:", error)
    }
}
// โหลดข้อมูลตอนเปิดหน้า
onMounted(() => {
    fetchUsers()
})

// กรณีใช้ keep-alive แล้วกลับเข้าหน้าอีกครั้ง
onActivated(() => {
    fetchUsers()
})


//  Filter Search ฟังก์ชั่นค้นหา
const filteredUser = computed(() => {
    if (!searchQuery.value) return users.value

    return users.value.filter(user =>
        user.firstName?.includes(searchQuery.value) ||
        user.lastName?.includes(searchQuery.value)
    )
})

//  กำหนดสีสถานะ
const getStatusClass = (status) => {
    if (status === 'ยืนยันแล้ว') return 'text-green-600 font-semibold'
    if (status === 'ลบบัญชีแล้ว') return 'text-red-600 font-semibold'
    if (status === 'แก้ไขข้อมูลแล้ว') return 'text-yellow-500 font-semibold'
    return ''
}

const currentPage = ref(1)
const perPage = 3   // จำนวนข้อมูลต่อหน้า

const totalPages = computed(() => {
    return Math.ceil(filteredUser.value.length / perPage)
})



// ทุกครั้งที่ค่า searchQuery เปลี่ยน ให้ตั้ง currentPage กลับไปเป็นหน้า 1
watch(searchQuery, () => {
    currentPage.value = 1
})

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
                        placeholder="ค้นหาชื่อผู้ใช้..."
                        class="w-full border border-gray-400 rounded-lg py-3 px-4 pr-12 bg-white"
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

                <!-- Mobile View -->
                <div class="lg:hidden space-y-4">

                    <div 
                        v-for="user in paginatedUsers" 
                        :key="user.id"
                        class="bg-[#E9E2E2] rounded-lg p-5 shadow-sm"
                    >
                        <div class="mb-3 border-b pb-2">
                            <p class="text-sm text-gray-500">ชื่อ-นามสกุล</p>
                            <p class="font-semibold">
                                {{ user.firstName }} {{ user.lastName }}
                            </p>
                        </div>

                        <div class="flex justify-between py-1">
                            <span class="text-sm text-gray-500">สถานะ</span>
                            <span :class="getStatusClass(user.status)">
                                {{ user.status }}
                            </span>
                        </div>

                        <div class="flex justify-between py-1">
                            <span class="text-sm text-gray-500">ประเภท/สิทธิ์</span>
                            <span>{{ user.permission }}</span>
                        </div>

                        <div class="flex justify-between py-1">
                            <span class="text-sm text-gray-500">สาขาวิชา</span>
                            <span class="text-right">
                                {{ user.major }}
                            </span>
                        </div>
                    </div>

                    <div v-if="filteredUser.length === 0" class="text-center py-6 text-gray-500">
                        ไม่พบข้อมูลที่ค้นหา
                    </div>
                </div>


                <!-- Desktop Table -->
                <div class="hidden lg:block">
                    <div class="overflow-x-auto">
                        <table class="w-full">
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
                                <tr
                                    v-for="user in paginatedUsers"
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

               <div class="flex justify-end items-center mt-6 gap-3">

                        <!-- ปุ่มย้อนกลับ -->
                        <button
                            class="px-3 py-1 border rounded"
                            :disabled="currentPage === 1"
                            @click="currentPage--"
                        >
                            ←
                        </button>

                        <!-- แสดงหน้าปัจจุบัน -->
                        <span class="px-4 py-1 border rounded bg-white">
                            {{ currentPage }} / {{ totalPages }}
                        </span>

                        <!-- ปุ่มถัดไป -->
                        <button
                            class="px-3 py-1 border rounded"
                            :disabled="currentPage === totalPages || totalPages === 0"
                            @click="currentPage++"
                        >
                            →
                        </button>

                    </div>
                </div>

            </div>

        </section>
    </main>

    <Footer />
</template>

<style scoped>
#Search-Input {
    border: 2px solid #E9E2E2 !important;
}
</style>