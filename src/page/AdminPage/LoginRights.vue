<script setup>
    import { ref, computed } from 'vue';
    import NavbarAdmin from '../../components/NavbarALL/NavbarAdmin.vue'
    import Footer from '../../components/Footer.vue'
    


    const searchQuery = ref(''); // ดึงข้อมูลชื่อผู้ใช้จาก input และกำหนดลงในตัวแปร searchQuery

    //  กำหนดข้อมูลผู้ใช้ทั้งหมดที่จะแสดงในตาราง มีทั้งหมด 5 row กับอีก 6 column
    const users = ref([
        { id: 1, firstName: 'นิมิต', lastName: 'อะไรก็ว่าไป', status: 'ยังไม่ยืนยัน', permission: 'ยังไม่ได้กำหนดสิทธิ์' },
        { id: 2, firstName: 'ณัฐวรรณ', lastName: 'เบเกอร์', status: 'ยังไม่ยืนยัน', permission: 'ยังไม่ได้กำหนดสิทธิ์' },
        { id: 3, firstName: 'ณัฐพงศ์', lastName: 'พันธะลา', status: 'ยังไม่ยืนยัน', permission: 'ยังไม่ได้กำหนดสิทธิ์' },
        { id: 4, firstName: 'พงศ์พล', lastName: 'ไชยชวลิตสกุล', status: 'ยังไม่ยืนยัน', permission: 'ยังไม่ได้กำหนดสิทธิ์' },
        { id: 5, firstName: 'กฤติเดช', lastName: 'เกลอรัตนกุล', status: 'ยังไม่ยืนยัน', permission: 'ยังไม่ได้กำหนดสิทธิ์' },
        { id: 6, firstName: 'โชคชัย', lastName: 'ไม่ใยดี', status: 'ยังไม่ยืนยัน', permission: 'ยังไม่ได้กำหนดสิทธิ์' },
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
</script>


<template>
    <NavbarAdmin />

    <main class="bg-[#EBE8E8] flex justify-center items-center py-12 px-4 min-h-[calc(96vh-100px)]">
        <section class="w-full max-w-5xl">
            <div class="mb-6">
                <h1 class="text-2xl md:text-3xl font-bold mb-1">กำหนดสิทธิ์การเข้าสู่ระบบ</h1>
                <p class="text-base md:text-lg font-semibold text-gray-700">
                    รายละเอียดข้อมูลกำหนดสิทธิ์การเข้าสู่ระบบทั้งหมด</p>
            </div>

            <div class="bg-white p-4 md:p-6 lg:p-10 rounded-lg">
                <!-- Search Input -->
                <div class="mb-6 md:mb-8">
                    <input v-model="searchQuery" type="text" placeholder="ค้นหารายชื่อ"
                        class="py-2 px-3 rounded-sm w-full lg:w-65" id="Search-Input"/>
                </div>

                <!-- Mobile/Tablet Card View (แสดงบนหน้าจอเล็กกว่า 1024px) -->
                <div class="lg:hidden space-y-4">
                    <div v-for="user in filteredUser" :key="user.id" 
                        class="bg-white border border-gray-200 rounded-lg shadow-sm p-5">
                        <div class="space-y-3">
                            <!-- ชื่อ-นามสกุล -->
                            <div class="flex justify-between items-start border-b border-gray-100 pb-3">
                                <div>
                                    <p class="text-sm text-gray-500 mb-1">ชื่อ-นามสกุล</p>
                                    <p class="text-base font-semibold">{{ user.firstName }} {{ user.lastName }}</p>
                                </div>
                            </div>

                            <!-- สถานะ -->
                            <div class="flex justify-between items-center">
                                <p class="text-sm text-gray-500">สถานะ</p>
                                <p class="text-sm font-medium text-yellow-600">{{ user.status }}</p>
                            </div>

                            <!-- ประเภท/สิทธิ์ -->
                            <div class="flex justify-between items-center">
                                <p class="text-sm text-gray-500">ประเภท/สิทธิ์</p>
                                <p class="text-sm font-medium text-right">{{ user.permission }}</p>
                            </div>

                            <!-- ปุ่มจัดการ -->
                            <div class="pt-3">
                                <button class="w-full bg-[#4665EC] text-white py-2.5 px-4 rounded cursor-pointer hover:bg-[#3651d4] transition-colors">
                                    ยืนยันสิทธิ์
                                </button>
                            </div>
                        </div>
                    </div>

                    <!-- ข้อความเมื่อไม่มีข้อมูล -->
                    <div v-if="filteredUser.length === 0" class="text-center py-8 text-gray-500">
                        ไม่พบข้อมูลที่ค้นหา
                    </div>
                </div>

                <!-- Desktop Table View (แสดงบนหน้าจอ 1024px ขึ้นไป) -->
                <div class="hidden lg:block bg-white shadow overflow-hidden">
                    <div class="overflow-x-auto">
                        <table class="min-w-[600px] w-250 lg:w-full">
                            <!-- Table Header -->
                            <thead class="bg-[#2E70D3] text-white">
                                <tr>
                                    <th class="px-4 py-3 text-center text-base md:text-lg font-semibold">ชื่อจริง</th>
                                    <th class="px-4 py-3 text-center text-base md:text-lg font-semibold">นามสกุล</th>
                                    <th class="px-4 py-3 text-center text-base md:text-lg font-semibold">สถานะ</th>
                                    <th class="px-4 py-3 text-center text-base md:text-lg font-semibold">ประเภท/สิทธิ์
                                    </th>
                                    <th class="px-4 py-3 text-center text-base md:text-lg font-semibold">จัดการ</th>
                                </tr>
                            </thead>

                            <tbody class="bg-white">
                                <!-- v-for จะนำชื่อที่เก็บเป็น object ที่ผ่านการกรองมาแสดงผลที่ละตัว -->
                                <tr v-for="(user, index) in filteredUser" :key="user.id"
                                    :class="{ 'border-b border-gray-200': index !== filteredUser.length - 1}">
                                    <td class="px-4 py-3 text-center text-sm md:text-base">{{ user.firstName }}</td>
                                    <td class="px-4 py-3 text-center text-sm md:text-base">{{ user.lastName }}</td>
                                    <td class="px-4 py-3 text-center text-sm md:text-base text-yellow-600">{{
                                        user.status }}</td>
                                    <td class="px-4 py-3 text-center text-sm md:text-base">{{ user.permission }}</td>
                                    <td class="px-4 py-3 text-center">
                                        <button class="bg-[#4665EC] cursor-pointer text-white py-2 px-6 rounded hover:bg-[#3651d4] transition-colors">ยืนยันสิทธิ์</button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <Footer />
</template>

<style scoped>
    #Search-Input{
        border: 2px solid rgb(161, 159, 159) !important;
    }
</style>