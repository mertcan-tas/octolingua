import { defineStore } from 'pinia'
import { v4 as uuidv4 } from 'uuid'

const TAB_ID_KEY = 'app_active_tab_id'
const TAB_TIMESTAMP_KEY = 'app_tab_last_active'
const CHECK_INTERVAL = 1000 // Check every second

export const useTabStore = defineStore('tab', {
  state: () => ({
    currentTabId: '',
    isActiveTab: true,
    lastActiveTabId: '',
    checkIntervalId: null
  }),
  
  actions: {
    initialize() {
      // Generate unique ID for this tab using uuid
      this.currentTabId = uuidv4()
      
      // Set this tab as active
      this.setActiveTab()
      
      // Start checking if this is the active tab
      this.startTabCheck()
      
      // Listen for storage changes from other tabs
      window.addEventListener('storage', this.handleStorageChange)
      
      // When tab is closing or refreshing, clean up
      window.addEventListener('beforeunload', this.cleanup)
    },
    
    setActiveTab() {
      localStorage.setItem(TAB_ID_KEY, this.currentTabId)
      localStorage.setItem(TAB_TIMESTAMP_KEY, Date.now().toString())
      this.isActiveTab = true
      this.lastActiveTabId = this.currentTabId
    },
    
    startTabCheck() {
      this.checkIntervalId = setInterval(() => {
        const activeTabId = localStorage.getItem(TAB_ID_KEY)
        const timestamp = localStorage.getItem(TAB_TIMESTAMP_KEY)
        
        // Update active status
        this.isActiveTab = activeTabId === this.currentTabId
        this.lastActiveTabId = activeTabId
        
        // If this is the active tab, update the timestamp
        if (this.isActiveTab) {
          localStorage.setItem(TAB_TIMESTAMP_KEY, Date.now().toString())
        }
        
        // If no activity for 5 seconds in the active tab, take over
        if (!this.isActiveTab && Date.now() - parseInt(timestamp) > 5000) {
          this.setActiveTab()
        }
      }, CHECK_INTERVAL)
    },
    
    handleStorageChange(event) {
      if (event.key === TAB_ID_KEY) {
        this.isActiveTab = event.newValue === this.currentTabId
        this.lastActiveTabId = event.newValue
      }
    },
    
    cleanup() {
      // If this was the active tab, clear the active tab
      if (this.isActiveTab) {
        localStorage.removeItem(TAB_ID_KEY)
        localStorage.removeItem(TAB_TIMESTAMP_KEY)
      }
      
      clearInterval(this.checkIntervalId)
      window.removeEventListener('storage', this.handleStorageChange)
    },
    
    activateThisTab() {
      this.setActiveTab()
    }
  }
})