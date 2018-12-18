<template>
  <div id="user">
    <Nav></Nav>
    <br>

    <div id="wrongDates" uk-modal>
      <div class="uk-modal-dialog uk-modal-body">
        <button class="uk-modal-close-default" type="button" uk-close></button>
        <h2 class="uk-modal-title">Invalid Dates</h2>
        <p>Both StartDate & EndDate cannot be empty</p>
      </div>
    </div>

    <p>  Admin Functions </p> <br/> <br/>
    <button class="uk-button uk-button-default" v-on:click="addItemsToggle()">Add Items</button>
    <button class="uk-button uk-button-default" v-on:click="billsToggle()">View Sales History</button>

    <div v-if="show_bills">
      <br>
      Start Date : &nbsp;&nbsp; <input type="date" v-model="startDate"/>  <br>
      End Date : &nbsp;&nbsp;&nbsp;&nbsp; <input type="date" v-model="endDate"/>  <br>
      <button class="uk-button uk-button-default" v-on:click="processTable()">GO</button> <br>

      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

    <div v-if="view_table" class="uk-overflow-auto">
      <table class="uk-table">
        <thead>
          <tr>
            <th>Bill ID</th>
            <th>Date</th>
            <th>Bill Amount</th>

          </tr>
        </thead>
        <tbody>
          <tr v-for="obj in tableData">
            <td>{{obj.id}}</td>
            <td>{{obj.date}}</td>
            <td>{{obj.price}}</td>

          </tr>
        </tbody>
      </table>

    </div>
    <br>
    <span v-if="view_table"> Total Earnings for this time period : {{totalEarnings}} </span>
    <br><br><br><br><br>
    </div>

    <div v-if="show_addItems">
    <br>
    <button class="uk-button uk-button-default" v-on:click="tBurger()">Add Burger</button>
    <button class="uk-button uk-button-default" v-on:click="tShake()">Add Shake</button>
    <button class="uk-button uk-button-default" v-on:click="tSalad()">Add Salad</button>
    <button class="uk-button uk-button-default" v-on:click="tPasta()">Add Pasta</button>
    <button class="uk-button uk-button-default" v-on:click="tBeverage()">Add Beverage</button>

    <div id="addBurger" v-if="show_burger">
      <br> <br>
      Name : &nbsp;&nbsp; &nbsp; &nbsp;&nbsp;   <input v-model="burger.name" type="text"> <br>
      Category : &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      <select v-model="burger.category">
      <option disabled value="">Select Category</option>
      <option>veg</option>
      <option>nonveg</option>
      </select>
      <br>
      Price : &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      <input v-model="burger.price" type="text">
      <br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      <button class="uk-button uk-button-default" v-on:click="addBurger()">Add Burger</button>
    </div>

    <div id="addShake" v-if="show_shake">
      <br> <br>
      Name : &nbsp; &nbsp; &nbsp;&nbsp; <input v-model="shake.name" type="text"> <br>
      Price : &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      <input v-model="shake.price" type="text">
      <br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      <button class="uk-button uk-button-default" v-on:click="addShake()">Add Shake</button>
    </div>

    <div id="addSalad" v-if="show_salad">
      <br> <br>
      Name : &nbsp;&nbsp; &nbsp; &nbsp;&nbsp;   <input v-model="salad.name" type="text"> <br>
      Category : &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      <select v-model="salad.category">
      <option disabled value="">Select Category</option>
      <option>veg</option>
      <option>nonveg</option>
      </select>
      <br>
      Price : &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      <input v-model="salad.price" type="text">
      <br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      <button class="uk-button uk-button-default" v-on:click="addSalad()">Add Salad</button>
    </div>

    <div id="addPasta" v-if="show_pasta">
      <br> <br>
      Name : &nbsp;&nbsp; &nbsp; &nbsp;&nbsp;   <input v-model="pasta.name" type="text"> <br>
      Category : &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      <select v-model="pasta.category">
      <option disabled value="">Select Category</option>
      <option>veg</option>
      <option>nonveg</option>
      </select>
      <br>
      Price : &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      <input v-model="pasta.price" type="text">
      <br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      <button class="uk-button uk-button-default" v-on:click="addPasta()">Add Pasta</button>
    </div>

    <div id="addBeverage" v-if="show_beverage">
      <br> <br>
      Name : &nbsp; &nbsp; &nbsp;&nbsp; <input v-model="beverage.name" type="text"> <br>
      Price : &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      <input v-model="beverage.price" type="text">
      <br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      <button class="uk-button uk-button-default" v-on:click="addBeverage()">Add Beverage</button>
    </div>
    </div>

  </div>
</template>

<script>

import Nav from './Nav'

