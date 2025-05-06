<template>
<v-app>
    <div>
      <LessonSlider></LessonSlider>
    </div>
    <v-main>
      <slot></slot>
    </v-main>
    <LessonBottom></LessonBottom>
  </v-app>
</template>

<script>
export default {
  name: 'LessonSkeleton',
  data() {
    return {

    };
  },
  methods: {

  }
};
</script>


