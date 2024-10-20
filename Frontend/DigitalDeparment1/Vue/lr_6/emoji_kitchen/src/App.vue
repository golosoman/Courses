<script setup>
import { onMounted, ref, computed } from "vue";
import EmojiList from "./EmojiList.vue";
import EmojiMixer from "./EmojiMixer.vue";
import Loader from "./Loader.vue";
import Comp from "./Comp.vue"

let emojis = ref([]);
let dataIsLoading = ref(true);
let selectedSmiles = ref([null, null]);

let var1 = ref(1);
let var2 = ref(2);
let a = computed(() => var1 + var2);

const getEmoji = async () => {
    try {
        let response = await fetch("https://emojihub.yurace.pro/api/all");

        if (!response.ok) {
            throw new Error(`Произошла ошибка: ${response.status}`);
        }

        let json = await response.json();
        console.log(json);
        return json;
    } catch (error) {
        console.log(error.message);
    }
};

onMounted(async () => {
    
    dataIsLoading.value = true;
    emojis.value = await getEmoji();
    dataIsLoading.value = false;
});

const handleSearchEmoji = (emoji, index) => {
    selectedSmiles.value[index] = emoji;
    console.log(selectedSmiles.value);
};
</script>

<template>
    <div>{{ a }}</div>
    <div><Comp /></div>
    <div v-if="dataIsLoading">
        <Loader />
    </div>
    <div class="page-wrapper" v-else>
        <div class="left-panel-wrapper">
            <EmojiList
                :emojis
                @selectEmoji="handleSearchEmoji($event, (index = 0))"
            />
        </div>
        <div class="content-wrapper">
            <div id="main">
                <EmojiMixer
                    :first-emoji="selectedSmiles[0]"
                    :second-emoji="selectedSmiles[1]"
                />
            </div>
        </div>
        <div class="right-panel-wrapper">
            <EmojiList
                :emojis
                @selectEmoji="handleSearchEmoji($event, (index = 1))"
            />
        </div>
    </div>
    
    <!-- <div>
        <input type="button" value="Получить" @click="getEmoji()" />
    </div> -->
</template>

<style scoped>
.page-wrapper {
    display: flex;
    justify-content: space-between;
}
.left-panel-wrapper {
    width: 500px;
    background-color: rgba(125, 120, 120, 0.152);
}
.right-panel-wrapper {
    width: 500px;
    background-color: rgba(125, 120, 120, 0.152);
}

#main {
    position: fixed; /* Фиксированное положение */
    left: 45%;
}
.content-wrapper {
    /*width: 250px;*/
    width: calc(100% - 400px);
    padding: 0 30px;
}
</style>
