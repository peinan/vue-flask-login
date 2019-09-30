import Vue from "vue";
import Router from "vue-router";
import Signin from "./components/signin.vue";
import Signup from "./components/signup.vue";
import User from "./components/user.vue";
import NotFound from "./components/NotFound.vue";

Vue.use(Router);

export default new Router({
  routes: [
    { path: "/", name: "root", component: Signin },
    { path: "/signin", name: "signin", component: Signin },
    { path: "/signup", name: "signup", component: Signup },
    { path: "/user", name: "user", component: User },
    { path: "*", name: "NotFound", component: NotFound }
  ]
});
