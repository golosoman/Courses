<script setup>
    import { ref, onMounted } from "vue";
    let number = ref("");
    let type = ref("");
    let result = ref("Здесь будут ответы!");
    let dataIsLoading = ref(false);
    let inputNumber = ref(null);

    const searchFact = async () => {
        dataIsLoading.value = true;
        try {
            const response = await fetch(`http://numbersapi.com/${number.value}/${type.value}?json`);
            const json = await response.json();
            if (json.found) {
                result.value = json.text;
            } else {
                result.value = `${json.number} - скучное число`
            }
        } catch (error) {
            console.log(error)
            result.value = 'Что-то пошло не так, проверьте правильность введенных данных!'
        }
        dataIsLoading.value = false;
        return result;
    };

    const focus = () => {
        inputNumber.value.focus();
    }

    onMounted (() => {
        focus();
    });

</script>

<template>
    <div class="container">
        <div v-if="dataIsLoading">
            <span class="loader"></span>
        </div>
        <div v-else>
            <h3>{{ result }}</h3>
        </div>
        <form>
            <label for="number">Введите число: </label><br/>
            <input type="number" name="number" required ref="inputNumber" v-model.number="number"/><br/>
            <fieldset>
                <legend>Выберите факт:</legend>
                <div>
                    <label>
                        <input
                            type="radio"
                            name="fact"
                            value="math"
                            v-model="type"
                            required
                        />
                        Факт из области математики
                    </label>
                </div>
                <div>
                    <label>
                        <input
                            type="radio"
                            name="fact"
                            value="year"
                            v-model="type"
                        />
                        Факт о введенном годе
                    </label>
                </div>
                <div>
                    <label>
                        <input
                            type="radio"
                            name="fact"
                            value="trivia"
                            checked
                            v-model="type"
                        />
                        Случайный факт о числе
                    </label>
                </div>
            </fieldset>
            <input type="button" value="Поиск" @click="searchFact()">
        </form>
    </div>
</template>

<style scoped>
    .loader{
      display: block;
      position: relative;
      height: 12px;
      width: 100%;
      border: 1px solid #010000;
      border-radius: 10px;
      overflow: hidden;
    }
    .loader::after {
      content: '';
      width: 40%;
      height: 100%;
      background: #4CAF50;
      position: absolute;
      top: 0;
      left: 0;
      box-sizing: border-box;
      animation: animloader 2s linear infinite;
    }
    
    @keyframes animloader {
      0% {
        left: 0;
        transform: translateX(-100%);
      }
      100% {
        left: 100%;
        transform: translateX(0%);
      }
    }

    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        color: #333;
        margin: 0;
        padding: 0;
    }

    .container {
        max-width: 800px;
        margin: 0 auto;
        margin-top: 50px;
        padding: 20px;
        background-color: #fff;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    h3 {
        font-size: 24px;
        margin-bottom: 20px;
    }

    form {
        margin-bottom: 20px;
    }

    label {
        margin-bottom: 10px;
        font-weight: bold;
    }

    input[type="number"]:focus,
    textarea:focus {
        outline: none;
        border-color: #4CAF50; /* Цвет рамки при фокусе */
    }

    input[type="number"],
    input[type="button"] {
        padding: 10px;
        width: 100%;
        margin-bottom: 15px;
        box-sizing: border-box;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    input[type="button"] {
        background-color: #4CAF50;
        color: white;
        border: none;
        cursor: pointer;
    }

    input[type="button"]:hover {
        background-color: #45a049;
    }

    fieldset {
        margin-bottom: 10px;
        border: 2px solid #ddd;
        padding: 10px;
        border-radius: 5px;
    }

    legend {
        font-weight: bold;
        color: #333;
    }

    input[type="radio"] {
        margin-right: 10px;
    }
</style>
