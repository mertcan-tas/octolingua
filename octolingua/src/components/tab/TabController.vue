<template>

</template>

<script>
import { Report } from 'notiflix/build/notiflix-report-aio';
import { mapState, mapActions } from 'pinia'
import { useTabStore } from '@/plugins/stores/tabManager.js'

export default {
  name: 'TabController',
  
  computed: {
    ...mapState(useTabStore, ['isActiveTab'])
  },
  
  methods: {
    ...mapActions(useTabStore, ['activateThisTab']),
    
    activateTab() {
      this.activateThisTab()
    },
    
    warningDialog() {
      Report.warning(
        'Bu sekme aktif değil!',
        'Uygulamanın başka bir sekmesi açık durumda.',
        'Burada Kalacağım',
        () => {
          this.activateTab()
        },
        {
          fontFamily: 'Quicksand',
          backgroundColor: '#f8f8f8',
          
          messageMaxLength: 1923,
          plainText: false,
          warning: {
            svgColor: '#eebf31',
            titleColor: '#1e1e1e',
            messageColor: '#242424',
            buttonBackground: '#eebf31',
            buttonColor: '#fff',
            backOverlayColor: 'rgba(0,0,0,0.7)',
          },
        },
      );
    }
  },
  
  watch: {
    // isActiveTab değişimini izle
    isActiveTab(newValue, oldValue) {
      // Sekme aktiften inaktife geçtiyse dialog göster
      if (oldValue === true && newValue === false) {
        this.warningDialog()
      }
    }
  },
  
  mounted() {
    // İlk yüklendiğinde sekme aktif değilse dialogu göster
    if (!this.isActiveTab) {
      this.warningDialog()
    }
  }
}
</script>