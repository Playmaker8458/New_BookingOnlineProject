<script setup>
    import axios from 'axios';
    import { ref, onMounted } from 'vue';

    const tableData = ref([]);

    const ShowData_API = async () => {
        await axios.post("http://localhost:8000/Table/LoginPermissions")
        .then(response_data => {
            console.log(response_data.data[0]);
            tableData.value = response_data.data[0];
        })
    };

    onMounted(() => {
        ShowData_API();
    });
</script>

<template>
    <h1 class="text-center font-bold text-4xl text-red-700" ref="DataTable"> 
        Hello World
    </h1>
    <Table>
        <tr>
            <th>ชื่อเต็มผู้ใช้งาน</th>
            <th>สถานะการเข้าสู่ระบบ</th>
            <th>ประเภท/สิทธิ์</th>
            <th>จัดการ</th>
        </tr>
        <tr>
            <td>{{ tableData.fullname }}</td>
            <td>{{ tableData.status_permissions }}</td>
            <td>{{ tableData.role_user }}</td>
        </tr>
    </Table>
</template>