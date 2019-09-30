<template>
  <div class="user">
    <v-card-text>
      <v-layout justify-start>
        <span class="display-1 primary--text mb-2">ユーザ</span>
      </v-layout>
      {{ username }}
    </v-card-text>

    <v-card-actions>
      <v-layout justify-end>
        <v-btn depressed color="error" @click="signout">
          サインアウト
        </v-btn>
      </v-layout>
    </v-card-actions>
  </div>
</template>

<script>
import router from "../router.js";

export default {
  name: "user",
  data: function() {
    return {
      username: ""
    };
  },
  methods: {
    signout: () => {
      router.push({ name: "signin" });
    }
  }
};
</script>
