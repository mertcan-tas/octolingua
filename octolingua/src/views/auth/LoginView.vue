<template>
  <ClearLayout>
    <v-container >
      <v-row justify="center" align="center">
        <v-col cols="12" sm="10" md="6" lg="4">
          <div class="text-h5 font-weight-bold text-center mb-6">
            Profilini oluştur
          </div>
          
          <v-form @submit.prevent="submitForm" class="w-100">
            <v-text-field-primary
              v-model="formData.age"
              placeholder="Yaş"
              class="mb-4"
              clearable
              @click:clear="formData.age = ''"
            >
              <template v-slot:append-inner>
                <IconClear
                  v-if="formData.age"
                  @click="formData.age = ''"
                  style="cursor: pointer"
                />
              </template>
            </v-text-field-primary>

            <div class="mb-4 text-body-2">
              Yaşını sunman doğru Duolingo tecrübeni edinmeni sağlar. Daha fazla
              bilgi için lütfen
              <a href="/privacy">Gizlilik Politikası</a>'na göz at.
            </div>

            <v-text-field-primary
              v-model="formData.name"
              class="mb-4"
              placeholder="Ad (isteğe bağlı)"
            ></v-text-field-primary>

            <v-text-field-primary
              v-model="formData.email"
              class="mb-4"
              type="email"
              placeholder="E-posta"
            ></v-text-field-primary>

            <v-text-field-primary
              v-model="formData.password"
              :type="passwordVisible ? 'text' : 'password'"
              placeholder="Parola"
              class="mb-4"
            >
              <template v-slot:append-inner>
                <div class="icon-wrapper" @click="togglePasswordVisibility">
                  <IconEyeOn v-if="passwordVisible" />
                  <IconEyeOff v-else />
                </div>
              </template>
            </v-text-field-primary>

            <v-btn-primary color="primary" block class="w-100"> Hesap Aç </v-btn-primary>
          </v-form>
          
          <v-divider color="lightgrey" class="my-6 text-center border-opacity-75">
            <div class="text-uppercase px-2  font-weight-bold">Veya</div>
          </v-divider>
          
          <v-btn-primary block class="w-100"> Facebook </v-btn-primary>
        </v-col>
      </v-row>
    </v-container>
  </ClearLayout>
</template>

<script>
export default {
  data() {
    return {
      formData: {
        age: "",
        name: "",
        email: "",
        password: ""
      },
      passwordVisible: false,
    };
  },
  methods: {
    togglePasswordVisibility() {
      this.passwordVisible = !this.passwordVisible;
      
      // Buton tıklamasından sonra odaklanmayı kaldır
      if (document.activeElement) {
        document.activeElement.blur();
      }
    },
    submitForm() {
      // Form gönderme işlevi burada uygulanabilir
      console.log('Form gönderildi:', this.formData);
    }
  },
};
</script>

<style scoped>
.w-100 {
  width: 100%;
}

.icon-wrapper {
  cursor: pointer;
}
</style>