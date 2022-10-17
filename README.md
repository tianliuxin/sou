# sou的作用
sou主要是为了命令行搜索而实现的,实现的原理是借助本地的搜索软件去打开指定的链接或者搜索指定的内容

# sou的安装
下载源码包进行`pip install 源码包名`,或者使用`python setup.py install`去安装

# sou的用法
若是win系统并具有edge浏览器,则无需配置,开箱即用

若想添加软件和搜索引擎,可以在sou安装的地方打开config.py,在里面配置搜索软件的位置和你需要的搜索引擎即可!  

```bash

sou -h # 查看帮助
sou hello,world # 搜索hello,world
sou -l www.baidu.com # 打开百度
sou -a google -e github nlp # 使用google在github上搜索nlp
sou hello world # 会分别搜索hello和world,若想作为一个整体可以使用sou "hello world"

```

# 待办
后面可能改变配置的方式,比如配置文件的修改或者使用命令配置等