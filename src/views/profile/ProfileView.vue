<template>
  <BaseLayout>
    {{ message }}
  </BaseLayout>
</template>

<script>
export default {
  data() {
    return {
      message: "Hello, Vue!",
    };
  },
  methods: {
    sayHello() {
      console.log(this.message);
    },
  },
};
</script>
