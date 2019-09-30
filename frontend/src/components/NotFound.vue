<template>
  <div class="NotFound">
    <v-card-text>
      <v-layout justify-start>
        <span class="display-1 primary--text mb-2">NotFound</span>
      </v-layout>
    </v-card-text>

    <v-card-actions>
      <v-layout justify-end>
        <v-btn depressed color="success" @click="signin">
          サインイン
        </v-btn>
      </v-layout>
    </v-card-actions>
  </div>
</template>

<script>
import router from "../router.js";

export default {
  name: "NotFound",
  methods: {
    signin: () => {
      router.push({ name: "signin" });
    }
  }
};
</script>
