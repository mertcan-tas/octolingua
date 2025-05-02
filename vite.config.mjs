import Components from 'unplugin-vue-components/vite'
import Vue from '@vitejs/plugin-vue'
import Vuetify, { transformAssetUrls } from 'vite-plugin-vuetify'
import ViteFonts from 'unplugin-fonts/vite'
import vueDevTools from 'vite-plugin-vue-devtools'

import { defineConfig } from 'vite'
import { fileURLToPath, URL } from 'node:url'

export default defineConfig({
  plugins: [
    Vue({
      template: { transformAssetUrls },
    }),
    vueDevTools(),
    Vuetify(),
    Components({
      dirs: [
        'src/assets/*',
        'src/components/*',
        'src/layouts'
      ],
    }),
    ViteFonts({
      google: {
        families: [{
          name: 'Raleway',
          styles: 'wght@100;300;400;500;700;900',
        }],
      },
    }),
  ],
  optimizeDeps: {
    exclude: ['vuetify'],
  },
  define: { 'process.env': {} },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
    extensions: [
      '.js',
      '.json',
      '.jsx',
      '.mjs',
      '.ts',
      '.tsx',
      '.vue',
    ],
  },
  server: {
    port: 3000,
  },
  css: {
    preprocessorOptions: {
      sass: {
        api: 'modern-compiler',
      },
      scss: {
        api:'modern-compiler',
      },
    },
  },
})
