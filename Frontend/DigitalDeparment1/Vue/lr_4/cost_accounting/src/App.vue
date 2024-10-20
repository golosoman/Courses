<script setup>
  import { computed, ref } from "vue";
  let history = ref([]);
  let title = ref("");
  let amount = ref("");

  let incomeBalance = computed(() => {
      return history.value.reduce(
          (total, current) => (total += current.amount > 0 ? current.amount : 0),
          0
      );
  });

  let outcomeBalance = computed(() => {
      return history.value.reduce(
          (total, current) => (total += current.amount < 0 ? current.amount : 0),
          0
      );
  });

  let totalBalance = computed(() => {
      let total = outcomeBalance.value + incomeBalance.value;
      return total;
  });

  const addElementInList = () => {
      if(title.value.trim() === "" || String(amount.value).trim() === ""){
        console.log("Не все поля заполнены")
      }
      else{
        history.value.push({
          "text": title.value,
          "amount": amount.value,
        });
        title.value = "";
        amount.value = "";
      }
      
  };
</script>

<template>
  <div class="content">
    <div v-if="history.length != 0">
        <div>
            <h1>Учет расходов</h1>
            <h2>Баланс: {{ totalBalance }}</h2>
            <h2>Расходы: {{ outcomeBalance }}</h2>
            <h2>Доходы: {{ incomeBalance }}</h2>
        </div>
        <ul id="history">
            <li v-for="(item, index) in history" :key="index + 1">
                {{ "Название: " + item.text + " Сумма: " + item.amount }}
            </li>
        </ul>
    </div>
    <div v-else>
        <h2>Вы не совершали финансовых операций</h2>
    </div>
    <form>
        <label for="title">Название</label><br />
        <input type="text" name="title" v-model.trim="title" required/><br />
        <label for="amount">Денежная сумма</label><br />
        <input type="number" name="amount" v-model.number="amount" required/><br />
        <input type="button" class="sbutton" value="Добавить" @click="addElementInList()" />
    </form>
  </div>
</template>

<style scoped>

  .content {
    margin-top: 10px;
    margin-left: 30px;
  }

  /* Стили для заголовков */
  h1 {
    font-family: 'Courier New', Courier, monospace;
    font-size: 36px;
    font-weight: bold;
    color: #2b2b2b; /* Цвет текста */
    margin-bottom: 20px;
    text-align: left;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); /* Тень текста */
  }

  h2 {
    font-family: 'Courier New', Courier, monospace;
    font-size: 24px;
    font-weight: bold;
    color: #2b2b2b;
    margin-bottom: 15px;
  }

  /* Стили для списков */
  ul {
    list-style-type: none;
    padding-left: 0;
  }

  li {
    font-family: 'Courier New', Courier, monospace;
    font-size: 16px;
    color: #2b2b2b;
    margin-bottom: 10px;
  }

  /* Стили для форм */
  form {
    font-family: 'Courier New', Courier, monospace;
    padding: 10px;
    font-size: 16px;
    color: #2b2b2b;
  }

  /* Стили для кнопок */
  .sbutton {
    margin-top: 10px;
    font-family: 'Courier New', Courier, monospace;
    font-size: 16px;
    font-weight: bold;
    color: #ffffff; /* Цвет текста */
    background-color: #4CAF50; /* Цвет фона */
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    border-radius: 5px;
  }

  .sbutton:hover {
    background-color: #45a049; /* Цвет фона при наведении */
  }

  /* Стили для поля ввода */
  input[type="text"],
  input[type="number"],
  textarea {
    font-family: 'Courier New', Courier, monospace;
    font-size: 16px;
    color: #2b2b2b;
    padding: 10px;
    border: 2px solid #cccccc; /* Цвет рамки */
    border-radius: 5px;
    margin-bottom: 15px;
  }

  input[type="text"]:focus,
  input[type="number"]:focus,
  textarea:focus {
    outline: none;
    border-color: #4CAF50; /* Цвет рамки при фокусе */
  }

  /* Дополнительные стили для поля ввода с ошибкой */
  .input-error {
    border-color: #ff6347; /* Цвет рамки при ошибке */
  }
</style>
