<script setup>
import { defineProps } from "vue";
const props = defineProps({
    htmlCode: {
        type: Array,
        required: true,
    },
});
</script>

<template>
    <div class="emoji" v-html="props.htmlCode[0]"></div>
</template>

<style scoped>
.emoji {
    width: 30px;
    height: 30px;
    font-size: 25px;
}
</style>
