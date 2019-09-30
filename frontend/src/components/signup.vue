<template>
  <div class="signup">
    <v-snackbar :color="snackbarColor" v-model="snackbar" top :timeout="3000">
      {{ snackbarText }}
    </v-snackbar>

    <v-card-text>
      <v-layout justify-start>
        <span class="display-1 primary--text mb-2">サインアップ</span>
      </v-layout>
      <v-form ref="form">
        <v-text-field
          class="mb-2"
          type="text"
          prepend-icon="person"
          v-model="username"
          :rules="[rules.required, rules.min3, rules.max20]"
          label="ユーザ名"
          clearable
          required
          :error="!username"
        ></v-text-field>

        <v-text-field
          class="mb-2"
          prepend-icon="lock"
          v-model="password"
          :append-icon="show ? 'visibility_off' : 'visibility'"
          :rules="[rules.required]"
          :type="show ? 'text' : 'password'"
          label="パスワード"
          counter
          required
          @click:append="show = !show"
          :error="!password"
        ></v-text-field>

        <v-text-field
          prepend-icon="lock"
          v-model="passwordConf"
          :rules="[rules.required]"
          type="password"
          label="確認"
          counter
          required
          :error="!passwordConf"
        ></v-text-field>
      </v-form>
    </v-card-text>

    <v-card-actions>
      <v-layout justify-end>
        <v-btn text color="primary" @click="signin">サインイン</v-btn>
        <v-btn depressed color="success" @click="signup" type="submit">
          サインアップ
        </v-btn>
      </v-layout>
    </v-card-actions>
  </div>
</template>

<script>
import crypto from "crypto";
import Axios from "axios";
import router from "../router.js";

export default {
  name: "signup",
  data: function() {
    return {
      snackbar: false,
      snackbarText: "",
      snackbarColor: "",
      username: "",
      password: "",
      passwordConf: "",
      show: false,
      rules: {
        required: v => !!v || "必須項目です",
        min3: v =>
          (v == null ? "" : v).length >= 3 || "3文字以上で入力してください",
        max20: v =>
          (v == null ? "" : v).length <= 20 || "20文字以内で入力してください"
      }
    };
  },
  methods: {
    signup: function() {
      this.snackbar = false;
      if (!this.$refs.form.validate()) {
        return;
      }
      if (this.password !== this.passwordConf) {
        return;
      }

      let sha256 = crypto.createHash("sha256");
      sha256.update(this.password);
      const hashPass = sha256.digest("base64");

      let sha256Conf = crypto.createHash("sha256");
      sha256Conf.update(this.passwordConf);
      const hashPassConf = sha256Conf.digest("base64");

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
        .post("/signup", {
          username: self.username,
          password: hashPass,
          passwordConf: hashPassConf
        })
        .then(res => {
          self.snackbarText = "登録しました";
          self.snackbarColor = "success";
          self.snackbar = true;
          setTimeout(function() {
            router.push({ name: "signin" });
          }, 1500);
        })
        .catch(() => {
          self.snackbarText = "エラーが発生しました";
          self.snackbarColor = "error";
          self.snackbar = true;
        });
    },
    signin: () => {
      router.push({ name: "signin" });
    }
  }
};
</script>
