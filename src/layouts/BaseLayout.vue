<template>
  <v-app>
    <Appbar />
    <v-main>
      <slot></slot>
    </v-main>
    <AppFooter />
  </v-app>
</template>

<script>
export default {
  data() {
    return {

    };
  },
};
</script>
