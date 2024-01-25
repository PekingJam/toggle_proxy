#### 简介

* 主要用于一键开关系统代理，针对使用clash、mihomo、singbox内核+webui的用户开发。

* 默认的webui地址为[http://127.0.0.1:9090/ui/#/proxies](http://127.0.0.1:9090/ui/#/proxies)，如果你的后端地址不是这个请修改源码然后打包后替换程序即可
* 压缩包里包含一键启动脚本和所需的图片资源

#### 环境

* Python 3.10.11 
* pystary 0.10.5
* pyinstaller 6.3.0

#### 使用教程

1. 解压全部文件到一个目录
2. 更改`start.vbs`中的路径为解压后程序的*完整路径*
3. 双击start.vbs 启动！

#### 自行打包

1. 安装依赖

   ```shell
   pip install -r requirements.txt
   ```

2. 修改代码中的后端地址

3. 打包，打包后的程序在`dist`目录中

   ```shell
   pyinstaller -F .\main.py -i .\blue.png
   ```

