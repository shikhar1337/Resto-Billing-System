<template>
  <div id="welcome">

    <br><br><br><br><br><br>
    RESTAURANT BILLING SYSTEM
    <br><br><br>
    <button class="uk-button uk-button-default" v-on:click="goToLogin()">Login</button>
    <!--<button class="uk-button uk-button-default" v-on:click="goToRegistration()">Registration</button>-->
    </div>
</template>

<style scoped>
button:hover{
  border-color: lightcoral;
}
</style>

<script>

export default {
  name: 'Welcome',
  methods:{
    goToLogin(){
      this.$router.push({path:'/login'})
    },
    goToRegistration(){
      this.$router.push({path:'/register'})
    }
  }
}
</script>


