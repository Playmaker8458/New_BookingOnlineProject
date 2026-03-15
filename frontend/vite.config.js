import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    tailwindcss(),
  ],
  // ngrok server (close or off)
  // server: {
  //   host: true,
  //   post: 5173,
  //   // บังคับให้ server ngrok รัน post:5173 (https) 
  //   allowedHosts: [
  //     "loan-paradisiacal-newfangledly.ngrok-free.dev",
  //     "53e2-2403-6200-88a2-cf07-758a-8591-4cda-4290.ngrok-free.app"
  //   ]
  // }
})