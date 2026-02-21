<script setup>
    import NavbarStudent from '../../components/NavbarStudent.vue'

    import headerStudent from '../../components/StudentContent/headerStudent.vue'
    import ContentStudent from '../../components/StudentContent/ContentStudent.vue'

    import Footer from '../../components/Footer.vue'
</script>

<template>
    <!-- ส่วนหัว -->
    <NavbarStudent />

    <!-- เนื้อหาหลัก -->
    <main class="min-h-screen bg-[#EBE8E8]">
        <!-- เนื้อหาหลัก ส่วนบน -->
        <headerStudent />
        <!-- เนื้อหาหลักกลาง ทั้งหมด -->
        <ContentStudent />
    </main>
    
    <!-- ส่วนท้าย -->
    <Footer />
</template>