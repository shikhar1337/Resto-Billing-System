<template>
  <div id="login" class="row">
    <nav class="uk-navbar-container uk-navbar-transparent" uk-navbar>
      <div class="uk-navbar-center">
        <router-link to="/"><img uk-tooltip="title: Home Screen ; pos: bottom " src="../assets/home.png" height="85" width="85"></router-link>
        &nbsp;
        <!--
        <router-link to="/register"><img uk-tooltip="title: Registration ; pos: bottom " src="../assets/reg.png" height="85" width="85"></router-link>
        -->
      </div>
    </nav>

    <br><br><br>
    <b>LOGIN</b>

    <table class="uk-table uk-table-middle">
      <tr>
        <td class="uk-width-1-4"></td>
        <td class="uk-table-shrink">  <span>Email</span></td>
        <td class="uk-table-shrink">  <input v-model="email" v-on:keyup="email_chkf()" type="text"/>  </td>
        <td><img v-if="email_chk" src="../assets/wrong.png" uk-tooltip="title: Invalid Email Address Type ; pos: right" height="25" width="25"/> </td>
      </tr>
      <tr>
        <td class="uk-width-1-4"></td>
        <td class="uk-table-shrink"> <span>Password</span> </td>
        <td class="uk-table-shrink"> <input v-model="password" v-on:keyup="password_chkf()" type="password"/> </td>
        <td> <img v-if="password_chk" src="../assets/wrong.png" uk-tooltip="title: Password Length should be between 6-12 characters & No white space is allowed  ; pos: right" height="25" width="25"/>  </td>
      </tr>
    </table>

    <button class="uk-button uk-button-secondary" v-on:click="doLogin()">LOGIN</button>

    <div id="failedLogin" uk-modal>
      <div class="uk-modal-dialog uk-modal-body">
        <button class="uk-modal-close-default" type="button" uk-close></button>
        <h2 class="uk-modal-title">Login Failure</h2>
        <p>Password is incorrect or the account doesn't exists</p>
      </div>
    </div>

    <div id="corrections" uk-modal>
      <div class="uk-modal-dialog uk-modal-body">
        <button class="uk-modal-close-default" type="button" uk-close></button>
        <h2 class="uk-modal-title">Correction</h2>
        <p>There are some corrections to be made</p>
      </div>
    </div>

  </div>
</template>

<style scoped>
#tablediv{
  text-align: right;
}
tr{
  text-align: right;
}
</style>

<script>
export default {
  name: 'Login',
  data(){
    return {
      email:'',
      password:'',
      email_chk:1,
      password_chk:1
    }
  },
  methods:{
    async doLogin(){
      if(this.email_chk || this.password_chk){
        UIkit.modal('#corrections').show()
        return
      }

      let result = await this.$store.dispatch('login',{email:this.email,password:this.password})
      if(result!=0){
        this.$router.push({path:'/menu/burgers'})
        this.$store.state.loggedCustomerID=result
        console.log(result)
      } else {
        // drop modal saying login failed
        UIkit.modal('#failedLogin').show()
        this.email=''
        this.password=''
      }
    },
    email_chkf(){
      var re = /^(?:[a-z0-9!#$%&amp;'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&amp;'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])$/;
      if(re.test(this.email)){
        this.email_chk=0
      }else{
        this.email_chk=1
      }
    },
    password_chkf(){
      if(this.password.length>5 && this.password.length<13 && !(/^\s+$/).test(this.password)){
        this.password_chk=0
      }else{
        this.password_chk=1
      }
    }
  }
}

/*
(result)=>{
          if(result){
            console.log("result= ",result)

          } else {
            // drop modal saying login failed
          }
        }
        */
</script>


