<template>
  <v-list nav class="pa-2">
    <v-list-item>
      <v-img width="128" height="30" contain class="ml-4 mb-4 mt-5">
        <AppLogo/>
      </v-img>
      <DrawerRouterList />
    </v-list-item>
  </v-list>
</template>

<script>
export default {
  name: "DrawerBaseList",
};
</script>
