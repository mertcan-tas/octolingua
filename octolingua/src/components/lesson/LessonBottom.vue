<template>
  <v-footer app height="140" color="primary">
    <v-container>
      <v-row justify="space-between" align="center">
        <v-col cols="12" sm="8" md="6" lg="6">
          <v-row align="center" justify="center" dense>
            <v-col cols="auto">
              <v-avatar color="white" size="80">
                <IconTrue />
              </v-avatar>
            </v-col>
            <v-col cols="auto ml-3" justify="space-around">
              <p class="text-white font-weight-bold text-h6">Aferin!</p>
              <v-btn color="transparent" size="small" :ripple="false" class="text-capitalize" >
                <template v-slot:prepend>
                  <IconFlag/>
                </template>
                Bildir
              </v-btn>
            </v-col>
          </v-row>
        </v-col>

        <v-col cols="12" sm="8" md="6" lg="6">
          <v-row align="center" justify="center" dense>
            <v-col cols="auto">
              <v-btn color="secondary" variant="outlined"> Button </v-btn>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </v-footer>
</template>
