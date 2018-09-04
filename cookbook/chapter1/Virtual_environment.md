## 准备工作
请确保项目是在虚拟环境中运行。
这里使用的是virtualenv来创建python虚拟环境  
如果你会使用和创建虚拟环境，可以跳过本节内容。
### 安装virtualenv  
如果安装了virtualenv可以跳过。  
`sudo apt-get install python-virtualenv`  
上面代码不需要指定python版本。  
### 创建虚拟环境
请找到你的python3安装路径的路径。  
linux的python3路径一般在**/usr/bin/python3**  
最好是专门创建一个目录来存放虚拟环境的文件。  
这里我们选择和django项目同级吧，方便我们调用。  
首先，确定你的项目要放在哪里。例如我要放在桌面。  
在桌面新建一个目录，例如：work_space。  
然后进入该目录。  
在终端输入`virtualenv -p /usr/bin/python3 venv`  
注意，终端的操作路径是在work_space目录下，不是在根目录下。  
这时，可以看到work_space目录中多了一个venv的目录。  
这就是我们的虚拟环境文件目录。  
### 进入和退出虚拟环境
在终端输入`source /home/username/Desktop/work_space/venv/bin/activate`  
请把上面的路径替换成你虚拟环境目录的路径。  
不知道的可以手动点开venv然后点开bin后，按下`Ctrl`和`L`来查看虚拟环境的路径  
记得在后面加上activate。  
成功后会发现你的终端命令提示符会多了(venv)  
如果需要退出虚拟环境，在终端输入`deactivate`即可。
