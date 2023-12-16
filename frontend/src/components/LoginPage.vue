<template>
  <div
    class="container vh-100 d-flex justify-content-center align-items-center"
  >
    <div
      class="card bg-light rounded p-5 shadow-sm border-0"
      shadow="444"
      style="max-width: 700 min-width: 500"
    >
      <h3 class="text-center">Войти в систему</h3>
      <form @submit.prevent="login" class="p-2">
        <div class="form-group mb-3">
          <input
            type="text"
            id="login"
            v-model="login"
            class="form-control"
            placeholder="Логин"
            required
          />
        </div>
        <div class="form-group mb-3">
          <input
            type="password"
            id="password"
            v-model="password"
            class="form-control"
            placeholder="Пароль"
            required
          />
        </div>
        <div class="form-group mb-3">
          <button type="submit" class="btn btn-primary w-50">Войти</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginPage",
  data() {
    return {
      login: "",
      password: "",
    };
  },
};
</script>

<style>
/* Import Montserrat font from Google Fonts */
@import url("https://fonts.googleapis.com/css?family=Montserrat&display=swap");

/* Apply Montserrat font to all elements */
* {
  font-family: "Montserrat", sans-serif;
}

/* Make the input placeholders light grey */
::placeholder {
  color: lightgrey;
}
</style>
