<template>
  <div class="container">

    <div class="row">

        <table id="tb-veg" class="uk-table uk-table-divider">
          <thead>
            <th> <span>Salad Name </span> </th>
            <th> <span>Category </span> </th>
            <th> <span>Price </span> </th>
          </thead>
            <tbody >
              <tr v-for="salad in salads">
                <td><span>{{salad.name}}</span></td>
                <td><span class="uk-label" v-bind:class="setCategory(salad.category)">{{salad.category}}</span></td>
                <td><span>{{salad.price }}</span></td>
                <td><button class="uk-button uk-button-secondary" href="#modal-center" uk-toggle v-on:click="setData(salad.name,salad.price,salad.id)">Add to Cart</button></td>
                <td></td>
              </tr>
            </tbody>
        </table>

        <!-- Quantity Modal -->
        <div id="modal-center" class="uk-flex-top" uk-modal>
          <div class="uk-modal-dialog uk-modal-body uk-margin-auto-vertical">

            <button class="uk-modal-close-default" type="button" uk-close></button>
            <div id="modal">
              <p>Select the quantity you wish to order<p/>
              <input v-model="quantity" type="number" value = "1" min="1" max="10"/>
              <br><br>
              <button class="uk-button uk-button-secondary uk-modal-close" v-on:click="addToCart()">Add to Cart</button>
            </div>
          </div>
        </div>

    </div>

  </div>
</template>

<script>
export default {
  name: 'Salads',
  //JQuery Code is used using mounted after installing jquery by cmd :" npm install jquery --save"
  mounted(){

    $('#category').on('load', function(){
      if(($this).text==='veg')
      ($this).addClass('veg')
    });
  },
  data(){
    return {
      quantity:1
    }
  },
  methods:{
    incrementQ(){
      this.quantity = this.quantity+1
    },
    decrementQ(){
      if(this.quantity===1)
      return

      this.quantity= this.quantity-1
    },
    setCategory(category){
      if(category==='veg')
      return 'veg-label'
      else
      return 'nonveg-label'
    },
    setData(name,price,id){
      this.$store.state.item.name=name;
      this.$store.state.item.price=price;
      this.$store.state.item.id=id;
      this.$store.state.item.quantity=1;
      this.quantity=1;
    },
    addToCart(){
      this.$store.state.item.quantity=this.quantity
      this.quantity=1
      this.$store.state.item.price*=this.$store.state.item.quantity


      UIkit.notification({
      message: this.$store.state.item.quantity + " " + this.$store.state.item.name + " added to cart",
      status: 'primary',
      pos: 'top-right',
      timeout: 3000
      })

      let obj = this.$store.state.item
      let cart = this.$store.state.cart

      for(var i=0;i<cart.length;i++){
        if(cart[i].id===obj.id){
          cart[i].quantity+=obj.quantity
          return
        }
      }
      console.log("adding item",this.$store.state.cart)
      this.$store.state.cart.push(this.$store.state.item)

      this.$store.state.item={}
      }
  },
  computed:{
    salads(){
      return this.$store.getters.getSalads
    }
  }
}
</script>

<style scoped>

.veg-label{
  background-color: green;
  color:honeydew;
}

.nonveg-label{
  background-color:brown;
  color:honeydew;
}

tr:hover{
  background-color:dodgerblue;
  color: white;
}
tr{  text-align: left; }

.selectedItem{
  background-color:dodgerblue;
  color: white
}

img{
  height:25px;
  width:25px;
}

#modal{
  text-align: center;
}
</style>

