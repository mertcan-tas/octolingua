<template>
  <v-layout class="overflow-visible" style="height: 88px">
    <v-bottom-navigation v-model="value" color="teal" grow elevation="3">
      <v-btn>
        <IconLearn/>
      </v-btn>
      <v-btn>
        <IconVoice/>
      </v-btn>
      <v-btn>
        <IconScoreboard/>
      </v-btn>
      <v-btn>
        <IconTasks/>
      </v-btn>
      <v-btn>
        <IconStore/>
      </v-btn>
      <v-btn>
        <IconProfile/>
      </v-btn>
    </v-bottom-navigation>
  </v-layout>
</template>
