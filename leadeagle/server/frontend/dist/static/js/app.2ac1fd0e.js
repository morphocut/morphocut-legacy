(function(t){function e(e){for(var s,o,n=e[0],l=e[1],d=e[2],c=0,u=[];c<n.length;c++)o=n[c],r[o]&&u.push(r[o][0]),r[o]=0;for(s in l)Object.prototype.hasOwnProperty.call(l,s)&&(t[s]=l[s]);p&&p(e);while(u.length)u.shift()();return i.push.apply(i,d||[]),a()}function a(){for(var t,e=0;e<i.length;e++){for(var a=i[e],s=!0,o=1;o<a.length;o++){var n=a[o];0!==r[n]&&(s=!1)}s&&(i.splice(e--,1),t=l(l.s=a[0]))}return t}var s={},o={app:0},r={app:0},i=[];function n(t){return l.p+"static/js/"+({tiles:"tiles"}[t]||t)+"."+{tiles:"b8738810"}[t]+".js"}function l(e){if(s[e])return s[e].exports;var a=s[e]={i:e,l:!1,exports:{}};return t[e].call(a.exports,a,a.exports,l),a.l=!0,a.exports}l.e=function(t){var e=[],a={tiles:1};o[t]?e.push(o[t]):0!==o[t]&&a[t]&&e.push(o[t]=new Promise(function(e,a){for(var s="static/css/"+({tiles:"tiles"}[t]||t)+"."+{tiles:"d9d59247"}[t]+".css",o=l.p+s,r=document.getElementsByTagName("link"),i=0;i<r.length;i++){var n=r[i],d=n.getAttribute("data-href")||n.getAttribute("href");if("stylesheet"===n.rel&&(d===s||d===o))return e()}var c=document.getElementsByTagName("style");for(i=0;i<c.length;i++){n=c[i],d=n.getAttribute("data-href");if(d===s||d===o)return e()}var u=document.createElement("link");u.rel="stylesheet",u.type="text/css",u.onload=e,u.onerror=function(e){var s=e&&e.target&&e.target.src||o,r=new Error("Loading CSS chunk "+t+" failed.\n("+s+")");r.request=s,a(r)},u.href=o;var p=document.getElementsByTagName("head")[0];p.appendChild(u)}).then(function(){o[t]=0}));var s=r[t];if(0!==s)if(s)e.push(s[2]);else{var i=new Promise(function(e,a){s=r[t]=[e,a]});e.push(s[2]=i);var d,c=document.getElementsByTagName("head")[0],u=document.createElement("script");u.charset="utf-8",u.timeout=120,l.nc&&u.setAttribute("nonce",l.nc),u.src=n(t),d=function(e){u.onerror=u.onload=null,clearTimeout(p);var a=r[t];if(0!==a){if(a){var s=e&&("load"===e.type?"missing":e.type),o=e&&e.target&&e.target.src,i=new Error("Loading chunk "+t+" failed.\n("+s+": "+o+")");i.type=s,i.request=o,a[1](i)}r[t]=void 0}};var p=setTimeout(function(){d({type:"timeout",target:u})},12e4);u.onerror=u.onload=d,c.appendChild(u)}return Promise.all(e)},l.m=t,l.c=s,l.d=function(t,e,a){l.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:a})},l.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},l.t=function(t,e){if(1&e&&(t=l(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var a=Object.create(null);if(l.r(a),Object.defineProperty(a,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var s in t)l.d(a,s,function(e){return t[e]}.bind(null,s));return a},l.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return l.d(e,"a",e),e},l.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},l.p="/frontend/",l.oe=function(t){throw console.error(t),t};var d=window["webpackJsonp"]=window["webpackJsonp"]||[],c=d.push.bind(d);d.push=e,d=d.slice();for(var u=0;u<d.length;u++)e(d[u]);var p=c;i.push([0,"chunk-vendors"]),a()})({0:function(t,e,a){t.exports=a("56d7")},"034f":function(t,e,a){"use strict";var s=a("c21b"),o=a.n(s);o.a},"41f3":function(t,e,a){"use strict";var s=a("e918"),o=a.n(s);o.a},"524c":function(t,e,a){"use strict";var s=a("8f77"),o=a.n(s);o.a},"56d7":function(t,e,a){"use strict";a.r(e);a("cadf"),a("551c"),a("097d");var s=a("2b0e"),o=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{attrs:{id:"app"}},[a("b-navbar",{attrs:{toggleable:"md",type:"dark",variant:"dark",sticky:"true"}},[a("b-navbar-toggle",{attrs:{target:"nav_collapse"}}),a("b-navbar-brand",{attrs:{to:"/"}},[t._v("LeadEagle")]),a("b-collapse",{attrs:{"is-nav":"",id:"nav_collapse"}},[a("b-navbar-nav",[a("b-nav-item",{attrs:{to:"/datasets"}},[t._v("Datasets")]),a("b-nav-item",{attrs:{to:"/projects"}},[t._v("Projects")])],1)],1)],1),a("router-view")],1)},r=[],i=(a("034f"),a("2877")),n={},l=Object(i["a"])(n,o,r,!1,null,null,null);l.options.__file="App.vue";var d=l.exports,c=a("8c4f"),u=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"home"},[t._m(0),t._m(1),a("div",{staticClass:"col col-12"},[a("div",{staticClass:"row"},[a("div",{staticClass:"centering"},[a("b-button",{attrs:{to:"/datasets",variant:"primary"}},[t._v("Datasets")]),a("b-button",{attrs:{to:"/projects",variant:"primary"}},[t._v("Projects")])],1)]),t._m(2),a("div",{staticClass:"row"},[a("div",{staticClass:"centering"},[a("b-button",{attrs:{to:"/tiles"}},[t._v("Tiles")]),a("b-button",{attrs:{to:{name:"Ping",params:{userId:123}}}},[t._v("Ping")]),a("b-button",{attrs:{to:"/upload"}},[t._v("Upload")])],1)])])])},p=[function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",[s("img",{attrs:{alt:"Vue logo",src:a("cf05")}})])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("h1",[t._v("LeadEagle")])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"row"},[a("div",{staticClass:"divider"})])}],m=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"hello"},[a("h1",[t._v(t._s(t.msg))]),t._m(0),a("h3",[t._v("Installed CLI Plugins")]),t._m(1),a("h3",[t._v("Essential Links")]),t._m(2),a("h3",[t._v("Ecosystem")]),t._m(3)])},f=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("p",[t._v("\n    For guide and recipes on how to configure / customize this project,"),a("br"),t._v("\n    check out the\n    "),a("a",{attrs:{href:"https://cli.vuejs.org",target:"_blank",rel:"noopener"}},[t._v("vue-cli documentation")]),t._v(".\n  ")])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("ul",[a("li",[a("a",{attrs:{href:"https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel",target:"_blank",rel:"noopener"}},[t._v("babel")])]),a("li",[a("a",{attrs:{href:"https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-eslint",target:"_blank",rel:"noopener"}},[t._v("eslint")])])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("ul",[a("li",[a("a",{attrs:{href:"https://vuejs.org",target:"_blank",rel:"noopener"}},[t._v("Core Docs")])]),a("li",[a("a",{attrs:{href:"https://forum.vuejs.org",target:"_blank",rel:"noopener"}},[t._v("Forum")])]),a("li",[a("a",{attrs:{href:"https://chat.vuejs.org",target:"_blank",rel:"noopener"}},[t._v("Community Chat")])]),a("li",[a("a",{attrs:{href:"https://twitter.com/vuejs",target:"_blank",rel:"noopener"}},[t._v("Twitter")])]),a("li",[a("a",{attrs:{href:"https://news.vuejs.org",target:"_blank",rel:"noopener"}},[t._v("News")])])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("ul",[a("li",[a("a",{attrs:{href:"https://router.vuejs.org",target:"_blank",rel:"noopener"}},[t._v("vue-router")])]),a("li",[a("a",{attrs:{href:"https://vuex.vuejs.org",target:"_blank",rel:"noopener"}},[t._v("vuex")])]),a("li",[a("a",{attrs:{href:"https://github.com/vuejs/vue-devtools#vue-devtools",target:"_blank",rel:"noopener"}},[t._v("vue-devtools")])]),a("li",[a("a",{attrs:{href:"https://vue-loader.vuejs.org",target:"_blank",rel:"noopener"}},[t._v("vue-loader")])]),a("li",[a("a",{attrs:{href:"https://github.com/vuejs/awesome-vue",target:"_blank",rel:"noopener"}},[t._v("awesome-vue")])])])}],v={name:"HelloWorld",props:{msg:String}},h=v,b=(a("524c"),Object(i["a"])(h,m,f,!1,null,"b6a59770",null));b.options.__file="HelloWorld.vue";var _=b.exports,g={name:"home",components:{HelloWorld:_}},C=g,y=(a("cccb"),Object(i["a"])(C,u,p,!1,null,null,null));y.options.__file="Home.vue";var w=y.exports,D=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"container"},[a("div",[a("p",[t._v(t._s(t.msg))])]),a("button",{staticClass:"btn btn-primary",attrs:{type:"button"}},[t._v(t._s(t.msg))])])},x=[],k=a("bc3a"),F=a.n(k),$={name:"Ping",data:function(){return{msg:""}},methods:{getMessage:function(){var t=this,e="http://localhost:5000/ping";F.a.get(e).then(function(e){t.msg=e.data}).catch(function(t){console.error(t)})}},created:function(){this.getMessage()}},A=$,j=Object(i["a"])(A,D,x,!1,null,null,null);j.options.__file="Ping.vue";var S=j.exports,E=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"example-full"},[a("button",{staticClass:"btn btn-danger float-right btn-is-option",attrs:{type:"button"},on:{click:function(e){e.preventDefault(),t.isOption=!t.isOption}}},[a("i",{staticClass:"fa fa-cog",attrs:{"aria-hidden":"true"}}),t._v("\n    Options\n  ")]),a("h1",{staticClass:"example-title",attrs:{id:"example-title"}},[t._v(t._s(t.dataset.name)+": Upload")]),a("div",{directives:[{name:"show",rawName:"v-show",value:t.$refs.upload&&t.$refs.upload.dropActive,expression:"$refs.upload && $refs.upload.dropActive"}],staticClass:"drop-active"},[a("h3",[t._v("Hello there! Drop files to upload")])]),a("div",{directives:[{name:"show",rawName:"v-show",value:!t.isOption,expression:"!isOption"}],staticClass:"upload"},[a("div",{staticClass:"table-responsive"},[a("table",{staticClass:"table table-hover"},[t._m(0),a("tbody",[t._l(t.dataset_files,function(e,s){return a("tr",{key:e.object_id},[a("td",[t._v(t._s(s))]),t._m(1,!0),a("td",[a("div",{staticClass:"filename"},[t._v(t._s(e.filename))])]),a("td",[t._v("FileSize")]),a("td"),e.error?a("td",[t._v(t._s(e.error))]):e.success?a("td",[t._v("success")]):e.active?a("td",[t._v("active")]):a("td"),a("td",[a("div",{staticClass:"btn-group"},[a("button",{staticClass:"btn btn-secondary btn-sm dropdown-toggle",attrs:{type:"button"}},[t._v("Action")]),a("div",{staticClass:"dropdown-menu"},[a("a",{class:{"dropdown-item":!0,disabled:e.active||e.success||"compressing"===e.error},attrs:{href:"#"},on:{click:function(a){a.preventDefault(),!e.active&&!e.success&&"compressing"!==e.error&&t.onEditFileShow(e)}}},[t._v("Edit")]),a("div",{staticClass:"dropdown-divider"}),a("a",{staticClass:"dropdown-item",attrs:{href:"#"},on:{click:function(a){a.preventDefault(),t.$refs.upload.remove(e)}}},[t._v("Remove")])])])])])}),t.files.length?t._e():a("tr",[a("td",{attrs:{colspan:"7"}},[a("div",{staticClass:"text-center p-5"},[t._m(2),a("label",{staticClass:"btn btn-lg btn-primary",attrs:{for:t.name}},[t._v("Select Files")])])])]),t._l(t.files,function(e,s){return a("tr",{key:e.id},[a("td",[t._v(t._s(s))]),a("td",[e.thumb?a("img",{attrs:{src:e.thumb,width:"40",height:"auto"}}):a("span",[t._v("No Image")])]),a("td",[a("div",{staticClass:"filename"},[t._v(t._s(e.name))]),e.active||"0.00"!==e.progress?a("div",{staticClass:"progress"},[a("div",{class:{"progress-bar":!0,"progress-bar-striped":!0,"bg-danger":e.error,"progress-bar-animated":e.active},style:{width:e.progress+"%"},attrs:{role:"progressbar"}},[t._v(t._s(e.progress)+"%")])]):t._e()]),a("td",[t._v(t._s(t._f("formatFileSize")(e.size)))]),a("td",[t._v(t._s(t._f("formatFileSize")(e.speed)))]),e.error?a("td",[t._v(t._s(e.error))]):e.success?a("td",[t._v("success")]):e.active?a("td",[t._v("active")]):a("td"),a("td",[a("div",{staticClass:"btn-group"},[a("button",{staticClass:"btn btn-secondary btn-sm dropdown-toggle",attrs:{type:"button"}},[t._v("Action")]),a("div",{staticClass:"dropdown-menu"},[a("a",{class:{"dropdown-item":!0,disabled:e.active||e.success||"compressing"===e.error},attrs:{href:"#"},on:{click:function(a){a.preventDefault(),!e.active&&!e.success&&"compressing"!==e.error&&t.onEditFileShow(e)}}},[t._v("Edit")]),a("a",{class:{"dropdown-item":!0,disabled:!e.active},attrs:{href:"#"},on:{click:function(a){a.preventDefault(),e.active&&t.$refs.upload.update(e,{error:"cancel"})}}},[t._v("Cancel")]),e.active?a("a",{staticClass:"dropdown-item",attrs:{href:"#"},on:{click:function(a){a.preventDefault(),t.$refs.upload.update(e,{active:!1})}}},[t._v("Abort")]):e.error&&"compressing"!==e.error&&t.$refs.upload.features.html5?a("a",{staticClass:"dropdown-item",attrs:{href:"#"},on:{click:function(a){a.preventDefault(),t.$refs.upload.update(e,{active:!0,error:"",progress:"0.00"})}}},[t._v("Retry upload")]):a("a",{class:{"dropdown-item":!0,disabled:e.success||"compressing"===e.error},attrs:{href:"#"},on:{click:function(a){a.preventDefault(),!e.success&&"compressing"!==e.error&&t.$refs.upload.update(e,{active:!0})}}},[t._v("Upload")]),a("div",{staticClass:"dropdown-divider"}),a("a",{staticClass:"dropdown-item",attrs:{href:"#"},on:{click:function(a){a.preventDefault(),t.$refs.upload.remove(e)}}},[t._v("Remove")])])])])])})],2)])]),a("div",{staticClass:"example-foorer"},[a("div",{staticClass:"footer-status float-right"},[t._v("\n        Drop: "+t._s(!!t.$refs.upload&&t.$refs.upload.drop)+",\n        Active: "+t._s(!!t.$refs.upload&&t.$refs.upload.active)+",\n        Uploaded: "+t._s(!t.$refs.upload||t.$refs.upload.uploaded)+",\n        Drop active: "+t._s(!!t.$refs.upload&&t.$refs.upload.dropActive)+"\n      ")]),a("div",{staticClass:"btn-group"},[a("file-upload",{ref:"upload",staticClass:"btn btn-primary dropdown-toggle",attrs:{"post-action":t.postAction,"put-action":t.putAction,extensions:t.extensions,accept:t.accept,multiple:t.multiple,directory:t.directory,size:t.size||0,thread:t.thread<1?1:t.thread>5?5:t.thread,headers:t.headers,data:t.data,drop:t.drop,"drop-directory":t.dropDirectory,"add-index":t.addIndex},on:{"input-filter":t.inputFilter,"input-file":t.inputFile},model:{value:t.files,callback:function(e){t.files=e},expression:"files"}},[a("i",{staticClass:"fa fa-plus"}),t._v("\n          Select\n        ")]),a("div",{staticClass:"dropdown-menu"},[a("label",{staticClass:"dropdown-item",attrs:{for:t.name}},[t._v("Add files")]),a("a",{staticClass:"dropdown-item",attrs:{href:"#"},on:{click:t.onAddFolader}},[t._v("Add folder")]),a("a",{staticClass:"dropdown-item",attrs:{href:"#"},on:{click:function(e){e.preventDefault(),t.addData.show=!0}}},[t._v("Add data")])])],1),t.$refs.upload&&t.$refs.upload.active?a("button",{staticClass:"btn btn-danger",attrs:{type:"button"},on:{click:function(e){e.preventDefault(),t.$refs.upload.active=!1}}},[a("i",{staticClass:"fa fa-stop",attrs:{"aria-hidden":"true"}}),t._v("\n        Stop Upload\n      ")]):a("button",{staticClass:"btn btn-success",attrs:{type:"button"},on:{click:function(e){e.preventDefault(),t.$refs.upload.active=!0}}},[a("i",{staticClass:"fa fa-arrow-up",attrs:{"aria-hidden":"true"}}),t._v("\n        Start Upload\n      ")])])]),a("div",{directives:[{name:"show",rawName:"v-show",value:t.isOption,expression:"isOption"}],staticClass:"option"},[a("div",{staticClass:"form-group"},[a("label",{attrs:{for:"accept"}},[t._v("Accept:")]),a("input",{directives:[{name:"model",rawName:"v-model",value:t.accept,expression:"accept"}],staticClass:"form-control",attrs:{type:"text",id:"accept"},domProps:{value:t.accept},on:{input:function(e){e.target.composing||(t.accept=e.target.value)}}}),a("small",{staticClass:"form-text text-muted"},[t._v("Allow upload mime type")])]),a("div",{staticClass:"form-group"},[a("label",{attrs:{for:"extensions"}},[t._v("Extensions:")]),a("input",{directives:[{name:"model",rawName:"v-model",value:t.extensions,expression:"extensions"}],staticClass:"form-control",attrs:{type:"text",id:"extensions"},domProps:{value:t.extensions},on:{input:function(e){e.target.composing||(t.extensions=e.target.value)}}}),a("small",{staticClass:"form-text text-muted"},[t._v("Allow upload file extension")])]),a("div",{staticClass:"form-group"},[a("label",[t._v("PUT Upload:")]),a("div",{staticClass:"form-check"},[a("label",{staticClass:"form-check-label"},[a("input",{directives:[{name:"model",rawName:"v-model",value:t.putAction,expression:"putAction"}],staticClass:"form-check-input",attrs:{type:"radio",name:"put-action",id:"put-action",value:""},domProps:{checked:t._q(t.putAction,"")},on:{change:function(e){t.putAction=""}}}),t._v(" Off\n        ")])]),a("div",{staticClass:"form-check"},[a("label",{staticClass:"form-check-label"},[a("input",{directives:[{name:"model",rawName:"v-model",value:t.putAction,expression:"putAction"}],staticClass:"form-check-input",attrs:{type:"radio",name:"put-action",id:"put-action",value:"/upload/put"},domProps:{checked:t._q(t.putAction,"/upload/put")},on:{change:function(e){t.putAction="/upload/put"}}}),t._v(" On\n        ")])]),a("small",{staticClass:"form-text text-muted"},[t._v("After the shutdown, use the POST method to upload")])]),a("div",{staticClass:"form-group"},[a("label",{attrs:{for:"thread"}},[t._v("Thread:")]),a("input",{directives:[{name:"model",rawName:"v-model.number",value:t.thread,expression:"thread",modifiers:{number:!0}}],staticClass:"form-control",attrs:{type:"number",max:"5",min:"1",id:"thread"},domProps:{value:t.thread},on:{input:function(e){e.target.composing||(t.thread=t._n(e.target.value))},blur:function(e){t.$forceUpdate()}}}),a("small",{staticClass:"form-text text-muted"},[t._v("Also upload the number of files at the same time (number of threads)")])]),a("div",{staticClass:"form-group"},[a("label",{attrs:{for:"size"}},[t._v("Max size:")]),a("input",{directives:[{name:"model",rawName:"v-model.number",value:t.size,expression:"size",modifiers:{number:!0}}],staticClass:"form-control",attrs:{type:"number",min:"0",id:"size"},domProps:{value:t.size},on:{input:function(e){e.target.composing||(t.size=t._n(e.target.value))},blur:function(e){t.$forceUpdate()}}})]),a("div",{staticClass:"form-group"},[a("label",{attrs:{for:"minSize"}},[t._v("Min size:")]),a("input",{directives:[{name:"model",rawName:"v-model.number",value:t.minSize,expression:"minSize",modifiers:{number:!0}}],staticClass:"form-control",attrs:{type:"number",min:"0",id:"minSize"},domProps:{value:t.minSize},on:{input:function(e){e.target.composing||(t.minSize=t._n(e.target.value))},blur:function(e){t.$forceUpdate()}}})]),a("div",{staticClass:"form-group"},[a("label",{attrs:{for:"autoCompress"}},[t._v("Automatically compress:")]),a("input",{directives:[{name:"model",rawName:"v-model.number",value:t.autoCompress,expression:"autoCompress",modifiers:{number:!0}}],staticClass:"form-control",attrs:{type:"number",min:"0",id:"autoCompress"},domProps:{value:t.autoCompress},on:{input:function(e){e.target.composing||(t.autoCompress=t._n(e.target.value))},blur:function(e){t.$forceUpdate()}}}),t.autoCompress>0?a("small",{staticClass:"form-text text-muted"},[t._v("More than "+t._s(t.autoCompress)+" files are automatically compressed")]):a("small",{staticClass:"form-text text-muted"},[t._v("Set up automatic compression")])]),a("div",{staticClass:"form-group"},[a("div",{staticClass:"form-check"},[a("label",{staticClass:"form-check-label"},[a("input",{directives:[{name:"model",rawName:"v-model",value:t.addIndex,expression:"addIndex"}],staticClass:"form-check-input",attrs:{type:"checkbox",id:"add-index"},domProps:{checked:Array.isArray(t.addIndex)?t._i(t.addIndex,null)>-1:t.addIndex},on:{change:function(e){var a=t.addIndex,s=e.target,o=!!s.checked;if(Array.isArray(a)){var r=null,i=t._i(a,r);s.checked?i<0&&(t.addIndex=a.concat([r])):i>-1&&(t.addIndex=a.slice(0,i).concat(a.slice(i+1)))}else t.addIndex=o}}}),t._v(" Start position to add\n        ")])]),a("small",{staticClass:"form-text text-muted"},[t._v("Add a file list to start the location to add")])]),a("div",{staticClass:"form-group"},[a("div",{staticClass:"form-check"},[a("label",{staticClass:"form-check-label"},[a("input",{directives:[{name:"model",rawName:"v-model",value:t.drop,expression:"drop"}],staticClass:"form-check-input",attrs:{type:"checkbox",id:"drop"},domProps:{checked:Array.isArray(t.drop)?t._i(t.drop,null)>-1:t.drop},on:{change:function(e){var a=t.drop,s=e.target,o=!!s.checked;if(Array.isArray(a)){var r=null,i=t._i(a,r);s.checked?i<0&&(t.drop=a.concat([r])):i>-1&&(t.drop=a.slice(0,i).concat(a.slice(i+1)))}else t.drop=o}}}),t._v(" Drop\n        ")])]),a("small",{staticClass:"form-text text-muted"},[t._v("Drag and drop upload")])]),a("div",{staticClass:"form-group"},[a("div",{staticClass:"form-check"},[a("label",{staticClass:"form-check-label"},[a("input",{directives:[{name:"model",rawName:"v-model",value:t.dropDirectory,expression:"dropDirectory"}],staticClass:"form-check-input",attrs:{type:"checkbox",id:"drop-directory"},domProps:{checked:Array.isArray(t.dropDirectory)?t._i(t.dropDirectory,null)>-1:t.dropDirectory},on:{change:function(e){var a=t.dropDirectory,s=e.target,o=!!s.checked;if(Array.isArray(a)){var r=null,i=t._i(a,r);s.checked?i<0&&(t.dropDirectory=a.concat([r])):i>-1&&(t.dropDirectory=a.slice(0,i).concat(a.slice(i+1)))}else t.dropDirectory=o}}}),t._v(" Drop directory\n        ")])]),a("small",{staticClass:"form-text text-muted"},[t._v("Not checked, filter the dragged folder")])]),a("div",{staticClass:"form-group"},[a("div",{staticClass:"form-check"},[a("label",{staticClass:"form-check-label"},[a("input",{directives:[{name:"model",rawName:"v-model",value:t.uploadAuto,expression:"uploadAuto"}],staticClass:"form-check-input",attrs:{type:"checkbox",id:"upload-auto"},domProps:{checked:Array.isArray(t.uploadAuto)?t._i(t.uploadAuto,null)>-1:t.uploadAuto},on:{change:function(e){var a=t.uploadAuto,s=e.target,o=!!s.checked;if(Array.isArray(a)){var r=null,i=t._i(a,r);s.checked?i<0&&(t.uploadAuto=a.concat([r])):i>-1&&(t.uploadAuto=a.slice(0,i).concat(a.slice(i+1)))}else t.uploadAuto=o}}}),t._v(" Auto start\n        ")])]),a("small",{staticClass:"form-text text-muted"},[t._v("Automatically activate upload")])]),a("div",{staticClass:"form-group"},[a("button",{staticClass:"btn btn-primary btn-lg btn-block",attrs:{type:"button"},on:{click:function(e){e.preventDefault(),t.isOption=!t.isOption}}},[t._v("Confirm")])])]),a("div",{class:{"modal-backdrop":!0,fade:!0,show:t.addData.show}}),a("div",{class:{modal:!0,fade:!0,show:t.addData.show},attrs:{id:"modal-add-data",tabindex:"-1",role:"dialog"}},[a("div",{staticClass:"modal-dialog",attrs:{role:"document"}},[a("div",{staticClass:"modal-content"},[a("div",{staticClass:"modal-header"},[a("h5",{staticClass:"modal-title"},[t._v("Add data")]),a("button",{staticClass:"close",attrs:{type:"button"},on:{click:function(e){e.preventDefault(),t.addData.show=!1}}},[a("span",[t._v("×")])])]),a("form",{on:{submit:function(e){return e.preventDefault(),t.onAddData(e)}}},[a("div",{staticClass:"modal-body"},[a("div",{staticClass:"form-group"},[a("label",{attrs:{for:"name"}},[t._v("Name:")]),a("input",{directives:[{name:"model",rawName:"v-model",value:t.addData.name,expression:"addData.name"}],staticClass:"form-control",attrs:{type:"text",required:"",id:"name",placeholder:"Please enter a file name"},domProps:{value:t.addData.name},on:{input:function(e){e.target.composing||t.$set(t.addData,"name",e.target.value)}}}),t._m(3)]),a("div",{staticClass:"form-group"},[a("label",{attrs:{for:"type"}},[t._v("Type:")]),a("input",{directives:[{name:"model",rawName:"v-model",value:t.addData.type,expression:"addData.type"}],staticClass:"form-control",attrs:{type:"text",required:"",id:"type",placeholder:"Please enter the MIME type"},domProps:{value:t.addData.type},on:{input:function(e){e.target.composing||t.$set(t.addData,"type",e.target.value)}}}),t._m(4)]),a("div",{staticClass:"form-group"},[a("label",{attrs:{for:"content"}},[t._v("Content:")]),a("textarea",{directives:[{name:"model",rawName:"v-model",value:t.addData.content,expression:"addData.content"}],staticClass:"form-control",attrs:{required:"",id:"content",rows:"3",placeholder:"Please enter the file contents"},domProps:{value:t.addData.content},on:{input:function(e){e.target.composing||t.$set(t.addData,"content",e.target.value)}}})])]),a("div",{staticClass:"modal-footer"},[a("button",{staticClass:"btn btn-secondary",attrs:{type:"button"},on:{click:function(e){e.preventDefault(),t.addData.show=!1}}},[t._v("Close")]),a("button",{staticClass:"btn btn-primary",attrs:{type:"submit"}},[t._v("Save")])])])])])]),a("div",{class:{"modal-backdrop":!0,fade:!0,show:t.editFile.show}}),a("div",{class:{modal:!0,fade:!0,show:t.editFile.show},attrs:{id:"modal-edit-file",tabindex:"-1",role:"dialog"}},[a("div",{staticClass:"modal-dialog modal-lg",attrs:{role:"document"}},[a("div",{staticClass:"modal-content"},[a("div",{staticClass:"modal-header"},[a("h5",{staticClass:"modal-title"},[t._v("Edit file")]),a("button",{staticClass:"close",attrs:{type:"button"},on:{click:function(e){e.preventDefault(),t.editFile.show=!1}}},[a("span",[t._v("×")])])]),a("form",{on:{submit:function(e){return e.preventDefault(),t.onEditorFile(e)}}},[a("div",{staticClass:"modal-body"},[a("div",{staticClass:"form-group"},[a("label",{attrs:{for:"name"}},[t._v("Name:")]),a("input",{directives:[{name:"model",rawName:"v-model",value:t.editFile.name,expression:"editFile.name"}],staticClass:"form-control",attrs:{type:"text",required:"",id:"name",placeholder:"Please enter a file name"},domProps:{value:t.editFile.name},on:{input:function(e){e.target.composing||t.$set(t.editFile,"name",e.target.value)}}})]),t.editFile.show&&t.editFile.blob&&t.editFile.type&&"image/"===t.editFile.type.substr(0,6)?a("div",{staticClass:"form-group"},[a("label",[t._v("Image:")]),a("div",{staticClass:"edit-image"},[a("img",{ref:"editImage",attrs:{src:t.editFile.blob}})]),a("div",{staticClass:"edit-image-tool"},[a("div",{staticClass:"btn-group",attrs:{role:"group"}},[a("button",{staticClass:"btn btn-primary",attrs:{type:"button",title:"cropper.rotate(-90)"},on:{click:function(e){t.editFile.cropper.rotate(-90)}}},[a("i",{staticClass:"fa fa-undo",attrs:{"aria-hidden":"true"}})]),a("button",{staticClass:"btn btn-primary",attrs:{type:"button",title:"cropper.rotate(90)"},on:{click:function(e){t.editFile.cropper.rotate(90)}}},[a("i",{staticClass:"fa fa-repeat",attrs:{"aria-hidden":"true"}})])]),a("div",{staticClass:"btn-group",attrs:{role:"group"}},[a("button",{staticClass:"btn btn-primary",attrs:{type:"button",title:"cropper.crop()"},on:{click:function(e){t.editFile.cropper.crop()}}},[a("i",{staticClass:"fa fa-check",attrs:{"aria-hidden":"true"}})]),a("button",{staticClass:"btn btn-primary",attrs:{type:"button",title:"cropper.clear()"},on:{click:function(e){t.editFile.cropper.clear()}}},[a("i",{staticClass:"fa fa-remove",attrs:{"aria-hidden":"true"}})])])])]):t._e()]),a("div",{staticClass:"modal-footer"},[a("button",{staticClass:"btn btn-secondary",attrs:{type:"button"},on:{click:function(e){e.preventDefault(),t.editFile.show=!1}}},[t._v("Close")]),a("button",{staticClass:"btn btn-primary",attrs:{type:"submit"}},[t._v("Save")])])])])])])])},P=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("thead",[a("tr",[a("th",[t._v("#")]),a("th",[t._v("Thumb")]),a("th",[t._v("Name")]),a("th",[t._v("Size")]),a("th",[t._v("Speed")]),a("th",[t._v("Status")]),a("th",[t._v("Action")])])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("td",[a("img",{attrs:{width:"40",height:"auto"}})])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("h4",[t._v("Drop files anywhere to upload\n                  "),a("br"),t._v("or\n                ")])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("small",{staticClass:"form-text text-muted"},[t._v("\n                Such as\n                "),a("code",[t._v("filename.txt")])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("small",{staticClass:"form-text text-muted"},[t._v("\n                Such as\n                "),a("code",[t._v("text/plain")])])}],N=(a("34ef"),a("28a5"),a("6b54"),a("7f7f"),a("c93e")),O=a("b5fc"),z=(a("e9e8"),a("8019")),I=a.n(z),U={components:{FileUpload:I.a},data:function(){return{dataset:null,files:[],dataset_files:[],accept:"image/png,image/gif,image/jpeg,image/webp",extensions:"gif,jpg,jpeg,png,webp",minSize:1024,size:10485760,multiple:!0,directory:!1,drop:!0,dropDirectory:!0,addIndex:!1,thread:3,name:"file",postAction:"/api/datasets/"+this.$route.params.dataset_id+"/upload",putAction:"",headers:{"X-Csrf-Token":"xxxx"},data:{_csrf_token:"xxxxxx"},autoCompress:1048576,uploadAuto:!1,isOption:!1,addData:{show:!1,name:"",type:"",content:""},editFile:{show:!1,name:""}}},watch:{"editFile.show":function(t,e){!t&&e&&this.$refs.upload.update(this.editFile.id,{error:this.editFile.error||""}),t&&this.$nextTick(function(){if(this.$refs.editImage){var t=new O["a"](this.$refs.editImage,{autoCrop:!1});this.editFile=Object(N["a"])({},this.editFile,{cropper:t})}})},"addData.show":function(t){t&&(this.addData.name="",this.addData.type="",this.addData.content="")}},methods:{getDataset:function(){var t=this,e="/api/datasets/"+this.$route.params.dataset_id;F.a.get(e).then(function(e){t.dataset=e.data.dataset,console.log(t.dataset)}).catch(function(t){console.error(t)})},getDatasetFiles:function(){var t=this,e="/api/datasets/"+this.$route.params.dataset_id+"/files";F.a.get(e).then(function(e){t.dataset_files=e.data.dataset_files,console.log(t.dataset_files)}).catch(function(t){console.error(t)})},inputFilter:function(t,e,a){if(t&&!e){if(/(\/|^)(Thumbs\.db|desktop\.ini|\..+)$/.test(t.name))return a();if(/\.(php5?|html?|jsx?)$/i.test(t.name))return a()}if(t&&(!e||t.file!==e.file)){t.blob="";var s=window.URL||window.webkitURL;s&&s.createObjectURL&&(t.blob=s.createObjectURL(t.file)),t.thumb="",t.blob&&"image/"===t.type.substr(0,6)&&(t.thumb=t.blob)}},inputFile:function(t,e){console.log("inputfile"),t&&!e&&console.log("add",t),t&&e&&(t.active&&!e.active&&t.size>=0&&this.minSize>0&&t.size<this.minSize&&this.$refs.upload.update(t,{error:"size"}),t.progress!==e.progress&&console.log("inputfile progress: "+t.progress),t.error&&!e.error&&console.log("inputfile error: "+t.error),t.success&&!e.success&&console.log("inputfile success: "+t.success)),!t&&e&&e.success&&e.response.id,Boolean(t)===Boolean(e)&&e.error===t.error||this.uploadAuto&&!this.$refs.upload.active&&(this.$refs.upload.active=!0)},alert:function(t){function e(e){return t.apply(this,arguments)}return e.toString=function(){return t.toString()},e}(function(t){alert(t)}),onEditFileShow:function(t){this.editFile=Object(N["a"])({},t,{show:!0}),this.$refs.upload.update(t,{error:"edit"})},onEditorFile:function(){if(!this.$refs.upload.features.html5)return this.alert("Your browser does not support"),void(this.editFile.show=!1);var t={name:this.editFile.name};if(this.editFile.cropper){for(var e=atob(this.editFile.cropper.getCroppedCanvas().toDataURL(this.editFile.type).split(",")[1]),a=new Uint8Array(e.length),s=0;s<e.length;s++)a[s]=e.charCodeAt(s);t.file=new File([a],t.name,{type:this.editFile.type}),t.size=t.file.size}this.$refs.upload.update(this.editFile.id,t),this.editFile.error="",this.editFile.show=!1},onAddFolader:function(){var t=this;if(this.alert("on add folder"),this.$refs.upload.features.directory){var e=this.$refs.upload.$el.querySelector("input");e.directory=!0,e.webkitdirectory=!0,this.directory=!0,e.onclick=null,e.click(),e.onclick=function(a){t.directory=!1,e.directory=!1,e.webkitdirectory=!1}}else this.alert("Your browser does not support")},onAddData:function(){if(this.alert("on add data"),this.addData.show=!1,this.$refs.upload.features.html5){var t=new window.File([this.addData.content],this.addData.name,{type:this.addData.type});this.$refs.upload.add(t)}else this.alert("Your browser does not support")}},filters:{formatFileSize:function(t){if(!t)return"";var e="kb";return t/=1e3,t>1e3&&(t/=1e3,e="mb"),t>1e3&&(t/=1e3,e="gb"),t=t.toFixed(2),t+" "+e}},created:function(){this.getDataset(),this.getDatasetFiles()}},T=U,M=(a("41f3"),Object(i["a"])(T,E,P,!1,null,null,null));M.options.__file="Upload.vue";var R=M.exports,q=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"container"},[a("div",{staticClass:"row"},[a("div",{staticClass:"col-sm-10"},[a("h1",[t._v("Datasets")]),a("hr"),a("br"),a("br"),a("button",{directives:[{name:"b-modal",rawName:"v-b-modal.dataset-modal",modifiers:{"dataset-modal":!0}}],staticClass:"btn btn-success btn-sm",attrs:{type:"button"}},[t._v("Add Dataset")]),a("br"),a("br"),a("table",{staticClass:"table table-hover"},[t._m(0),a("tbody",t._l(t.datasets,function(e,s){return a("tr",{key:s},[a("td",[t._v(t._s(e.id))]),a("td",[t._v(t._s(e.name))]),a("td",[t._v(t._s(e.objects))]),a("td",[a("b-button",{staticClass:"btn btn-warning btn-sm",attrs:{type:"button",to:{name:"Upload",params:{dataset_id:e.id}}}},[t._v("Edit\n                ")]),a("button",{staticClass:"btn btn-danger btn-sm",staticStyle:{"margin-left":"0.5rem"},attrs:{type:"button"},on:{click:function(a){t.removeDataset(e.id)}}},[t._v("Delete")])],1)])}))])])]),a("b-modal",{ref:"addDatasetModal",attrs:{id:"dataset-modal",title:"Add a new dataset","hide-footer":""}},[a("b-form",{staticClass:"w-100",on:{submit:t.onSubmit,reset:t.onReset}},[a("b-form-group",{attrs:{id:"form-name-group",label:"Name:","label-for":"form-name-input"}},[a("b-form-input",{attrs:{id:"form-name-input",type:"text",required:"",placeholder:"Enter name"},model:{value:t.addDatasetForm.name,callback:function(e){t.$set(t.addDatasetForm,"name",e)},expression:"addDatasetForm.name"}})],1),a("b-button",{attrs:{type:"submit",variant:"primary"}},[t._v("Submit")]),a("b-button",{attrs:{type:"reset",variant:"danger"}},[t._v("Reset")])],1)],1)],1)},L=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("thead",[a("tr",[a("th",{attrs:{scope:"col"}},[t._v("ID")]),a("th",{attrs:{scope:"col"}},[t._v("Name")]),a("th",{attrs:{scope:"col"}},[t._v("Objects")]),a("th")])])}],B={data:function(){return{datasets:[],addDatasetForm:{id:0,name:"",objects:0}}},methods:{getDatasets:function(){var t=this,e="/api/datasets";F.a.get(e).then(function(e){t.datasets=e.data.datasets,console.log(t.datasets)}).catch(function(t){console.error(t)})},addDataset:function(t){var e=this,a="/api/datasets";F.a.post(a,t).then(function(){e.getDatasets()}).catch(function(t){console.log(t),e.getDatasets()})},removeDataset:function(t){console.log("remove dataset: "+t)},initForm:function(){this.addDatasetForm.id=0,this.addDatasetForm.name="",this.addDatasetForm.objects=0},onSubmit:function(t){t.preventDefault(),this.$refs.addDatasetModal.hide();var e={id:this.addDatasetForm.id,name:this.addDatasetForm.name,objects:this.addDatasetForm.objects};this.addDataset(e),this.initForm()},onReset:function(t){t.preventDefault(),this.$refs.addDatasetModal.hide(),this.initForm()}},created:function(){this.getDatasets()}},H=B,W=Object(i["a"])(H,q,L,!1,null,null,null);W.options.__file="Datasets.vue";var Y=W.exports,J=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"container"},[a("div",{staticClass:"row"},[a("div",{staticClass:"col-sm-10"},[a("h1",[t._v("Projects")]),a("hr"),a("br"),a("br"),a("button",{directives:[{name:"b-modal",rawName:"v-b-modal.dataset-modal",modifiers:{"dataset-modal":!0}}],staticClass:"btn btn-success btn-sm",attrs:{type:"button"}},[t._v("Add Project")]),a("br"),a("br"),a("table",{staticClass:"table table-hover"},[t._m(0),a("tbody",t._l(t.datasets,function(e){return a("tr",{key:e.id},[a("td",[t._v(t._s(e.id))]),a("td",[t._v(t._s(e.name))]),a("td",[t._v(t._s(e.objects))]),a("td",[e.download_running?a("div",{staticStyle:{display:"flex"}},[a("div",{staticClass:"loader"}),a("p",{staticStyle:{width:"10px"}}),a("p",[t._v("Processing...")])]):t._e(),e.download_path&&!e.download_running?a("div",[a("p",[t._v("Download Ready!")])]):t._e()]),a("td",[a("button",{staticClass:"btn btn-primary btn-sm",staticStyle:{"margin-left":"0.5rem"},attrs:{type:"button"},on:{click:function(a){t.processDataset(e)}}},[t._v("Process")]),e.download_path?a("b-button",{staticClass:"btn btn-warning btn-sm",staticStyle:{"margin-left":"0.5rem"},attrs:{type:"button",href:e.download_path}},[t._v("Download")]):t._e()],1)])}))])])]),a("b-modal",{ref:"addDatasetModal",attrs:{id:"dataset-modal",title:"Add a new dataset","hide-footer":""}},[a("b-form",{staticClass:"w-100",on:{submit:t.onSubmit,reset:t.onReset}},[a("b-form-group",{attrs:{id:"form-name-group",label:"Name:","label-for":"form-name-input"}},[a("b-form-input",{attrs:{id:"form-name-input",type:"text",required:"",placeholder:"Enter name"},model:{value:t.addDatasetForm.name,callback:function(e){t.$set(t.addDatasetForm,"name",e)},expression:"addDatasetForm.name"}})],1)],1)],1)],1)},V=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("thead",[a("tr",[a("th",{attrs:{scope:"col"}},[t._v("ID")]),a("th",{attrs:{scope:"col"}},[t._v("Name")]),a("th",{attrs:{scope:"col"}},[t._v("Objects")]),a("th"),a("th")])])}],X={data:function(){return{datasets:[],addDatasetForm:{id:0,name:"",objects:0}}},methods:{getDatasets:function(){var t=this,e="/api/datasets";F.a.get(e).then(function(e){t.datasets=e.data.datasets,console.log(t.datasets)}).catch(function(t){console.error(t)})},addDataset:function(t){var e=this,a="/api/datasets";F.a.post(a,t).then(function(){e.getDatasets()}).catch(function(t){console.log(t),e.getDatasets()})},processDataset:function(t){var e=this,a="/api/datasets/"+t.id+"/process";this.$set(t,"download_complete",!1),this.$set(t,"download_running",!0),F.a.get(a).then(function(a){e.$set(t,"download_complete",!0),e.$set(t,"download_running",!1),console.log("download path: "+a.data.download_path),t.download_path=a.data.download_path})},initForm:function(){this.addDatasetForm.id=0,this.addDatasetForm.name="",this.addDatasetForm.objects=0},onSubmit:function(t){t.preventDefault(),this.$refs.addDatasetModal.hide();var e={id:this.addDatasetForm.id,name:this.addDatasetForm.name,objects:this.addDatasetForm.objects};this.addDataset(e),this.initForm()},onReset:function(t){t.preventDefault(),this.$refs.addDatasetModal.hide(),this.initForm()}},created:function(){this.getDatasets()}},G=X,K=(a("f6ca"),Object(i["a"])(G,J,V,!1,null,null,null));K.options.__file="Projects.vue";var Q=K.exports;s["a"].use(c["a"]);var Z=new c["a"]({mode:"history",base:"/frontend/",routes:[{path:"/",name:"home",component:w},{path:"/tiles",name:"tiles",component:function(){return a.e("tiles").then(a.bind(null,"a15e"))}},{path:"/ping",name:"Ping",component:S},{path:"/datasets",name:"Datasets",component:Y},{path:"/datasets/:dataset_id/upload",name:"Upload",component:R,props:function(t){return{dataset_id:parseInt(t.params.dataset_id)}}},{path:"/projects",name:"Projects",component:Q}]}),tt=(a("f9e3"),a("9f7b"));s["a"].config.productionTip=!1,s["a"].use(tt["a"]),new s["a"]({router:Z,render:function(t){return t(d)}}).$mount("#app")},"8f59":function(t,e,a){},"8f77":function(t,e,a){},b9f2:function(t,e,a){},c21b:function(t,e,a){},cccb:function(t,e,a){"use strict";var s=a("8f59"),o=a.n(s);o.a},cf05:function(t,e,a){t.exports=a.p+"static/img/logo.82b9c7a5.png"},e918:function(t,e,a){},f6ca:function(t,e,a){"use strict";var s=a("b9f2"),o=a.n(s);o.a}});
//# sourceMappingURL=app.2ac1fd0e.js.map