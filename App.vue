<!-- frontend/src/App.vue -->

<template>
  <div>
    <h1>Inventory Dashboard</h1>
    <div v-if="loading">Loading...</div>
    <div v-else>
      <item-list v-for="item in items" :key="item.id" :item="item" />
    </div>
  </div>
</template>

<script>
import ItemList from './components/ItemList.vue';

export default {
  components: {
    ItemList,
  },
  data() {
    return {
      items: [],
      loading: true,
    };
  },
  mounted() {
    fetch('http://localhost:8000/api/items/')
      .then((response) => response.json())
      .then((data) => {
        this.items = data;
        this.loading = false;
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
        this.loading = false;
      });
  },
};
</script>

<style scoped>
/* Add your component styles here */
</style>
