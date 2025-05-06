<template>
  <v-container class="fill-height">
    <v-row justify="center" align="center">
      <v-col cols="12" sm="8" md="6" lg="6">
        <v-card flat >
          <v-card-text>
            <v-row align="center" justify="space-between" class="my-2">
              <v-col cols="auto">
                <v-btn
                  link
                  :to="{ name: 'home' }"
                  color="transparent"
                  class="no-hover"
                  icon
                  size="small"
                  :ripple="false"
                >
                  <v-icon><IconClose /></v-icon>
                </v-btn>
              </v-col>

              <v-col>
                <v-slider
                  v-model="slider1"
                  color="primary"
                  disabled
                  hide-details
                  class="custom-thick-slider no-thumb"
                  track-size="12"
                  thumb-size="0"
                  thumb-label="always"
                ></v-slider>
              </v-col>

              <v-col cols="auto" class="d-flex align-center">
                <IconHeart />
                <div class="ml-3 text-subtitle-1 font-weight-bold" color="danger">5</div>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      slider1: 50,
    };
  },
};
</script>

<style scoped>
/* Slider kalınlığını değiştirmek için daha spesifik seçiciler */
:deep(.custom-thick-slider .v-slider-track__background),
:deep(.custom-thick-slider .v-slider-track__fill) {
  height: 16px !important;
}

/* Slider'ın ucundaki noktayı (thumb) gizlemek için */
:deep(.no-thumb .v-slider-thumb) {
  display: none !important;
}

/* Slider thumb label'ı da gizle (eğer görünüyorsa) */
:deep(.no-thumb .v-slider-thumb__label) {
  display: none !important;
}

/* Tüm fontları değiştirmek için */
:deep(*) {
  font-family: "DIN Next Rounded LT Pro Medium", sans-serif;
}

/* Slider arka plan rengini özelleştirmek için */
:deep(.v-slider-track__background) {
  background-color: rgba(var(--v-theme-surface-variant), 0.8) !important;
}

:deep(.v-slider-track__fill) {
  background-color: rgb(var(--v-theme-primary)) !important;
}

/* Slider'a yuvarlak köşeler ekle */
:deep(.custom-thick-slider .v-slider-track__background),
:deep(.custom-thick-slider .v-slider-track__fill) {
  border-radius: 10px !important;
}
</style>
