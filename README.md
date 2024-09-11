## 这是什么：

这是一个由vue构建的网页端txt阅读器。

![image-20240911135426651](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/24/09/202409111359874.png)

![image-20240911135930298](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/24/09/202409111359418.png)

目前支持上传文件并且显示。



## 待开发：

* [ ] 书架功能和书籍暂存
* [ ] 显示当前在第几页
* [ ] 给出一个99.46%这样的阅读进度
* [ ] 自定义每页的最大行数，每行字符数，以及字符大小。
* [ ] 单词高亮和选中返回
* [ ] 划线高亮和返回



## 如何使用：

你需要自行安装和配置[nvm](https://github.com/nvm-sh/nvm)

```cmd
nvm use 18
cd ./view
npm install 
npm run serve
```

然后，你应该可以在访问:[127.0.0.1:8080](127.0.0.1:8080)来访问前端。



## 如何修改代码：

目前所有页面代码逻辑都在./view/src/App.vue中，可以自行修改。
