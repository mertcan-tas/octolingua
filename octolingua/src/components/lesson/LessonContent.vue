<template>
  <v-container class="fill-height">
    <v-row justify="center" align="center">
      <v-col cols="12" sm="8" md="6">
        <div class="filler text-center">
          <v-text class="text-h4">Duolingo Radio Button Design</v-text>
          <p class="desc text-subtitle-1">Interactive Duolingo radio buttons with keyboard navigation.</p>
        </div>
        
        <v-card flat class="mb-2" v-for="(option, index) in options" :key="index">
          <div 
            class="btn duolingo-btn d-flex align-center"
            :id="`btn-${index + 1}`" 
            @click="selectOption(index)"
            :style="getButtonStyle(index)"
          >
            <div 
              class="btn-choice mx-3"
              :id="`bc-${index + 1}`"
              :style="getChoiceStyle(index)"
            >{{ index + 1 }}</div>
            <div 
              class="btn-text text-center"
              :id="`bt-${index + 1}`"
              :style="getTextStyle(index)"
            >{{ option }}</div>
          </div>
        </v-card>
        
        <div class="mt-6">
          <v-btn 
            block 

            class="text-uppercase font-weight-bold button-19" 

            @click="checkAnswer"
            :disabled="selectedIndex === null"
          >
            Check
          </v-btn>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'DuolingoRadioButtons',
  data() {
    return {
      options: [
        '¡Tenemos que pagar la cuenta!',
        '¿Por qué no estás comiendo, Manuel?',
        'Disculpe señor, ¿dónde está el hotel más cercano?'
      ],
      selectedIndex: null,
      correctAnswer: 2, // Assuming the third option is correct (zero-based index)
    }
  },
  mounted() {
    window.focus();
    window.addEventListener('keypress', this.handleKeyPress);
  },
  beforeDestroy() {
    window.removeEventListener('keypress', this.handleKeyPress);
  },
  methods: {
    selectOption(index) {
      this.selectedIndex = index;
    },
    handleKeyPress(event) {
      const key = parseInt(event.key);
      if (key >= 1 && key <= this.options.length) {
        this.selectOption(key - 1);
      }
    },
    checkAnswer() {
      if (this.selectedIndex === null) {
        this.$vuetify.dialog.message.info('Please select an option first!');
        return;
      }
      
      if (this.selectedIndex === this.correctAnswer) {
        this.$vuetify.dialog.message.success('Correct!');
      } else {
        this.$vuetify.dialog.message.error('Incorrect. Try again!');
      }
    },
    getButtonStyle(index) {
      if (this.selectedIndex === index) {
        return {
          borderColor: '#84d8ff',
          backgroundColor: '#ddf4ff',
          borderBottom: '6px solid #84d8ff'
        };
      }
      return {
        borderColor: '#e5e5e5',
        backgroundColor: '#ffffff',
        borderBottom: '6px solid #e5e5e5'
      };
    },
    getChoiceStyle(index) {
      if (this.selectedIndex === index) {
        return {
          borderColor: '#84d8ff',
          color: '#1899d6'
        };
      }
      return {
        borderColor: '#e5e5e5',
        color: '#afafaf'
      };
    },
    getTextStyle(index) {
      if (this.selectedIndex === index) {
        return {
          color: '#1899d6'
        };
      }
      return {
        color: '#4b4b4b'
      };
    }
  }
}
</script>

<style scoped>
@import url(https://db.onlinewebfonts.com/c/f83531ae85a3fcd9345c4267e28833ee?family=DIN+Next+Rounded+LT+Pro+Medium);

* {
  font-family: "DIN Next Rounded LT Pro Medium";
}

.duolingo-btn {
  width: 100%;
  height: 58px;
  font-size: 19px;
  border-radius: 16px;
  border: 2px solid #e5e5e5;
  border-bottom: 6px solid #e5e5e5;
  padding: 12px 3px;
  line-height: 1.4;
  cursor: pointer;
  user-select: none;
}

.duolingo-btn:active {
  border-bottom: 2px solid #e5e5e5;
  transform: translateY(4px);
}

.btn-choice {
  border: 2px solid #e5e5e5;
  color: #afafaf;
  border-radius: 8px;
  width: 30px;
  height: 30px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.btn-text {
  width: 100%;
  text-align: center;
  font-size: 19px;
  letter-spacing: 0.5px;
}

.filler {
  margin: 42px 0;
}

.filler .desc {
  color: #737373;
}

.button-19 {
  border-radius: 16px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
}

.button-19:active {
  transform: translateY(4px);
}
</style>