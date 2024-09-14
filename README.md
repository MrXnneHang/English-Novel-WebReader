## 这是什么：

这是一个由vue构建的网页端txt阅读器，个人用来阅读英语原版书籍，目前支持单词查询，记录,支持长句翻译。

### 书架和书籍上传:

![image-20240913132735372](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/24/09/202409131327598.png)

### 单词查询和保存

![image-20240912163001490](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/24/09/202409121630112.png)

### 词组查询和保存

 ![image-20240912162929020](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/24/09/202409121629345.png)

### 长句翻译和记录：

![image-20240913133357354](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/24/09/202409131334335.png)



## 待开发：

* [x] 书架功能和书籍暂存
* [x] 显示当前在第几页
* [x] 快速前往指定页
* [x] 显示总页数
* [x] 给出一个99.46%这样的阅读进度
* [x] 自定义每页的最大行数，每行字符数，以及字符大小。
* [x] 选中返回
* [ ] 单词，句子复习



## 如何部署启动：

### 前端: 

你需要自行安装和配置nvm   
[linux nvm](https://github.com/nvm-sh/nvm)    
[windows nvm](https://github.com/coreybutler/nvm-windows/releases)   


```cmd
nvm use 18
cd ./view
npm install 
npm run serve -- --port 8081
```

然后，你应该可以在访问:[127.0.0.1:8081](127.0.0.1:8081)来访问前端。

### 后端:

python环境:
```
python -m pip install -r requirements.txt
```
之后有两种方法。   

**common:**    

你需要    
[chrome driver和chrome test](https://googlechromelabs.github.io/chrome-for-testing/)，注意两者版本的对应。    
[deeplx-local](https://github.com/ycvk/deeplx-local/releases/tag/v0.2.4),我用的是`deeplx-v0.2.4-windows-amd64.zip`    
你需要核对路径，在config.yml中核对chrome的路径，在deeplx-local.ps1中核对deeplx.exe的路径。
```cmd
powershell -ExecutionPolicy Bypass -File ".\deeplx-local.ps1"
python run.py
```

**specially:**    

如果你是linux.do的用户，你可以创建`./key.yml`,写入:  
```yaml
deeplx:your_api_key   
```
这个key可以再connect处获取。然后运行:
```cmd
python run.py --use_api_key
```





## 如何使用：

参见[English-Novel-WebReader使用手册](./English-Novel-WebReader使用手册.md)
