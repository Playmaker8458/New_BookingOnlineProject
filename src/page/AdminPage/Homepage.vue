<script setup>
    import NavbarAdmin from '../../components/NavbarALL/NavbarAdmin.vue';

    import headerAdmin from '../../components/HeaderContent/headerAdmin.vue';
    import ContentAdmin from '../../components/ContentALL/ContentAdmin.vue';
    
    import Footer from '../../components/Footer.vue';
</script>

<template>
    <!-- ส่วนหัว -->
    <NavbarAdmin/>
    
    <!-- เนื้อหาทั้งหมด -->
    <main class="min-h-[150vh] bg-[#EBE8E8]">
        <!-- เนื้อหาหลักส่วนบน -->
        <headerAdmin />
        <!-- เนื้อหาหลักส่วนกลาง ทั้งหมด -->
        <ContentAdmin />
    </main>

    <!-- ส่วนท้าย -->
    <Footer/>
</template>