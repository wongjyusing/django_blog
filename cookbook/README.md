# 简介
本书是关于使用Django2.1搭建博客的流程。  
# 关于gitbook的使用。  
## 安装node.js  
由于在winddows上比在linux上容易多了。  
所以下面讲一下在linux下如何安装node.js  
```linux
sudo mkdir /usr/local/lib/nodejs

# 把终端切换到Download或下载 目录中  
wget https://nodejs.org/dist/v8.11.4/node-v8.11.4-linux-x64.tar.xz

sudo tar -xJvf node-v8.11.4-linux-x64.tar.xz -C /usr/local/lib/nodejs

sudo mv /usr/local/lib/nodejs/node-v8.11.4-linux-x64 /usr/local/lib/nodejs/node-v8  

sudo vim ~/.profile

```  
新建的`.profile`文件后写入如下内容。  
```
# Nodejs
export NODEJS_HOME=/usr/local/lib/nodejs/node-v8/bin
export PATH=$NODEJS_HOME:$PATH
```
刷新资料  
`. ~/.profile`  
等待安装完成后，使用`node -v`，检查是否成功。  
## 安装gitbook  
`npm install -g gitbook-cli`  
## 使用gitbok  
结合这个库来说。  
在**cookbook**下执行以下代码。  
`gitbook serve`  
打开浏览器，输入`http://localhost:4000`  
即可浏览本教程。
