<template>
  <form @submit="onSubmit" class="add-form">
    <div>
      <label for="options">Choose a restaurant: </label>
      <select name="options" id="options" v-model="selectedRestaurant">
        <option v-for="(option, index) in options" :key="index" :value="option.id">{{ option.restaurant_name }}</option>
      </select>
    </div>
    <div class="form-control">
      <label>User</label>
      <input type="text" v-model="user" name="user" placeholder="Pick a Username" />
    </div> 
    <div class="form-control">
      <label>Food Rating</label>
      <input type="text" v-model="food" name="food" placeholder="1 (Very Bad) - 5 (Excellent)"/>
    </div>
    <div class="form-control">
      <label>Ambient Rating</label>
      <input type="text" v-model="ambient" name="ambient" placeholder="1 (Very Bad) - 5 (Excellent)"/>
    </div>
    <div class="form-control">
      <label>Staff Rating</label>
      <input type="text" v-model="staff" name="staff" placeholder="1 (Very Bad) - 5 (Excellent)"/>
    </div>
    <div class="form-control">
      <label>Service Rating</label>
      <input type="text" v-model="service" name="service" placeholder="1 (Very Bad) - 5 (Excellent)"/>
    </div>
    <div class="form-control">
      <label>Price Rating</label>
      <input type="text" v-model="price" name="price" placeholder="1 (Not Worth It) - 5 (Worth My Money)"/>
    </div>
    <div class="form-control">
      <label>Comment</label>
      <input type="text" v-model="comment" name="comment" placeholder="Add a Comment"/>
    </div>

    <input type="submit" value="Submit Rating" class="btn btn-block" />
  </form>
    
</template>

<script>
import axios from 'axios'

export default {
    name: 'AddRating',
    data() {
        return{
            restaurant_id: '',
            user: '',
            food: '',
            ambient: '',
            staff: '',
            service: '',
            price: '',
            comment: '',
            options: [],
            selectedRestaurant: null,
            selres: '',
        }
    },
    methods: {
        onSubmit(e) {
            e.preventDefault()
            if(!this.user) {
                alert('Please pick a username')
                return
            }
            const newRating = {
                restaurant_id: this.selectedRestaurant,
                user: this.user,
                food: this.food,
                ambient: this.ambient,
                staff: this.staff,
                service: this.service,
                price: this.price,
                comment: this.comment
            }
            this.$emit('add-rating', newRating)
            this.restaurant = '',
            this.user = '',
            this.food = '',
            this.ambient = '',
            this.staff = '',
            this.service = '',
            this.price = '',
            this.comment = ''
        }
    },

    created() {
      axios.get('http://localhost:8000/restaurants')
      .then(response => {
        this.options = response.data;
        console.log(response.data);
      })
      .catch(error => {
        console.log(error);
      });
    },

    watch: {
      selectedRestaurant: function() {
        if(this.selectedRestaurant) {
          console.log('Selected restaurant ID: ', this.selectedRestaurant);
          console.log(typeof this.selectedRestaurant);
          this.selres = (this.selectedRestaurant).toString();
          console.log(typeof this.selres);
        }
      }
    }
}
</script>

<style scoped>
.add-form {
  margin-bottom: 40px;
}
.form-control {
  margin: 20px 0;
}
.form-control label {
  display: block;
}
.form-control input {
  width: 100%;
  height: 40px;
  margin: 5px;
  padding: 3px 7px;
  font-size: 17px;
}
.form-control-check {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.form-control-check label {
  flex: 1;
}
.form-control-check input {
  flex: 2;
  height: 20px;
}
</style>