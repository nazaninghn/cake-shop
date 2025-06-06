"""
Django settings for zarineh project.

Generated by 'django-admin startproject' using Django 5.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path
import environ
import os

# ایجاد محیط
env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env()

# مسیر اصلی پروژه
BASE_DIR = Path(__file__).resolve().parent.parent

# کلید مخفی و تنظیمات دیباگ
SECRET_KEY = env("SECRET_KEY", default="django-insecure-key")
DEBUG = env.bool("DEBUG", default=True)
ALLOWED_HOSTS = ["*"]  # برای دیپلوی بهتره دامین خاص رو بزنی

# اپلیکیشن‌ها
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

# میدلورها
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # برای سرویس‌دهی فایل‌های استاتیک در تولید
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL‌ها
ROOT_URLCONF = 'zarineh.urls'

# قالب‌ها
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'core/templates'],
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

# WSGI
WSGI_APPLICATION = 'zarineh.wsgi.application'  # ← اینجا اشتباه تایپی بود، اصلاح شد

# دیتابیس (لوکال SQLite، در تولید بهتره PostgreSQL باشه)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# اعتبارسنجی رمز عبور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# تنظیمات زبان و زمان
LANGUAGE_CODE = 'fa'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_TZ = True

# فایل‌های استاتیک
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "core/static"]
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# کلید پیش‌فرض پایگاه داده
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
