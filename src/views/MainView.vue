<template>
  <BaseLayout>

    <div class="container">
 
    <div class="header">
      <div class="stats">
        <span>Kalan Can: {{ lives }}</span>
      </div>
    </div>

    <div v-if="gameActive" class="card">
      <div v-if="currentMode === 'quiz' && currentWord" class="quiz-container">
        <h2>Bu kelimenin anlamını seçin:</h2>
        <div class="question">{{ currentWord.question }}</div>
        
        <div class="options">
          <button
            v-for="(option, index) in currentWord.options" 
            :key="index"
            @click="checkAnswer(option)"
            :class="{'option-button': true}"
          >
            {{ option }}
          </button>
        </div>
      </div>
      
      <div v-else-if="currentMode === 'quiz' && !currentWord" class="loading">
        <p>Kelimeler yükleniyor...</p>
      </div>

      <div v-else-if="currentMode === 'result' && currentWord" class="result-container">
        <div :class="['result', lastAnswerCorrect ? 'correct' : 'wrong']">
          <h2 v-if="lastAnswerCorrect">Doğru!</h2>
          <h2 v-else>Yanlış!</h2>
          <p>
            <strong>{{ currentWord.english }}</strong> = 
            <strong>{{ currentWord.turkish }}</strong>
          </p>
          <button @click="nextQuestion" class="continue-button">Devam Et</button>
        </div>
      </div>
    </div>

    <div v-else class="game-over">
      <h2>Oyun Bitti!</h2>
      <p>Puanınız: {{ score }}</p>
      <button @click="restartGame" class="restart-button">Yeniden Başla</button>
    </div>
  </div>


  </BaseLayout>
</template>
  
<script>


