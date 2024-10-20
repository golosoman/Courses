<script setup>
import { defineProps, computed } from "vue";
import Emoji from "./Emoji.vue";
const props = defineProps({
    firstEmoji: {
        type: Object,
        default: null,
    },
    secondEmoji: {
        type: Object,
        default: null,
    },
});

const mixedEmoji = computed(() => {
    if (props.firstEmoji && props.secondEmoji) {
        const [unicodeFirst, unicodeSecond] = [
            props.firstEmoji.unicode[0],
            props.secondEmoji.unicode[0],
        ].map((u) => u.replace("U+", "").toLowerCase());
        return `https://emk.vercel.app/s/${unicodeFirst}_${unicodeSecond}?size=96`;
    }
});
</script>

<template>
    <div class="content" v-if="props.firstEmoji && props.secondEmoji">
        {{ console.log(mixedEmoji) }}
        <Emoji :htmlCode="props.firstEmoji.htmlCode" />
        <p class="content-size">➕</p>
        <Emoji :htmlCode="props.secondEmoji.htmlCode" />
        <p class="content-size">❓=</p>
        <img :src="mixedEmoji" />
    </div>
    <!-- {{ console.log(props.firstEmoji, props.secondEmoji) }} -->
</template>

<style scoped>
.content {
    padding-left: 50%;
}
.content-size {
    font-size: 25px;
}
</style>
