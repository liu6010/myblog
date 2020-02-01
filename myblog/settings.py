"""
Django settings for myblog project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...) 项目路径
#	os.path.abspath(__file__)获取绝对路径 如F:\Course\Django\path.py
#	os.path.dirname(os.path.abspath(__file__))获取绝对路径脚本文件前的目录，如F:\Course\Django
#	BASE_DIR的路径再取前一个目录，即F:\Course，在此项目中BASE_DIR=~/myblog（第一个mybolg）
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!  密钥配置
SECRET_KEY = '__k4dd$wg=rthrn1bp7iu$h=1u8*!5@-kbd7-7av*%m0731-*a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #

ALLOWED_HOSTS = ['*',] #域名访问权限，如果允许所有域名访问，可设置ALLOWED_HOSTS = ['*',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',	#内置后台管理系统
    'django.contrib.auth',		#内置的用户认证系统
    'django.contrib.contenttypes',	#记录项目中所有的model元数据(Django的orm框架)
    'django.contrib.sessions',		#会话功能，用于标识当前访问网站的用户身份，记录相关的用户信息
    'django.contrib.messages',		#消息提示功能
    'django.contrib.staticfiles',	#查找静态资源路径
	'mainsite',						#项目创建的mainsite app
	'markdown_deux',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'myblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-Hans' #2.0改版后zh_Hans改为zh-Hans

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[
	os.path.join(BASE_DIR,'static'),
]