<template>
  <div>
    <h1>Home Page</h1>
    <div class="router-class">
      <router-link to="/HelloWorld">HTML Basics</router-link>
      <router-link to="/CSSLayout">CSS Layout</router-link>
      <router-link to="/FlexBox">Flexbox</router-link>
      <router-link to="/Natours">Natours</router-link>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    goToHome() {
      this.$router.push({ name: "Home" });
    },
    goToHelloWorld() {
      this.$router.push({ name: "HelloWorld" });
    },
  },
};
</script>
<style scoped>
.router-class {
  display: flex;
  gap: 10px;
}
</style>
