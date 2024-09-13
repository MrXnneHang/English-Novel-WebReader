## 这是什么：

这是一个由vue构建的网页端txt阅读器，个人用来阅读英语原版书籍，目前支持单词查询，记录,支持长句翻译。

### 书架和书籍上传:

![image-20240913132735372](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/24/09/202409131327598.png)

### 单词查询和保存

![image-20240912163001490](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/24/09/202409121630112.png)

### 词组查询和保存

 ![image-20240912162929020](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/24/09/202409121629345.png)

### 长句翻译：

![image-20240912173949234](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/24/09/202409121739709.png)



## 待开发：

* [x] 书架功能和书籍暂存
* [x] 显示当前在第几页
* [x] 快速前往指定页
* [x] 显示总页数
* [x] 给出一个99.46%这样的阅读进度
* [x] 自定义每页的最大行数，每行字符数，以及字符大小。
* [x] 选中返回
* [ ] 单词，句子复习



## 如何使用：

### 前端: 

你需要自行安装和配置[nvm](https://github.com/nvm-sh/nvm)

```cmd
nvm use 18
cd ./view
npm install 
npm run serve
```

然后，你应该可以在访问:[127.0.0.1:8080](127.0.0.1:8080)来访问前端。

### 后端:

如果要完成查单词的功能，需要一些前置。
具体参考:[free-EN2CN-dictionary](https://github.com/MrXnneHang/free-EN2CN-dictionary)的环境部署。  

注意先查看`config.yml`中的chrome-driver,chrome路径是否正确。

然后创建`./key.yml`

内容:

```yaml
deeplx: your_api_key
```

这个L站有提供，在connect里可以看到。如果没有L站账户，可以等待后续本地运行deeplx的服务的版本。

```cmd
python -m pip install -r requirements.txt
python run.py
```



