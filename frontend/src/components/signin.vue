<template>
  <div class="signin">
    <v-snackbar color="error" v-model="snackbar" top :timeout="3000">
      {{ snackbarText }}
    </v-snackbar>

    <v-form ref="form">
      <v-card-text class="pb-2">
        <v-layout justify-start>
          <span class="display-1 primary--text mb-2">サインイン</span>
        </v-layout>

        <v-text-field
          class="mb-2"
          type="text"
          prepend-icon="person"
          v-model="username"
          :rules="nameRules"
          label="ユーザ名"
          clearable
          required
          :error="signinError"
        ></v-text-field>

        <v-text-field
          type="password"
          prepend-icon="lock"
          v-model="password"
          :append-icon="show ? 'visibility_off' : 'visibility'"
          :type="show ? 'text' : 'password'"
          @click:append="show = !show"
          :rules="passRules"
          label="パスワード"
          clearable
          required
          :error="signinError"
        ></v-text-field>
      </v-card-text>

      <v-card-actions>
        <v-layout justify-end>
          <v-btn text color="success" @click="signup">サインアップ</v-btn>
          <v-btn type="submit" depressed color="primary" @click="signin"
            >サインイン</v-btn
          >
        </v-layout>
      </v-card-actions>
    </v-form>
  </div>
</template>

<script>
import Cookies from "js-cookie";
import Axios from "axios";
import crypto from "crypto";
import router from "../router.js";

export default {
  name: "signin",
  data: function() {
    return {
      snackbar: false,
      snackbarText: "",
      username: "",
      password: "",
      nameRules: [v => !!v || "ユーザ名を入力してください"],
      passRules: [v => !!v || "パスワードを入力してください"],
      signinError: false,
      show: false
    };
  },
  methods: {
    signin: function() {
      this.snackbar = false;
      this.signinError = false;
      if (!this.$refs.form.validate()) {
        return;
      }
      let sha256 = crypto.createHash("sha256");
      sha256.update(this.password);
      const hashPass = sha256.digest("base64");

      let axios = Axios.create({
        baseURL: "http://localhost:5000",
        headers: {
          "Content-Type": "application/json",
          "X-Requested-With": "XMLHttpRequest"
        },
        responseType: "json"
      });
      let self = this;
      axios
        .post(
          "/signin",
          {
            username: self.username,
            password: hashPass
          },
          {
            validateStatus: function(status) {
              return status < 500;
            }
          }
        )
        .then(res => {
          if (res.data.access_token) {
            Cookies.set("jwt_token", res.data.access_token);
            router.push({ name: "user" });
          } else if (res.status === 401) {
            self.snackbarText = "ユーザ名またはパスワードが違います";
            self.snackbar = true;
            self.signinError = true;
          } else {
            throw new Error();
          }
        })
        .catch(() => {
          self.snackbarText = "エラーが発生しました";
          self.snackbar = true;
        });
    },
    signup: () => {
      router.push({ name: "signup" });
    }
  }
};
</script>
