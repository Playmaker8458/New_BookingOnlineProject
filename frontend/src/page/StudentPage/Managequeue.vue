<script setup>
    import NavbarStudent from '../../components/NavbarStudent.vue'
    import Card_ManageQueue from '../../components/StudentContent/Card_ManageQueue.vue'
    import Footer from '../../components/Footer.vue'
</script>

<template>
    <div class="min-h-screen bg-[#4C4949]">
        <NavbarStudent />
        <main class="min-h-[75vh] bg-[#EBE8E8] flex justify-center items-center">
            <Card_ManageQueue />
        </main>
        <Footer />
    </div>
</template>