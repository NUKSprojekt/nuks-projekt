<template>
<div class="avgRating">
    <h3>
        {{ avgRating.restaurant_name }}
        <p>Average: {{ avgRating.average }}</p>
    </h3>
    <p>Food: {{ avgRating.food }}</p>
    <p>Ambient: {{ avgRating.ambient }}</p>
    <p>Staff: {{ avgRating.staff }}</p>
    <p>Service: {{ avgRating.service }}</p>
    <p>Price: {{ avgRating.price }}</p>
    
</div>
</template>

<script>

export default {
    name: 'AvgRating',
    props: {
        avgRating: Object,
    },
}
</script>

<style scope>
.avgRating {
  background: #f4f4f4;
  margin: 5px;
  padding: 10px 30px;
  cursor: pointer;
}
.rating.reminder {
  border-left: 5px solid green;
}
.avgRating h3 {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.avgRating h2 {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
</style>