<template>
  <button @click="decreaseValue">{{ value }}</button>
</template>
  
<script setup>
  import { ref } from 'vue';
  const value = ref(1000);
  const decreaseValue = () => value.value /= 2;
</script>