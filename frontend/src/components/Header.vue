<template>
    <header>
        <h1>{{ title }}</h1>
        <Button @btn-click="$emit
        ('toggle-add-rating')" 
        :text="showAddRating ? 'Close' : 'Add Rating'" 
        :color="showAddRating ? 'red' : 'green'" />
    </header>
</template>

<script>
import Button from './Button.vue'
export default{
    name: 'Header',
    props: {
        title: String,
        showAddRating: Boolean,
    },
    components: {
        Button,
    },
}
</script>

<style scoped> 
header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}
</style>