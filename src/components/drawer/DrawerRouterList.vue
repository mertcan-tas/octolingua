<template>
  <v-list-item
    v-for="item in menuItems"
    :key="item.name"
    :to="{ name: item.name }"
    link
    exact
    :class="{ 'active-link': $route.name === item.name }"
    class="py-2 px-3 mb-3"
  > 
    <v-list-item-title class="d-flex align-center tile font-weight-bold">
      <v-icon class="mr-4" size="32">
        <component :is="item.icon"></component>
      </v-icon>
      {{ item.title }}
    </v-list-item-title>
  </v-list-item>

  <DrawerShowMoreButton />
</template>

<script>
import IconLearn from "@/assets/icons/menu/IconLearn.vue";
import IconVoice from "@/assets/icons/menu/IconVoice.vue";
import IconScoreboard from "@/assets/icons/menu/IconScoreboard.vue";
import IconTasks from "@/assets/icons/menu/IconTasks.vue";
import IconStore from "@/assets/icons/menu/IconStore.vue";
import IconProfile from "@/assets/icons/menu/IconProfile.vue";

export default {
  component: "DrawerRouterList",
  components: {
    IconLearn,
    IconVoice,
    IconScoreboard,
    IconTasks,
    IconStore,
    IconProfile,
  },
  data() {
    return {
      menuItems: [
        { name: "home", title: "Öğren", icon: "IconLearn" },
        { name: "characters", title: "Sesler", icon: "IconVoice" },
        { name: "leaderboard", title: "Puan Tablosu", icon: "IconScoreboard" },
        { name: "quests", title: "Görevler", icon: "IconTasks" },
        { name: "shop", title: "Mağaza", icon: "IconStore" },
        { name: "profile", title: "Profil", icon: "IconProfile" },
      ],
    };
  },
};
</script>

<style scoped>
.tile {
  font-size: 15px;
  color: rgb(119, 119, 119);
  letter-spacing: 0.8px;
  text-transform: uppercase;
  transition: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  cursor: pointer;
  user-select: none;
}

.active-link {
  background-color: rgb(221, 244, 255) !important; /* Açık mavi bir arka plan */
  color: #1976d2 !important; /* Koyu mavi bir yazı rengi */

  border: 2px solid rgb(132, 216, 255);
  border-radius: 12px;
}

.v-list-item--active .v-list-item__title {
  color: inherit !important; /* Aktif öğenin başlığının rengini `.active-link` ten almasını sağlar */
}
</style>
