import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    hmr: {
      // Reduce HMR frequency to prevent rapid reloads
      overlay: true,
    },
    watch: {
      // Reduce file watching frequency
      usePolling: false,
    },
  },
})
