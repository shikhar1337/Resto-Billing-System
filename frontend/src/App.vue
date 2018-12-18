<template>
  <div id="app" class="container">
    <router-view></router-view>
    </div>
</template>

<script>

export default {
  name: 'App'
}
</script>

<style>
body{
  font-family: 'Trebuchet MS';
}
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  font-size: 20px;
}
</style>
