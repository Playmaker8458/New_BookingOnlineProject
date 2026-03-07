import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    tailwindcss(),
  ],
    server: {
    allowedHosts: [
      '549f-49-229-211-126.ngrok-free.app'
    ]
  }
})