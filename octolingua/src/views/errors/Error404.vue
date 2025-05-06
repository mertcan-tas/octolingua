<template>
  <v-container class="fill-height">
    <v-row justify="center" align="center">
      <v-col cols="12" sm="8" md="6" class="text-center">
        <h2 class="mb-4">Duolingo Buton Tasarımı</h2>
        
 
        <v-hover v-slot="{ hover }">
          <v-btn
            class="duolingo-btn mb-6"
            :class="{ 'duolingo-btn-active': isActive || hover }"
            height="58"
            width="100%"
            elevation="0"
            @click="toggleActive"
          >
            <div class="d-flex align-center justify-start w-100">
              <div class="btn-choice mx-3" :class="{ 'btn-choice-active': isActive || hover }">
                1
              </div>
              <div class="btn-text" :class="{ 'btn-text-active': isActive || hover }">
                {{ buttonText }}
              </div>
            </div>
          </v-btn>
        </v-hover>
        

        <div>
          <v-btn
            block
      
            elevation="0"
            class="button-19 text-uppercase font-weight-bold"
            @click="checkAnswer"
          >
            {{ checkButtonText }}
          </v-btn>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'DuolingoButton',
  props: {
    buttonText: {
      type: String,
      default: '¡Tenemos que pagar la cuenta!'
    },
    checkButtonText: {
      type: String,
      default: 'Check'
    }
  },
  data() {
    return {
      isActive: false
    }
  },
  methods: {
    toggleActive() {
      this.isActive = !this.isActive;
      this.$emit('button-clicked', this.isActive);
    },
    checkAnswer() {
      if (!this.isActive) {
        this.$emit('check', false);
        return;
      }
      this.$emit('check', true);
    }
  }
}
</script>

<style scoped>

.duolingo-btn {
  background-color: #ffffff !important;
  border: 2px solid #e5e5e5 !important;
  border-bottom: 6px solid #e5e5e5 !important;
  border-radius: 16px !important;
  text-transform: none !important;
  transition: all 0.2s ease;
  position: relative;
  padding: 0 !important;
}

.duolingo-btn-active {
  background-color: #ddf4ff !important;
  border: 2px solid #84d8ff !important;
  border-bottom: 6px solid #84d8ff !important;
}

.duolingo-btn:active {
  transform: translateY(4px);
  border-bottom-width: 2px !important;
}

.btn-choice {
  min-width: 30px;
  height: 30px;
  border: 2px solid #e5e5e5;
  color: #afafaf;
  border-radius: 8px;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: all 0.2s ease;
}

.btn-choice-active {
  border-color: #84d8ff;
  color: #1899d6;
}

.btn-text {
  flex-grow: 1;
  text-align: center;
  font-size: 19px;
  color: #4b4b4b;
  letter-spacing: 0.5px;
  transition: all 0.2s ease;
}

.btn-text-active {
  color: #1899d6;
}

.button-19 {
  border-radius: 16px;
  letter-spacing: 1.5px;
  position: relative;
  overflow: hidden;
}

.button-19:active {
  transform: translateY(4px);
  border-bottom-width: 2px !important;
}
</style>