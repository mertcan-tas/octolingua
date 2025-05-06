<template>
  <TabController/>
  <RouterView />
  <NetworkController />
</template>

<script>
import TabController from '@/components/tab/TabController.vue'
import { useTabStore } from '@/plugins/stores/tabManager.js'

export default {
  name: 'App',
  components: {
    TabController
  },
  data() {
    return {
      tabStore: null
    }
  },
  created() {
    this.tabStore = useTabStore()
  },
  
  mounted() {
    this.tabStore.initialize()
  },
  
  beforeUnmount() {
    this.tabStore.cleanup()
  }
}
</script>