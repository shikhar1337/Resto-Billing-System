<template>
  <div class="container">

    <Nav></Nav>
    <br>

    <p>Cart</p>

    <div id="cart" v-if="this.$store.state.cart.length>0">
    <table id="" class="uk-table uk-table-divider">
      <thead>
        <th> <span>Item Name </span> </th>
        <th> <span>Quantity</span> </th>
        <th> <span>Price</span> </th>
      </thead>

      <tr v-for="item in cart">
        <td><span>{{item.name}}</span></td>
        <td><span>{{item.quantity}}</span></td>
        <td><span>{{item.price}}</span></td>
        <td><span><button class="uk-button uk-button-secondary" v-on:click="removeItem(item.id)">Remove</button></span></td>

      </tr>

    </table>

    <span>Cart Total : {{cartTotal}} </span><br>
    <span>GST : {{gst}} </span><br>
    <span>Final Total : {{finalTotal}} </span>
    <br><br>
    <button v-on:click="checkout()" class="uk-button uk-button-primary">CHECKOUT</button>
    </div>

  </div>
</template>

<script>
import Nav from './Nav'

export default{
  name: 'Cart',
  components:{
    "Nav":Nav
  },
  mounted(){
    this.setCartTotal()
    this.setFinalTotal()
  },
  data(){
    return {
      cart : this.$store.getters.getCart,
      gst:'5%',
      cartTotal:0,
      finalTotal:0
    }
  },
  watch: {
	      cart:()=> {
          console.log("cart changed") // watch not needed
	      }
  },
  methods:{
    removeItem(id){
      let cart = this.$store.state.cart;
      let index = 0;
      for(var i = 0 ; i < cart.length ; i++ ){
        if(cart[i].id===id){
          index = cart.indexOf(cart[i])
          console.log(index);
        }
      }
      // updating prices
      this.updatePrices(index)
      cart.splice(index,1)
    },
    setCartTotal(){
      for(var i=0;i<this.$store.state.cart.length;i++){
        this.cartTotal+=this.$store.state.cart[i].price
      }
    },
    setFinalTotal(){
      this.finalTotal=this.cartTotal+this.cartTotal*this.$store.state.gst_rate
    },
    updatePrices(itemIndex){
      this.cartTotal-=this.cart[itemIndex].price;
      this.setFinalTotal()
    },
    async checkout(){
      let result = await this.$store.dispatch('checkout')
      if(result!=0){
        this.$store.state.cart=[]
        this.$router.push({path:'/menu/burgers'})

        UIkit.notification({
        message: 'Bill ID '+result+' processed',
        status: 'primary',
        pos: 'top-right',
        timeout: 3000
        })
        window.print()
      }

    }
  },
  computed:{

  }
}

</script>


<style scoped>

</style>
