<template>
  <div id="nav">

    <nav class="uk-navbar-container uk-navbar-transparent" uk-navbar>

      <div class="uk-navbar-center">
        <router-link to="/menu/burgers"><img uk-tooltip="title: Menu ; pos: bottom " src="../assets/menu.png" height="85" width="85"></router-link>
        &nbsp;
        <router-link to="/cart"><img uk-tooltip="title: Cart ; pos: bottom " src="../assets/cart.png" height="85" width="85"></router-link>
        &nbsp;
        <router-link to="/user"><img uk-tooltip="title: Admin; pos: bottom " src="../assets/set.png" height="85" width="85"></router-link>
        &nbsp;
        <router-link to="/"><img uk-tooltip="title: Log Out; pos: bottom " src="../assets/exit.png" height="85" width="85"></router-link>
      </div>

    </nav>


  </div>
</template>

<style scoped>

</style>

<script>
export default {
  name: 'Nav'
}
</script>


