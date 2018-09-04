"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# 在项目中创建你的路径，像右边这样 os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# 快速启动项目设置不适合于生产，更多设置可浏览下方网页
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 安全密钥，不要让别人人知道
SECRET_KEY = 'o4-gadagh_)f*yoacxwog9d#!zb9e8ugj06%pahg4!tdxo)*^%'

# SECURITY WARNING: don't run with debug turned on in production!
# 不要在生产环境打开Debug模式
DEBUG = True

# 允许的端口，里面填写的内容，在部署的时候会用到
ALLOWED_HOSTS = []


# Application definition
# 定义应用的地方
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# 中间件
MIDDLEWARE = [
    # 安全中间件
    'django.middleware.security.SecurityMiddleware',
    # 会话中间件
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 共同的中间件
    'django.middleware.common.CommonMiddleware',
    # 防止跨域请求攻击的中间件
    'django.middleware.csrf.CsrfViewMiddleware',
    # 验证的中间件
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 消息的中间件
    'django.contrib.messages.middleware.MessageMiddleware',
    # 防止点击劫持的中间件
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 主要路由配置，这里默认是在mysite中的urls.py文件
ROOT_URLCONF = 'mysite.urls'

# 模板 注意这里有更改的地方
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 下面的DIR添加  os.path.join(BASE_DIR, 'templates')
        # 这里是项目寻找模板文件目录的配置很重要
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # APP_DIRS这里是  是否到应用目录中寻找模板目录，后期会用到，必须开启
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# 接口规范应用
WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# 数据库 开发环境使用sqlite3即可，
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# 密码验证器
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
#
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# 国际化 这里有很多修改，可以直接复制粘贴即可
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'  # 有修改，zh-hans 简体中文

TIME_ZONE = 'Asia/Shanghai' # 有修改 设置时区 亚洲/上海

USE_I18N = True

USE_L10N = True

USE_TZ = False          #关闭国际时间


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
# 静态文件配置路径  有修改  后期部署环节需要删掉
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]