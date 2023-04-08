<template>
<div class="rating">
    <h3>
        {{ rating.restaurant_id }}
    </h3>
    <p>User: {{rating.user_id}}</p>
    <p>Food: {{rating.food}}</p>
    <p>Ambient: {{rating.ambient}}</p>
    <p>Staff: {{rating.staff}}</p>
    <p>Service: {{rating.service}}</p>
    <p>Price: {{rating.price}}</p>
    <p>Comment: {{rating.comment}}</p>
</div>
</template>

<script>

export default {
    name: 'Rating',
    props: {
        rating: Object,
    }
}
</script>

<style scope>
.rating {
  background: #f4f4f4;
  margin: 5px;
  padding: 10px 30px;
  cursor: pointer;
}
.rating.reminder {
  border-left: 5px solid green;
}
.rating h3 {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.rating h2 {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
</style>