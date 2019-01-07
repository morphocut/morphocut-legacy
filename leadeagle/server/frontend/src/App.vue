<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

#header {
  position: -webkit-sticky;
  position: sticky;
  top: 0;
  z-index: 1071;
}
#sidebar {
  background: #fff;
  border-right: 1px solid #e5e5e5;
  border-bottom: 1px solid #e5e5e5;
}
@media (min-width: 768px) {
  #sidebar {
    position: -webkit-sticky;
    position: sticky;
    top: 3.5rem;
    z-index: 1000;
    max-height: calc(100vh - 3.5rem);
    border-right: 1px solid #e5e5e5;
    border-bottom: 1px solid #e5e5e5;
  }
}
#sidebar-nav {
  padding-top: 1rem;
  padding-bottom: 1rem;
  margin-right: -15px;
  margin-left: -15px;
  max-height: 100%;
  overflow-y: auto;
}
#sidebar-nav .nav {
  display: block;
}
#sidebar-nav .nav .nav-item .nav {
  display: none;
  margin-bottom: 1rem;
}
#sidebar-nav .nav .nav-item .nav {
  display: none;
  margin-bottom: 1rem;
}
#sidebar-nav .nav .nav-item.active .nav, #sidebar-nav .nav .active + .nav {
  display: block;
}
@media (min-width: 768px) {
  #sidebar-nav .nav .nav-item .nav {
    display: block;
  }
}
#sidebar-nav .nav .nav-link.active, #sidebar-nav .nav .active > .nav-link{
  color: #262626;
  font-weight: 500;
}
#sidebar-nav .nav-item .nav-link {
  padding: .25rem 1rem;
  font-weight: 500;
  color: #666
}
#sidebar-nav .nav-item .nav-item .nav-link {
  font-weight: 400;
  font-size: 85%;
  margin-left: 1rem
}
#main {
  padding-top: 1rem;
  margin-bottom: 2rem
}
blockquote {
  margin-bottom: 1rem;
  font-size: 1.25rem;
  padding: 0 1em;
  color: #6a737d;
  border-left: 0.25em solid #dfe2e5;
}
pre {
  padding: 16px;
  overflow: auto;
  font-size: 85%;
  line-height: 1.45;
  background-color: #f6f8fa;
  border-radius: 3px;
}
.modal-backdrop.fade {
  visibility: hidden;
}
.modal-backdrop.fade.show {
  visibility: visible;
}
.fade.show {
  display: block;
  /* z-index: 1; */
}
</style>
