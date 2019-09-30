<template>
  <v-app>
    <v-content>
      <v-layout justify-center>
        <v-flex xs12 sm7 md5 lg3>
          <v-spacer class="py-4"></v-spacer>
          <v-card class="elevation-3 pa-2 mx-2">
            <router-view />
          </v-card>
        </v-flex>
      </v-layout>
    </v-content>
  </v-app>
</template>

<script>
import "./router.js";

export default {
  name: "App"
};
</script>
