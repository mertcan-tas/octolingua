<template>
  <v-navigation-drawer
    v-model="localExplorerOpen"
    :temporary="false"
    :permanent="!isMobile"
    elevation="1"
    class="custom-drawer"
  >
    <DrawerBaseList />
  </v-navigation-drawer>
</template>

<script>
import { useUIStore } from "@/plugins/stores/ui.js";
import { mapState, mapActions } from "pinia";

export default {
  data() {
    return {
      isMobile: false,
    };
  },
  mounted() {
    this.isMobile = window.innerWidth <= 960;
    window.addEventListener("resize", this.checkScreenSize);
    // Drawer durumunu parent bileşene bildir
    this.$nextTick(() => {
      document.body.classList.toggle("drawer-closed", !this.localExplorerOpen);
    });
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.checkScreenSize);
  },
  watch: {
    localExplorerOpen(val) {
      // Drawer durumu değiştiğinde class'ı güncelle
      document.body.classList.toggle("drawer-closed", !val);
    },
  },
  computed: {
    ...mapState(useUIStore, ["isExplorerOpen"]),
    localExplorerOpen: {
      get() {
        return this.isExplorerOpen;
      },
      set(val) {
        this.setExplorer(val);
      },
    },
  },
  methods: {
    ...mapActions(useUIStore, ["setExplorer", "toggleExplorer"]),
    checkScreenSize() {
      this.isMobile = window.innerWidth <= 960;
      if (this.isMobile && this.localExplorerOpen) {
        this.setExplorer(false);
      }
    },
  },
};
</script>

<style scoped>
.custom-drawer {
  position: fixed !important;
  top: 0 !important;
  left: 0 !important;
  height: 100% !important;
  z-index: 4;
}

@media (min-width: 961px) {
  .custom-drawer {
    position: fixed !important;
    transform: translateX(0) !important;
  }
}
</style>
