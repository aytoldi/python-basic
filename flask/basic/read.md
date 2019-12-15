2、把Python安装文件夹下的Scripts文件夹添加到Path环境变量里，这样 easy_install 命令和其它 Python 脚本就加入到了命令行自动搜索的路径。步骤：右键点击计算机>选择属性>选择“高级系统设置”>点击最下面的“环境变量”>“系统变量”中找到“PATH”>双击进入Path变量编辑>输入Scripts文件路径

这次路径如下：;D:\Python\Scripts        示例图如下：

3、打开cmd ，输入命令：easy_install virtualenv（目录文件下）

4、继续输入命令：easy_install pip

5、继续输入命令：pip install virtualenv

二、创建环境

1、virtualenv 安装完后，创建自己的环境。创建一个项目文件夹，并在其下创建一个 venv 文件夹，依次输入的语句：

mkdir myproject（创建文件夹，文件夹名字自定义）

cd myproject（进入文件目录）

virtualenv venv（创建venv文件）

2、现在，无论何时想在某个项目上工作，只需要激活相应的环境。Windows下执行语句为：venv\scripts\activate

3、现在已经激活了virtualenv（shell 提示符显示的是当前环境）。

现在只需要输入命令来激活 virtualenv 中的 Flask

输入语句：pip install Flask