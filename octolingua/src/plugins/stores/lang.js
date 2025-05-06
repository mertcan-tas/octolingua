import { defineStore } from 'pinia'

export const useLangStore = defineStore('lang', {
  state: () => ({
    language: localStorage.getItem('language') || navigator.language || 'en',
  }),
  actions: {
    setLanguage(lang) {
      this.language = lang
      localStorage.setItem('language', lang)
    }
  }
})
