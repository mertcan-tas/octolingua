// ui.js - Pinia Store
import { defineStore } from 'pinia'

export const useUIStore = defineStore('ui', {
  state: () => ({
    isExplorerOpen: true,
  }),
  actions: {
    setExplorer(value) {
      this.isExplorerOpen = value
    },
    toggleExplorer() {
      this.isExplorerOpen = !this.isExplorerOpen
    },
  },
})