Hệ thống yêu cầu:
- Cài git
- Cài python, MySql
- Cài framework Django

Hướng dẫn cài đặt:

checkout code:

git clone git@github.com:dgthien/appdjango.git


Chỉnh sửa cấu hình trong file setting.py

/application/settings.py

Tạo database 'application' trong MySql

Cấu hình Databases (current is MySQL):

'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'application',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }

Start server

python manage.py syncdb
python manage.py runserver 8000

Frontend
http://localhost:8000/polls

Backend
http://localhost:8000/admin

Cấu hình Storage config:

AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