export default {
  data() {
    return {
      words: [],
      currentWord: null,
      currentMode: 'quiz',
      score: 0,
      lives: 3,
      gameActive: true,
      lastAnswerCorrect: false,
      answeredQuestions: []
    }
  },
  mounted() {
    fetch('english_turkish_words.md')
      .then(response => {
        if (!response.ok) {
          throw new Error('Kelime dosyası bulunamadı. HTTP durum: ' + response.status);
        }
        return response.text();
      })
      .then(data => {
        this.words = this.parseMarkdown(data);
        console.log('Kelimeler yüklendi:', this.words.length);
        if (this.words.length > 0) {
          this.startGame();
        } else {
          console.error('Kelime listesi boş.');
        }
      })
      .catch(error => {
        console.error('Kelime listesi yüklenemedi:', error);
        alert('Kelime listesi yüklenemedi: ' + error.message);
      });
  },
  methods: {
    parseMarkdown(mdText) {
      const lines = mdText.split('\n');
      const wordPairs = [];
      
      for (let i = 3; i < lines.length; i++) {
        const line = lines[i].trim();
        if (line.startsWith('|') && line.endsWith('|')) {
          const parts = line.split('|').filter(part => part.trim() !== '');
          if (parts.length >= 2) {
            const english = parts[0].trim();
            const turkish = parts[1].trim();
            if (english && turkish) {
              wordPairs.push({ english, turkish });
            }
          }
        }
      }
      return wordPairs;
    },
    
    startGame() {
      this.score = 0;
      this.lives = 3;
      this.gameActive = true;
      this.answeredQuestions = [];
      this.generateQuestion();
    },
    
    restartGame() {
      this.startGame();
    },
    
    generateQuestion() {
      try {
        this.currentMode = 'quiz';
        
        // Kelimeler henüz yüklenmemişse bekleyelim
        if (!this.words || this.words.length === 0) {
          console.warn('Kelimeler henüz yüklenmedi.');
          return;
        }
        
        // Henüz sorulmamış kelimeleri filtreleyelim
        const availableWords = this.words.filter(word => 
          !this.answeredQuestions.includes(word.english)
        );
        
        // Tüm kelimeler sorulduysa listeyi sıfırlayalım
        if (availableWords.length === 0) {
          this.answeredQuestions = [];
          return this.generateQuestion();
        }
        
        // Rastgele bir kelime seçelim
        const randomIndex = Math.floor(Math.random() * availableWords.length);
        const selectedWord = availableWords[randomIndex];
      
      // Rastgele soru tipi belirleyelim (İngilizce->Türkçe veya Türkçe->İngilizce)
      const questionType = Math.random() > 0.5 ? 'en_to_tr' : 'tr_to_en';
      
      // Seçenekleri oluşturalım (3 yanlış, 1 doğru)
      let options = [];
      let correctAnswer = '';
      
      if (questionType === 'en_to_tr') {
        // İngilizce -> Türkçe sorusu
        correctAnswer = selectedWord.turkish;
        const question = selectedWord.english;
        
        // 3 farklı yanlış cevap ekleyelim
        options = this.getRandomOptions(this.words, 'turkish', correctAnswer, 3);
        options.push(correctAnswer);
        
        // Seçenekleri karıştıralım
        this.shuffleArray(options);
        
        this.currentWord = {
          english: selectedWord.english,
          turkish: selectedWord.turkish,
          question: question,
          correctAnswer: correctAnswer,
          options: options
        };
      } else {
        // Türkçe -> İngilizce sorusu
        correctAnswer = selectedWord.english;
        const question = selectedWord.turkish;
        
        // 3 farklı yanlış cevap ekleyelim
        options = this.getRandomOptions(this.words, 'english', correctAnswer, 3);
        options.push(correctAnswer);
        
        // Seçenekleri karıştıralım
        this.shuffleArray(options);
        
        this.currentWord = {
          english: selectedWord.english,
          turkish: selectedWord.turkish,
          question: question,
          correctAnswer: correctAnswer,
          options: options
        };
      }
      
      this.answeredQuestions.push(selectedWord.english);
      } catch (error) {
        console.error('Soru oluşturulurken hata oluştu:', error);
        this.currentWord = null;
      }
    },
    
    getRandomOptions(wordList, field, correctAnswer, count) {
      const options = [];
      const usedIndices = new Set();
      
      while (options.length < count) {
        const randomIndex = Math.floor(Math.random() * wordList.length);
        const randomWord = wordList[randomIndex][field];
        

        if (randomWord !== correctAnswer && !options.includes(randomWord) && !usedIndices.has(randomIndex)) {
          options.push(randomWord);
          usedIndices.add(randomIndex);
        }
      }
      
      return options;
    },
    
    shuffleArray(array) {
      for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
      }
      return array;
    },
    
    checkAnswer(selectedAnswer) {
      const isCorrect = selectedAnswer === this.currentWord.correctAnswer;
      
      this.lastAnswerCorrect = isCorrect;
      this.currentMode = 'result';
      
      if (isCorrect) {
        this.score += 10;
      } else {
        this.lives -= 1;
        if (this.lives <= 0) {
          this.gameActive = false;
        }
      }
    },
    
    nextQuestion() {
      if (this.gameActive) {
        this.generateQuestion();
      }
    }
  }
}
</script>






<style>
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Arial', sans-serif;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

.stats {
  display: flex;
  gap: 20px;
}

.card {
  background-color: #fff;
  border-radius: 10px;
  padding: 30px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-bottom: 30px;
}

.quiz-container {
  text-align: center;
}

.question {
  font-size: 24px;
  font-weight: bold;
  margin: 20px 0;
  padding: 15px;
  background-color: #f8f9fa;
  border-radius: 5px;
}

.options {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 15px;
  margin-top: 20px;
}

.option-button {
  padding: 15px;
  border: 2px solid #ddd;
  border-radius: 5px;
  background-color: white;
  cursor: pointer;
  font-size: 16px;
  transition: all 0.2s;
}

.option-button:hover {
  background-color: #f1f1f1;
  border-color: #aaa;
}

.result-container {
  text-align: center;
}

.result {
  padding: 20px;
  border-radius: 5px;
}

.correct {
  background-color: #d4edda;
  color: #155724;
}

.wrong {
  background-color: #f8d7da;
  color: #721c24;
}

.continue-button, .restart-button {
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
  margin-top: 20px;
}

.continue-button:hover, .restart-button:hover {
  background-color: #45a049;
}

.game-over {
  text-align: center;
  padding: 30px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
</style>