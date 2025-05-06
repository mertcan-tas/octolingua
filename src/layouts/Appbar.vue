<!-- Appbar.vue -->
<template>
  <v-app-bar app color="transparent" elevation="0" height="60" class="custom-app-bar">
    <!-- <v-toolbar-title class="font-weight-bold">Polylingo</v-toolbar-title> -->
    
    <v-spacer></v-spacer>
    
    <v-toolbar-items>
      <v-btn icon size="small">
        <v-icon>mdi-settings</v-icon>
      </v-btn>
    </v-toolbar-items>
  </v-app-bar>
</template>

<script>
export default {
  name: 'Appbar'
}
</script>

<style scoped>
.custom-app-bar {
  width: calc(100% - 256px) !important; /* 256px, Vuetify'ın default drawer genişliği */
  left: 256px !important;
  z-index: 3;
}

/* Drawer kapalıyken */
.drawer-closed .custom-app-bar {
  width: 100% !important;
  left: 0 !important;
}

/* Mobil görünüm için */
@media (max-width: 960px) {
  .custom-app-bar {
    width: 100% !important;
    left: 0 !important;
  }
}
</style>