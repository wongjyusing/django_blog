## 前端设计  
在原有博客的样式基础上：
- 修改好之前的色号，
- 正文中的上一页和下一页。之前忘记写上去了
- 之前右边的目录位置和文字位置做一些调整。  
- 学习更多的知识，让页面拥有多种主题。  

## 前端文件生成  
```linux
mkdir static

mkdir static/js

mkdir static/css

mkdir static/img

touch static/js/vue-v2.js

touch front_end/index/templates/index.html
```  
## 关于Vue.js  
首先，感谢鱼C论坛的**鹰搏空**鱼油。告诉了我怎么改写vue.js的模板语法。  
之前查了好久都没有办法在python的web框架上使用Vue.js。  
注意是python的web框架哦，Tornado、Django、Flask都不行。  
现在这个方法如下：  
```javascript
new Vue({
  delimiters: ['${', '}']
})
```
引起冲突的原因是Django、Tornado、Flask、Vue.js。  
它们都是使用 `{{ xxxx }}`来匹配内容的。  
而我们在使用python的web框架。  
返回**html**文件时会检查该文件代码中的`{{ xxxx }}`，然后会检查返回的数据中否存在xxxx这个变量名。  
存在，则成功。  
不存在就会报错。导致整个系统崩溃。  
### index.html
```html
<!DOCTYPE html>
<html lang="zh-CN" dir="ltr">
    <head>
        <meta charset="utf-8">
        <script src="/static/js/vue-v2.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/axios/0.18.0/axios.js"></script>
        <title>首页</title>
    </head>
    <body>
        <header class="site-header">
            <div id="site-branding">
                <h1><a href="#">阿星的博客</a></h1>
                <div class="site-introduction">这是我用Django2.1和Vue.js搭建的博客</div>
            </div>
            <div id="site-navigation">
                <ul>
                    <li ><a href="#">首页</a></li>
                    <li ><a href="/blog/">博客列表</a></li>
                    <li ><a href="/blog/tag_list/"> 标签</a></li>
                    <li><a href="#">学习笔记</a></li>
                    <li ><a href="/about/">关于</a></li>
                </ul>
            </div>
        </header>
        <div id="chapter-list">
            <ul id="app2">
                <li v-for="item in info">

                    <a v-bind:href="item.fields.slug">${ item.fields.name }</a>
                </li>
            </ul>
        </div>
        <footer></footer>



    </body>
    <script>
    <!--基础的样式设计-->

    <!--书本的数据获取-->
    var book = new Vue({
    delimiters: ['${', '}'],
      el: '#app2',
      data () {
        return {
          info: ''
        }
      },
      mounted () {
        //Vue.prototype.$axios = axios,
        axios
          .get('http://127.0.0.1:8000/api_chapter/django/')
          .then(response => (this.info = response.data.books))
      }
    })




    </script>
</html>
```
