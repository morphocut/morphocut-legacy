<template>
  <div class="home">
    <router-link to="/tiles">Tiles</router-link>
    <!-- <router-link to="/ping">Ping</router-link>
    <router-link to="/upload">Upload</router-link> -->
    <router-link to="/datasets">Datasets</router-link>
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'home',
  components: {
    HelloWorld
  }
}
</script>
