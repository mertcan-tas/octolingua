<template>
  <v-app-bar
    elevation="0"
    height="75"
    class="custom-app-bar px-4"
  >
    <v-btn link :to="{ name: 'home' }"
     class="no-hover" icon size="small" :ripple="false">
      <v-icon><IconClose /></v-icon>
    </v-btn>

    <v-spacer></v-spacer>

    <v-btn-primary >
        Giriş
      </v-btn-primary>
  </v-app-bar>
</template>

<script>
export default {

};
</script>

<style scoped>
@media (max-width: 960px) {
  .custom-app-bar {
    width: 100% !important;
    left: 0 !important;
  }
}
</style>
