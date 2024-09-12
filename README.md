## 这是什么：

这是一个由vue构建的网页端txt阅读器，个人用来阅读英语原版书籍，目前支持单词查询，记录。后续会支持长句翻译，长句记录等等。

![image-20240912150357298](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/24/09/202409121507028.png) 

目前支持上传文件并且显示。



## 待开发：

* [ ] 书架功能和书籍暂存
* [x] 显示当前在第几页
* [x] 快速前往指定页
* [x] 显示总页数
* [x] 给出一个99.46%这样的阅读进度
* [ ] 自定义每页的最大行数，每行字符数，以及字符大小。
* [x] 选中返回



## 如何使用：

### 前端: 

你需要自行安装和配置[nvm](https://github.com/nvm-sh/nvm)

```cmd
nvm use 18
cd ./view
npm install 
npm run serve
```
修改后端端口: 根据你`./run.py`指定的端口，修改以下文件「没有更改的情况下，默认为5000」:
`./view/src/App.vue`:
```vue
http://localhost:5000/api/selected-word'
```
`./view/src/utils/axios.js`:
```cmd
axios.defaults.baseURL = 'http://127.0.0.1:5000';
```
你可以通过查找来定位，并且修改5000为你的后端端口。


然后，你应该可以在访问:[127.0.0.1:8080](127.0.0.1:8080)来访问前端。

### 后端:

如果要完成查单词的功能，需要一些前置。  
具体参考:[free-EN2CN-dictionary](https://github.com/MrXnneHang/free-EN2CN-dictionary)的环境部署。  


## 如何修改代码：

目前代码主要写在`./view/src/`,`./api.py`中。