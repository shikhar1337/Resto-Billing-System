import Vue from 'vue'
import Vuex from 'vuex'
import Axios from 'axios'

Vue.use(Vuex);

export const store = new Vuex.Store({
  //strict:true,
  state:{
    burgers:[],
    shakes:[],
    salads:[],
    pastas:[],
    beverages:[],
    cart:[],
    item:{},
    gst_rate:0.05,
    loggedCustomerID:0
  },
  getters:{
    getBurgers:(state)=>{
      return state.burgers;
    },
    getShakes:(state)=>{
      return state.shakes;
    },
    getSalads:(state)=>{
      return state.salads;
    },
    getPastas:(state)=>{
      return state.pastas;
    },
    getBeverages:(state)=>{
      return state.beverages;
    },
    getCart:(state)=>{
      return state.cart;
    }

  },
  actions:{
    getBurgersData(context,payload){
      //payload is the argument if argument is sent
      //context.commit('mutation',payload) can also be done
      Axios.get('http://127.0.0.1:5000/burgers')
      .then(response=>{
        context.state.burgers = response.data.burgers
      }).catch(e=>{
        console.log(e)
      })
    },
    getShakesData(context,payload){
      //payload is the argument if argument is sent
      //context.commit('mutation',payload) can also be done
      Axios.get('http://127.0.0.1:5000/shakes')
      .then(response=>{
        context.state.shakes = response.data.shakes
      }).catch(e=>{
        console.log(e)
      })
    },
    getSaladsData(context,payload){
      //payload is the argument if argument is sent
      //context.commit('mutation',payload) can also be done
      Axios.get('http://127.0.0.1:5000/salads')
      .then(response=>{
        context.state.salads = response.data.salads
      }).catch(e=>{
        console.log(e)
      })
    },
    getPastasData(context,payload){
      //payload is the argument if argument is sent
      //context.commit('mutation',payload) can also be done
      Axios.get('http://127.0.0.1:5000/pastas')
      .then(response=>{
        context.state.pastas = response.data.pastas
      }).catch(e=>{
        console.log(e)
      })
    },
    async getPrevOrders(context,payload){
      let response = await Axios.get('http://127.0.0.1:5000/prevOrders',{params:{customerId:context.state.loggedCustomerID}})
      return response.data
    },
    async getOrder(context,payload){
      let response = await Axios.get('http://127.0.0.1:5000/getOrder',{params:{orderId:payload}})
      return response.data
    },
    async getSalesData(context,payload){
      let response = await Axios.get('http://127.0.0.1:5000/getSalesData',{params:{startDate:payload.startDate,endDate:payload.endDate}})
      return response.data
    },
    getBeveragesData(context,payload){
      //payload is the argument if argument is sent
      //context.commit('mutation',payload) can also be done
      Axios.get('http://127.0.0.1:5000/beverages')
      .then(response=>{
        context.state.beverages = response.data.beverages
      }).catch(e=>{
        console.log(e)
      })
    },
    async checkout(context,payload){
      var config = { headers: {'Content-Type': 'application/json' } }
      let response = await Axios.post('http://127.0.0.1:5000/bill',{ cart:context.state.cart,customerId:context.state.loggedCustomerID},config)
      return parseInt(response.data)
    },
    async addBurger(context,payload){
      var config = { headers: {'Content-Type': 'application/json' } }
      let response = await Axios.post('http://127.0.0.1:5000/addBurger',{ name:payload.name,category:payload.category,price:payload.price},config)
      return parseInt(response.data)
    },
    async addShake(context,payload){
      var config = { headers: {'Content-Type': 'application/json' } }
      let response = await Axios.post('http://127.0.0.1:5000/addShake',{ name:payload.name,price:payload.price},config)
      return parseInt(response.data)
    },
    async addBeverage(context,payload){
      var config = { headers: {'Content-Type': 'application/json' } }
      let response = await Axios.post('http://127.0.0.1:5000/addBeverage',{ name:payload.name,price:payload.price},config)
      return parseInt(response.data)
    },
    async addSalad(context,payload){
      var config = { headers: {'Content-Type': 'application/json' } }
      let response = await Axios.post('http://127.0.0.1:5000/addSalad',{ name:payload.name,category:payload.category,price:payload.price},config)
      return parseInt(response.data)
    },
    async addPasta(context,payload){
      var config = { headers: {'Content-Type': 'application/json' } }
      let response = await Axios.post('http://127.0.0.1:5000/addPasta',{ name:payload.name,category:payload.category,price:payload.price},config)
      return parseInt(response.data)
    },
    async login(context,payload){
      var config = { headers: {'Content-Type': 'application/json' } }
      let response = await Axios.post('http://127.0.0.1:5000/login',{ email:payload.email,password:payload.password},config)
      return parseInt(response.data)
    },
    async register(context,payload){
      var config = { headers: {'Content-Type': 'application/json' } }
      let response = await Axios.post('http://127.0.0.1:5000/register',
      {
        name:payload.name,
        email:payload.email,
        password:payload.password,
        address:payload.address
      },
      config)
      return parseInt(response.data)
    }

  }
  })


  /*
  login(context,payload){
      var config = { headers: {'Content-Type': 'application/json' } }

      Axios.post('http://127.0.0.1:5000/login',
      { email:payload.email,
        password:payload.password
      }
      ,config)
              .then(response => {
                if(response.data==='success'){
                  console.log("response.data="+response.data)
                  return 1
                } else {
                  console.log("login failed store.js")
                  return 0
                }
              })
              .catch(e => {
                console.log(e)
              })
    }
    */

    /*
    checkout(context,payload){
      var config = { headers: {'Content-Type': 'application/json' } }

      Axios.post('http://127.0.0.1:5000/bill',
      { cart:context.state.cart,
        customerId:state.loggedCustomerID
      }
      ,config)
              .then(response => {
                console.log("response data",response.data)
                context.state.cart=[]
              })
              .catch(e => {
                console.log(e)
              })
    }
    */
