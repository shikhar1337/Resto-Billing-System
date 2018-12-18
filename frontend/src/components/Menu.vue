<template>
  <div>
    <Nav></Nav>
     <br><br>
    <router-link to="/menu/burgers"><button class="uk-button uk-button-default button hvr-fade">Burgers</button></router-link>
    <router-link to="/menu/shakes"><button class="uk-button uk-button-default button hvr-fade">Shakes</button></router-link>
    <router-link to="/menu/salads"><button class="uk-button uk-button-default button hvr-fade">Salads</button></router-link>
    <router-link to="/menu/pastas"><button class="uk-button uk-button-default button hvr-fade">Pastas</button></router-link>
    <router-link to="/menu/beverages"><button class="uk-button uk-button-default button hvr-fade">Beverages</button></router-link>

    <div id="submenu">
      <router-view></router-view>
    </div>

  </div>
</template>

<script>

import Nav from './Nav'

export default {
  name: 'Menu',
  components:{
    "Nav":Nav
  },
  beforeCreate(){
    this.$store.dispatch('getBurgersData')
    this.$store.dispatch('getShakesData')
    this.$store.dispatch('getSaladsData')
    this.$store.dispatch('getPastasData')
    this.$store.dispatch('getBeveragesData')
  }
}
</script>

<style scoped>

</style>

