# 这里不包含环境配置和部署。

你可以使用我提供的一键包,如果觉得部署太麻烦或者困难。    

一键包的使用方法，解压到你喜欢的位置，然后双击`0.后端_使用local_deeplx.bat`,再双击`1.前端.bat`。

然后前端显示的local端口即可。  

![image-20240914154851811](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/24/09/202409141549574.png)

【如果你是L站用户，可以选择到key.yml中填一下api-key，然后用另一个后端即可。】

# 书架页面的使用：

## 书籍导入

![image-20240914145656646](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/24/09/202409141549708.png)

目前支持txt和epub，如果你试图导入pdf或者其他，应该会收到这样的消息:

![image-20240914150357136](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/24/09/202409141549538.png)

## 书籍存储和查找：

之后，点击书籍封面就可以进入阅读。书籍是长时间存储的，位置位于`.\books`。

如果你的书籍很多，而找不到想要的书籍，可以试一下ctrl+f，用网页端自带的查找匹配：

![image-20240914150652332](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/24/09/202409141549732.png)



# Ebook页面的使用:

## 加载：

对于epub，每次加载会先解析成txt，如果你的epub非常大，可能会卡一会儿，400kb在我的笔记本没有上电的情况下大概要0.2s，如果你非常硬核，要在树莓派或者单片机上面跑，那可能需要头疼一下。

## 划词翻译和划线翻译。

这个划和复制粘贴时候的划是一样的，你看到它变成蓝色的，那就说明划线成功了，松开等待一下可以看到右上角弹出的窗口。



**对于单词，可以双击**

![image-20240914151436515](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/24/09/202409141549515.png)

对于句子，就只能拖动鼠标了。

![image-20240914151605589](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/24/09/202409141549606.png)

## 保存单词和句子的选项:

你可以保存，然后进入`./data/`查看你保存的单词。

目前单词乱序复习和句子记录再查看的软件还没写，应该会和这个项目剥离。因为并不是每个人都有提高词汇量的需求。但我是需要的（2500词汇量=-=。）

![image-20240914151835097](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/24/09/202409141549915.png)

![image-20240914151936696](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/24/09/202409141550563.png)

![image-20240914151953146](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/24/09/202409141550252.png)

![image-20240914152004953](https://fastly.jsdelivr.net/gh/MrXnneHang/blog_img/BlogHosting/img/24/09/202409141550472.png)

说起来单词创建和单词词性词意是分开的，为了之后向sql扩展。大概模拟成数据库表的格式。

**尽量不要手动修改保存的三个文件！！！**