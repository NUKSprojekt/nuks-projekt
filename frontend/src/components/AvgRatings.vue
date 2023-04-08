<template>
<div>
<div v-for="avgRating in avgRatings" :key="avgRating.id">
    <avgRating :avgRating="avgRating" />
</div>
</div>
    
</template>

<script>
import avgRating from './AvgRating.vue'
export default {
    name: 'AvgRatings',
    props: {
        avgRatings: Array,
    },
    components: {
        avgRating,
    }
}
</script>