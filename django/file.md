##创建django项目
使用 django-admin 来创建 test 项目：
######     django-admin startproject test1

####进入项目 , 启动项目
######  D:\project\python\python-basic\django>cd test1
######  D:\project\python\python-basic\django\test1>python manage.py runserver

#创建独立模块
####创建用户登录模块
D:\project\python\python-basic\django\test1>
######  python manage.py startapp booktest


##########
GET请求
###### http://imooc.com?title=java$category=3
###### 可以用浏览器直接访问
###### 请求可以携带参数，但是有长度限制
######  请求参数直接放在url后面, REQUEST URL: http://imooc.com?title=java$category=3


# 生成迁移文件
python manage.py makemigrations
# 执行迁移命令
python manage.py migrate
# 启动服务
python manage.py runserver


##########
POST请求

"""
    安装模块 
    pip3 install pymysql
    pip3 install django

"""


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test1',#mysql 数据库名称
        'USER':'root', #用户名
        'PASSWORD':'root',#密码
        'HOST':'127.0.0.1',#host
        'PORT':'3303',#端口号
    }
}


STATIC_URL = '/static/' #调用时目录
STATICFILES_DIRS=[
 os.path.join(BASE_DIR,"static"), #具体路径
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "booktest"#配置自定义模块
]