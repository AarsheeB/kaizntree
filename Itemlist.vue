<!-- frontend/src/components/ItemList.vue -->

<template>
  <div>
    <h2>{{ item.name }}</h2>
    <p>SKU: {{ item.sku }}</p>
    <p>Category: {{ item.category.name }}</p>
    <p>Tags: {{ item.tags.map(tag => tag.name).join(', ') }}</p>
    <p>Quantity: {{ item.quantity }}</p>
    <p>Price: ${{ item.price }}</p>
  </div>
</template>

<script>
export default {
  props: ['item'],
};
</script>

<style scoped>
/* Add your component styles here */
</style>
