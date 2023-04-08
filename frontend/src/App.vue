/* eslint-disable */
<template>
  <div class="container">
    <Header @toggle-add-rating="toggleAddRating" title="Restaurants" :showAddRating="showAddRating"/>
    <div v-show="showAddRating">
      <AddRating @add-rating="addRating"/>
    </div>
    <!--<Ratings :ratings="ratings" /> -->
    <AvgRatings :avgRatings="avgRatings" />
  </div>
</template>

<script>
import Header from './components/Header.vue'
//import Ratings from './components/Ratings.vue'
import AddRating from './components/AddRating.vue'
import AvgRatings from './components/AvgRatings.vue'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    Header,
    //Ratings,
    AddRating,
    AvgRatings
  },
  data() {
    return {
      msg: '',
      ratings: [],
      showAddRating: false,
      avgRatings: [],
    }
  },
  methods: {
    toggleAddRating(){
      this.showAddRating = !this.showAddRating
    },

    /*
    getRestaurants() {
      axios.get('http://localhost:8000/restaurants')
      .then((res) => {
        this.msg = res.data;
        console.log(res);
      })
      .catch((error) => {
        console.error(error)
      });
    },
  

    getRating() {
      axios.get('http://localhost:8000/rating/{rating_id}?id=2')
      .then((rating) => {
        this.rating = rating.data
        console.log(rating)
        console.log(this.msg)
      })
    },
    */
    getRatings() {
      axios.get('http://localhost:8000/ratings')
      .then((ratings) => {
        this.ratings = ratings.data;
        console.log(ratings);
      })
      .catch((error) => {
        console.error(error)
      });
    },

    getAvgRatings() {
      axios.get('http://localhost:8000/restaurants/averages')
      .then((avgratings) => {
        this.avgRatings = avgratings.data;
        console.log(avgratings);
      })
      .catch((error) => {
        console.error(error)
      });
    },

    addRating(rating){
      console.log(rating);
      axios.post('http://localhost:8000/rating', rating, {
        headers: {
        "Content-Type": "application/json",
        }
      })
      .then((response) => {
        const addedRating = response.data;
        console.log(addedRating)
        this.ratings = [...this.ratings, rating]
        this.getAvgRatings()
      })
      .catch((error) => console.error(error));
    }
  },

  mounted() {
    //his.getRatings();
    this.getAvgRatings();
  }
}
</script>

<style>
/*
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
*/
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap');
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
body {
  font-family: 'Poppins', sans-serif;
}
.container {
  max-width: 800px;
  margin: 30px auto;
  overflow: auto;
  min-height: 400px;
  border: 1px solid steelblue;
  padding: 30px;
  border-radius: 5px;
}
.btn {
  display: inline-block;
  background: #000;
  color: #fff;
  border: none;
  padding: 10px 20px;
  margin: 5px;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
  font-size: 15px;
  font-family: inherit;
}
.btn:focus {
  outline: none;
}
.btn:active {
  transform: scale(0.98);
}
.btn-block {
  display: block;
  width: 100%;
}
</style>