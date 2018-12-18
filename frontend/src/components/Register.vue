<template>
  <div id="login">

    <nav class="uk-navbar-container uk-navbar-transparent" uk-navbar>
      <div class="uk-navbar-center">
        <router-link to="/"><img uk-tooltip="title: Home Screen ; pos: bottom " src="../assets/home.png" height="85" width="85"></router-link>
        &nbsp;
        <router-link to="/login"><img uk-tooltip="title: Login ; pos: bottom " src="../assets/login.png" height="85" width="85"></router-link>
      </div>
    </nav>


    <br><br><br>
    <b>REGISTRATION</b>

    <table class="uk-table uk-table-middle">
      <tr>
        <td class="uk-width-1-4"></td>
        <td class="uk-table-shrink">  <span>Name</span></td>
        <td class="uk-table-shrink">  <input v-model="name" v-on:keyup="name_chkf()" type="text"/>  </td>
        <td><img v-if="name_chk" uk-tooltip="title: Name cannot be left blank & should be less than 30 characters  ; pos: right" src="../assets/wrong.png" height="25" width="25"/> </td>
      </tr>
      <tr>
        <td class="uk-width-1-4"></td>
        <td class="uk-table-shrink">  <span>Email</span></td>
        <td class="uk-table-shrink">  <input v-model="email" v-on:keyup="email_chkf()" type="text"/>  </td>
        <td><img v-if="email_chk" uk-tooltip="title: Invalid Email Address Type ; pos: right" src="../assets/wrong.png" height="25" width="25"/> </td>
      </tr>
      <tr>
        <td class="uk-width-1-4"></td>
        <td class="uk-table-shrink"> <span>Password</span> </td>
        <td class="uk-table-shrink"> <input v-model="password" v-on:keyup="password_chkf()" type="password"/> </td>
        <td> <img v-if="pass_chk" uk-tooltip="title: Password Length should be between 6-12 characters & No white space is allowed  ; pos: right" src="../assets/wrong.png" height="25" width="25"/>  </td>
      </tr>
      <tr>
        <td class="uk-width-1-4"></td>
        <td class="uk-table-shrink"> <span>Confirm Password</span> </td>
        <td class="uk-table-shrink"> <input v-model="cnf_password" v-on:keyup="password_chkf()" type="password"/> </td>
        <td> <img v-if="cnfpass_chk" uk-tooltip="title: Passwords should match ; pos: right" src="../assets/wrong.png" height="25" width="25"/>  </td>
      </tr>
      <tr>
        <td class="uk-width-1-4"></td>
        <td class="uk-table-shrink"> <span>Mobile Number</span> </td>
        <td class="uk-table-shrink"> <input v-model="mobile" v-on:keyup="mobile_chkf()" type="text"/> </td>
        <td> <img v-if="mobile_chk" uk-tooltip="title: Mobile number should contain exactly 10 digits ; pos: right" src="../assets/wrong.png" height="25" width="25"/>  </td>
      </tr>
      <tr>
        <td class="uk-width-1-4"></td>
        <td class="uk-table-shrink"> <span> Address</span> </td>
        <td class="uk-table-shrink"> <textarea v-model="address"></textarea> </td>
        <td></td>
      </tr>
    </table>

    <div id="corrections" uk-modal>
      <div class="uk-modal-dialog uk-modal-body">
        <button class="uk-modal-close-default" type="button" uk-close></button>
        <h2 class="uk-modal-title">Correction</h2>
        <p>There are some corrections to be made</p>
      </div>
    </div>

    <div id="regfailed" uk-modal>
      <div class="uk-modal-dialog uk-modal-body">
        <button class="uk-modal-close-default" type="button" uk-close></button>
        <h2 class="uk-modal-title">Registration failed</h2>
        <p>Registration Cannot be done. An account with this email address already exists.</p>
      </div>
    </div>

    <div id="regdone" uk-modal>
      <div class="uk-modal-dialog uk-modal-body">
        <button class="uk-modal-close-default" type="button" uk-close></button>
        <h2 class="uk-modal-title">Registration Successful</h2>
        <p>Please Log In using your new credentials</p>
      </div>
    </div>

    <button class="uk-button uk-button-secondary" v-on:click="doRegistration" >REGISTER</button>
  </div>
</template>

<style scoped>

</style>

<script>
export default {
  name: 'Register',
  data(){
    return{
      name:'',
      email:'',
      password:'',
      cnf_password:'',
      mobile:'',
      address:'',
      name_chk:1,
      email_chk:1,
      pass_chk:1,
      cnfpass_chk:1,
      mobile_chk:1
    }
  },
  methods:{
    async doRegistration(){
      if(this.name_chk || this.email_chk || this.pass_chk || this.cnfpass_chk || this.mobile_chk ){
        UIkit.modal('#corrections').show()
        return
      }

      let result = await this.$store.dispatch('register',{
        name:this.name,
        email:this.email,
        password:this.password,
        address:this.address
        })

        if(result == 1){
          this.$router.push({path:'/login'})
          UIkit.modal('#regdone').show()
        } else if(result == 2){
          UIkit.modal('#regfailed').show()
          this.email=''
        }
    },
    name_chkf(){
      if(this.name.length>0 && this.name.length<31 && !(/^\s*$/).test(this.name))
      this.name_chk=0
      else
      this.name_chk=1
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
      this.pass_chkf()
      this.cnfpass_chkf()
    },
    pass_chkf(){
      if(this.password.length>5 && this.password.length<13 && !(/^\s+$/).test(this.password)){
        this.pass_chk=0
      }else{
        this.pass_chk=1
      }
    },
    cnfpass_chkf(){
      if(this.password===this.cnf_password){
        this.cnfpass_chk=0
      }else{
        this.cnfpass_chk=1
      }
    },
    mobile_chkf(){
      if(this.mobile.length===10 && !(/^\s+$/).test(this.mobile) && (/^\d+$/).test(this.mobile) ){
        this.mobile_chk=0
      }else{
        this.mobile_chk=1
      }
    }
  }
}
</script>



