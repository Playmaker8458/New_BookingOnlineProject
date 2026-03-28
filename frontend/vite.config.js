import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import tailwindcss from '@tailwindcss/vite'
import path from 'path'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    tailwindcss(),
  ],
    server: { //test sever
    host: '0.0.0.0',   // สำคัญ
    port: 5173,
    strictPort: true,
    allowedHosts: true
  },
   resolve: {
    alias: {
      '@': path.resolve(__dirname, './src')
    }
  }
})