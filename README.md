一、设计初心：
自动数据收集、报告、接收、审批、更新和展示，搭建一个基础的面向运维的主机管理平台。
二、项目需求分析：
尽可能存储所有的IT资产数据，但不包括外设、U盘、显示器这种属于行政部门管理的设备；
硬件信息可自动收集、报告、分析、存储和展示；
具有后台管理人员的工作界面；
具有前端可视化展示的界面；
具有日志记录功能；
具有注册登录功能；
具有用户管理、权限管理功能；
数据可手动添加、修改和删除。
......
三、资产分类分析：
详见classify
四、具体实现：
环境：Ubuntu16.04+python3.5+django1.11+mysql
1、创建django项目及app
django-admin startproject django_project_name
在项目文件夹下：python manage.py startapp app_name
将app注册到项目中：
INSTALLED_APPS = [
	...
        'app_name',
]
2、配置数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysql_name',
	'HOST': '127.0.0.1',
	'PORT': 3306,
	'USER': 'root',
	'PASSWORD': 'mysql',
	'CHARSET': 'utf8',
    }
}
3、settings中添加xadmin插件作为后台管理
xadmin
# 引入自创建的Sources Roots目录
sys.path.insert(0, os.path.join(BASE_DIR, 'extapps'))
INSTALLED_APPS = [
	...
        'xadmin',
]
更改url中admin的引入：import xadmin as admin
数据迁移：生成迁移表---python manage.py makemigrations
	 迁移到数据库---python manage.py migrate
xadmin和django自带的用户管理系统使用方法相同，只是导包的路径不同
4、分析数据结构之间的关系，创建模型类
详见myapps--->assetsapp--->model.py
注意各表之间的关系，以及各种产品之间的关系，数据迁移
5、客户端收集数据脚本
创建一个Client文件夹，作为客户端的根目录。在Client下，创建下列包。注意是包，不是文件夹：
    bin是客户端启动脚本的所在目录
    conf是配置文件目录
    core是核心代码目录
    log是日志文件保存目录
    plugins是插件或工具目录
6、Linux系统数据收集和Windows系统数据收集（设计细节详见collection）
Linux：使用subprocess.Popen()实现Linux命令执行，收集系统信息
Windows：windows中没有方便的命令可以获取硬件信息，但是有额外的模块可以帮助我们实现目的，这个模块叫做wmi。可以使用pip install wmi的方式安装。但是wmi安装后，import wmi依然会出错，因为它依赖一个叫做win32com的模块。
我们依然可以通过pip install pypiwin32来安装win32com模块，可能些机器无法通过pip成功安装。所以，这里我在github中提供了一个手动安装包pywin32-220.win-amd64-py3.5(配合wmi模块，获取主机信息的模块).exe，方便大家。
使用方法：进入bin目录，运行“python3 main.py report_data”收集硬件信息并汇报；“python3 main.py collect_data”收集硬件信息
7、前前端页面展示及视图
前段页面展示使用AdminLTE，它托管在GitHub上，可以通过下面的地址下载：https://github.com/almasaeed2010/AdminLTE/releases，AdminLTE自带JQuery和Bootstrap3框架，无需另外下载。AdminLTE自带多种配色皮肤，可根据需要实时调整。AdminLTE是移动端自适应的，无需单独考虑。AdminLTE自带大量插件，比如表格、Charts等等，可根据需要载入。将AdminLTE源文件包里的bootstrap、dist和plugins三个文件夹，全部拷贝到 static目录中，在settings中添加配置:
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
前端页面就是各种挖坑，填坑操作，详见templates文件夹
8、注册登录
