<template>
    <div>
        <form class="form_content">
            <label for="name">Имя</label>
            <input type="text" class="field_input" name="name" v-model="user.name" /><br />
            <label for="surname">Фамилия</label>
            <input type="text" class="field_input" name="surname" v-model="user.surname" /><br />
            <fieldset>
                <legend>Выберите пол:</legend>
                <div>
                    <input
                        type="radio"
                        name="gender"
                        value="Man"
                        v-model="user.gender"
                    />
                    <label for="Man">М</label>
                </div>
                <div>
                    <input
                        type="radio"
                        name="gender"
                        value="Woman"
                        v-model="user.gender"
                    />
                    <label for="Woman">Ж</label>
                </div>
            </fieldset>
            <label for="password">Пароль</label>
            <input :type="showPassword ? 'text' : 'password'" name="password" class="field_input" v-model="password" /><br />
            <label for="password">Подтверждение пароля</label>
            <input :type="showPassword ? 'text' : 'password'" name="passwordConfirm" class="field_input" v-model="passwordConf" /><br />
            <input type="button" value="Показать пароль" class="form_content_submit" @mousedown="showPassword = true" @mouseup="showPassword = false">
            <input
                type="button"
                value="Зарегестрироваться"
                class="form_content_submit"
                @click="printToConsole()"
                :disabled="validatePassword(password, passwordConf)"
            />
        </form>
    </div>
    <div>
        <p>
            Пользователь: {{ user.name }} {{ user.surname }}.
            {{ checkGender(user.gender) }} пола.
        </p>
    </div>
</template>

<script setup>
    import { reactive, ref } from "vue";

    let user = reactive({
        name: "",
        surname: "",
        gender: "",
    });

    let password = ref("");
    let passwordConf = ref("");

    const validatePassword = (firstPassword, secondPassword) => {
        return !(firstPassword.trim() !== "" && firstPassword === secondPassword);
    };

    const checkGender = (gender) => {
        return gender === "Woman" ? "Женского" : gender === "Man"? "Мужского": "";
    };

    const printToConsole = () => {
        console.log(`name: ${user.name}, surname: ${
            user.surname
        }, gender: ${user.gender}, 
                password: ${password.value}, passwordConfirm ${passwordConf.value}`);
    };

    // const changeShowPassword()

    let showPassword = ref(false);
</script>

<style scoped>
    *:disabled {
        background-color: dimgrey;
        color: linen;
        opacity: 1;
    }

    .form_content{
    width: 200px;
    background: #f1f5fc;
    border: 1px solid black;
    border-radius: 15%;
    padding: 5%;
    margin: 20px auto 0 auto;
    }
    .form_content_submit{
        margin-top: 10px;
        padding:5px;
    }

    .field_input{
        width: 200px;
        padding:5px;
    }

</style>
