<template>
  <BaseLayout>
  
  </BaseLayout>
</template>

<script>
export default {
  name: 'MyComponent',
  data() {
    return {
      message: 'Hello, Vue!'
    };
  },
  methods: {
    sayHello() {
      console.log(this.message);
    }
  }
};
</script>