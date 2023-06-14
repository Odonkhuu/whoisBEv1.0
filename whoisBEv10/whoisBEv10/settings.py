
from pathlib import Path
import os


# nemelt importuud 
import hashlib
import base64
import random
from django.urls import resolve, get_resolver, URLResolver, URLPattern
###############################
BASE_DIR = Path(__file__).resolve().parent.parent
t = os.path.join(BASE_DIR, 'templates')
SECRET_KEY = 'django-insecure-#_966zao2el-7c%hqh=85b*on!y=p*6c^tr8*oo$-akm8my%+4'

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "*", "202.131.254.138", "192.168.0.15"]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app1',
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

ROOT_URLCONF = 'whoisBEv10.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [t,],
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

WSGI_APPLICATION = 'whoisBEv10.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ------------ start Bidnii nemsen tohiruulguud
# ... existing code ...
pgDbName = "dbwhois"
pgUser = "uwhois"
pgHost = "202.131.254.138"
pgPassword = "whoispass"
pgPort = "5938"

# ... existing code ...

# ------------ end Bidnii nemsen tohiruulguud

# bidnii nemsen function


## Нууц үгийг md5 хашруу хөрвүүлж байгаа
def mandakhHash(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()
#   mandakhHash

## Бүртгүүлэхэд автоматаар үүсэх 5 оронтой код
def createPassword(length):
    # Random string of length 5
    result_str = ''.join((random.choice('abcdefghjkmnpqrstuvwxyz123456789$!?') for i in range(length)))
    return result_str
    # Output example: ryxay
#   createPassword

## Хэрэглэгчийн бүртгэл баталгаажуулах код үүсгэнэ. 
## 30 тэмдэгт байгаа. 
## length нь үсгийн урт
def createCodes(length):
    # Random string of length 30
    result_str = ''.join((random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(length)))
    return result_str
    # Output example: ryxay
#   createCodes

def base64encode(length):
    return str(base64.b64encode((createCodes(length-26) + str(datetime.now().time())).encode('ascii'))).replace('\'','').replace('"','').replace('=','')
#   base64encode

def get_view_name_by_path(path):
    result = resolve(path=path)
    return result.view_name
#   get_view_name_by_path

def pth(request):
    return get_view_name_by_path(request.path)
#   pth

def reqValidation(json,keys):
    validReq = True
    for key in keys:
        if(key not in json):
            validReq = False
            break
    return validReq
#   def


