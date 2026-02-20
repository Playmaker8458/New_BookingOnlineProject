<script setup>
    import NavbarAdvisor from '../../components/NavbarAdvisor.vue';
    
    import headerAdvisor from '../../components/AdvisorContent/headerAdvisor.vue';
    import ContentAdvisor from '../../components/AdvisorContent/ContentAdvisor.vue';
    
    import Footer from '../../components/Footer.vue'
</script>

<template>
    <!-- ส่วนหัว -->
    <NavbarAdvisor />

    <!-- เนื้อหาหลัก -->
    <main class="min-h-screen bg-[#EBE8E8]">
        <headerAdvisor/>
        <ContentAdvisor />
    </main>
    
    <!-- ส่วนท้าย -->
    <Footer />
</template>