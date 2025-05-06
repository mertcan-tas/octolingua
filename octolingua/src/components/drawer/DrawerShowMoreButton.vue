<template>
  <div class="dropdown-container">
    <v-list-item 
      @mouseenter="showMenu = true"
      class="py-2 px-3 mb-3 dropdown-trigger"
      style="cursor: pointer;"
    >
      <v-list-item-title class="d-flex align-center tile font-weight-black">
        <v-icon class="mr-2" size="32">
          <IconMore />
        </v-icon>
        Daha Fazla
      </v-list-item-title>
    </v-list-item>
    
    <v-card
      v-show="showMenu"
      class="dropdown-menu"
      @mouseleave="showMenu = false"
    >
      <v-list>
        <v-list-item @click="handleItemClick('test')">
          <v-list-item-title>test</v-list-item-title>
        </v-list-item>
        <v-list-item @click="handleItemClick('item2')">
          <v-list-item-title>Menü Öğesi 2</v-list-item-title>
        </v-list-item>
        <v-list-item @click="handleItemClick('item3')">
          <v-list-item-title>Menü Öğesi 3</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-card>
  </div>
</template>

<script>
import IconMore from "@/assets/icons/menu/IconMore.vue";

export default {
  name: "DrawerShowMoreButton",
  components: {
    IconMore
  },
  data: function() {
    return {
      showMenu: false
    };
  },
  methods: {
    handleItemClick: function(action) {
      console.log('Clicked:', action);
      this.showMenu = false;
      // İstediğiniz aksiyonu burada gerçekleştirebilirsiniz
    }
  }
};
</script>

<style scoped>
.dropdown-container {
  position: relative;
}

.dropdown-trigger {
  border-radius: 8px;
}

.dropdown-menu {
  position: absolute;
  left: 0;
  z-index: 100;
  min-width: 200px;
  margin-top: 4px;
}
</style>