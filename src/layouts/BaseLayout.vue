<template>
  <v-app>
    <div class="app-header-container">
      <ExplorerDrawer></ExplorerDrawer>
      <Appbar></Appbar>
    </div>
    <v-main class="custom-main">
      <slot></slot>
    </v-main>
  </v-app>
</template>

<script>
import Appbar from './Appbar.vue';
import ExplorerDrawer from './ExplorerDrawer.vue';
import { useUIStore } from '@/plugins/stores/ui.js';
import { mapState } from 'pinia';

export default {
  components: {
    Appbar,
    ExplorerDrawer
  },
  computed: {
    ...mapState(useUIStore, ['isExplorerOpen']),
  },
  data() {
    return {
      isMobile: false,
    };
  },
  mounted() {
    this.isMobile = window.innerWidth <= 960;
    window.addEventListener('resize', this.checkScreenSize);
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.checkScreenSize);
  },
  methods: {
    checkScreenSize() {
      this.isMobile = window.innerWidth <= 960;
    },
  },
};
</script>

<style>
.app-header-container {
  display: flex;
  position: fixed;
  width: 100%;
  top: 0;
  left: 0;
  z-index: 5;
}

.custom-main {
  padding-top: 60px !important; /* AppBar'ın height değerine göre ayarlayın */
}

@media (max-width: 960px) {
  .custom-main {
    padding-top: 60px !important;
    padding-left: 0 !important;
  }
}

@media (min-width: 961px) {
  .custom-main {
    padding-left: 256px !important; /* Drawer genişliğine göre ayarlayın */
  }
  
  .drawer-closed .custom-main {
    padding-left: 0 !important;
  }
}
</style>