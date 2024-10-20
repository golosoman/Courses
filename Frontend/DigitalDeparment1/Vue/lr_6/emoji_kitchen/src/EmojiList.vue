<script setup>
import { defineProps, defineEmits } from "vue";
import Emoji from "./Emoji.vue";

const props = defineProps({
    emojis: {
        type: Array,
        required: true,
        default: [],
    },
});

const emit = defineEmits(["selectEmoji"]);
</script>

<template>
    <div class="emoji_content">
        <div v-for="(emoji, index) in props.emojis" :key="index">
            <Emoji
                :htmlCode="emoji.htmlCode"
                @click="emit('selectEmoji', emoji)"
            />
        </div>
    </div>

    <!-- <ul id="array-with-index">
    <li v-for="(emoji, index) in emojis" :key="index">
        <Emoji :name="emoji.name" :category="emoji.category" :group="emoji.group" :htmlCode="emoji.htmlCode" :unicode="emoji.unicode" />
    </li>
    </ul> -->
</template>

<style scoped>
.emoji_content {
    display: flex;
    flex-wrap: wrap;
}
</style>