export default {
  name: 'User',
  components:{
    "Nav":Nav
  },
  created(){
    this.tableData=[],
    this.totalEarnings = 0
  },
  data(){
    return{
      tableData:[],
      totalEarnings:0,
      view_table:0,
      show_addItems:0,
      startDate:'',
      endDate:'',
      show_bills:0,
      show_burger:0,
      show_shake:0,
      show_salad:0,
      show_pasta:0,
      show_beverage:0,
      toggle:0,
      burger:{},
      shake:{},
      salad:{},
      pasta:{},
      beverage:{}
    }
  },
  methods:{
    async processTable(){
      this.tableData=[]
      this.totalEarnings=0

      if(this.startDate=='' && this.endDate==''){
        UIkit.modal('#wrongDates').show()
        return
      }

      let result = await this.$store.dispatch('getSalesData',{startDate:this.startDate,endDate:this.endDate})
      let obj = {'id':0,'date':'','price':0}
      for(let i = 1;i<result.id.length;i++){
        obj.id = result.id[i]
        obj.date = result.date[1]
        obj.price = parseFloat(result.price[i])
        this.totalEarnings+=obj.price
        this.tableData.push(obj)
        obj = {'id':0,'date':'','price':0}
      }
      this.view_table=1
    },
    addItemsToggle(){
      this.view_table=0

      if(this.show_addItems==0){
        this.show_addItems=1
        this.show_bills=0
      } else if(this.show_addItems==1){
        this.show_addItems=0
        this.setAlltoZero()
      }
    },
    billsToggle(){
      if(this.show_bills==0){
        this.show_bills=1
        this.show_addItems=0
      } else if(this.show_bills==1){
        this.show_bills=0
      }
      this.setAlltoZero()
    },
    async addBurger(){
      this.burger.price=parseFloat(this.burger.price)
      let result = await this.$store.dispatch('addBurger',this.burger)

      if(result){
        UIkit.notification({
        message: this.burger.name+' added to the Burger Menu',
        status: 'primary',
        pos: 'top-right',
        timeout: 3000
      })
      }

      this.burger={}
    },
    async addShake(){
      this.shake.price=parseFloat(this.shake.price)
      let result = await this.$store.dispatch('addShake',this.shake)

      if(result){
        UIkit.notification({
        message: this.shake.name+' added to the Shake Menu',
        status: 'primary',
        pos: 'top-right',
        timeout: 3000
      })
      }

      this.shake={}
    },
    async addBeverage(){
      this.beverage.price=parseFloat(this.beverage.price)
      let result = await this.$store.dispatch('addBeverage',this.beverage)

      if(result){
        UIkit.notification({
        message: this.beverage.name+' added to the Beverage Menu',
        status: 'primary',
        pos: 'top-right',
        timeout: 3000
      })
      }

      this.beverage={}
    },
    async addSalad(){
      this.salad.price=parseFloat(this.salad.price)
      let result = await this.$store.dispatch('addSalad',this.salad)

      if(result){
        UIkit.notification({
        message: this.salad.name+' added to the Salad Menu',
        status: 'primary',
        pos: 'top-right',
        timeout: 3000
      })
      }

      this.salad={}
    },
    async addPasta(){
      this.pasta.price=parseFloat(this.pasta.price)
      let result = await this.$store.dispatch('addPasta',this.pasta)

      if(result){
        UIkit.notification({
        message: this.pasta.name+' added to the Pasta Menu',
        status: 'primary',
        pos: 'top-right',
        timeout: 3000
      })
      }

      this.pasta={}
    },
    setAlltoZero(){
      this.show_burger=0
      this.show_shake=0
      this.show_salad=0
      this.show_pasta=0
      this.show_beverage=0
    },
    tBurger(){
      //if((this.show_burger||this.show_shake||this.show_salad||this.show_pasta||this.show_beverage)
      if(this.show_shake||this.show_salad||this.show_pasta||this.show_beverage)
      this.setAlltoZero()

      if(this.show_burger==1){
        this.show_burger = 0
      } else if(this.show_burger == 0){
        this.show_burger = 1
      }
    },
    tShake(){
      if(this.show_burger||this.show_salad||this.show_pasta||this.show_beverage)
      this.setAlltoZero()

      if(this.show_shake==1){
        this.show_shake = 0
      } else if(this.show_shake == 0){
        this.show_shake = 1
      }
    },
    tSalad(){
      if(this.show_burger||this.show_shake||this.show_pasta||this.show_beverage)
      this.setAlltoZero()

      if(this.show_salad==1){
        this.show_salad = 0
      } else if(this.show_salad == 0){
        this.show_salad = 1
      }
    },
    tPasta(){
      if(this.show_burger||this.show_shake||this.show_salad||this.show_beverage)
      this.setAlltoZero()

      if(this.show_pasta==1){
        this.show_pasta = 0
      } else if(this.show_pasta == 0){
        this.show_pasta = 1
      }
    },
    tBeverage(){
      if(this.show_burger||this.show_shake||this.show_salad||this.show_pasta)
      this.setAlltoZero()

      if(this.show_beverage==1){
        this.show_beverage = 0
      } else if(this.show_beverage == 0){
        this.show_beverage = 1
      }
    }
  }
}

//
</script>

<style scoped>
button:hover{
  border-color: lightcoral;
}

.uk-overflow-auto{
  height: 500px;
}

</style>

