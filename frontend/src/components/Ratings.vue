<template>
<div>
<div v-for="rating in ratings" :key="rating.id">
    <Rating :rating="rating" />
</div>
</div>
    
</template>

<script>
import Rating from './Rating.vue'
export default {
    name: 'Ratings',
    props: {
        ratings: Array,
    },
    components: {
        Rating,
    }
}
</script>