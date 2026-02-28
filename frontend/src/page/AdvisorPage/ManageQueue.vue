<script setup>
    import NavbarAdvisor from '../../components/NavbarAdvisor.vue';
    import ListManageQueue from '../../components/AdvisorContent/List_ManageQueue.vue';
    import Footer from '../../components/Footer.vue';
</script>

<template>
    <NavbarAdvisor />
    <main class="min-h-screen bg-[#EBE8E8]">
        <ListManageQueue />
    </main>
    <Footer />
</template>