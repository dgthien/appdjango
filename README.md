Huong dan cai dat:

Chay lenh checkout code:

git clone git@github.com:dgthien/appdjango.git


He thong yeu cau:
- Cai python
- Cai framework Django

Chinh sua cac cau hinh trong file setting.py

/application/settings.py

Tao database application trong MySql

Cau hinh Databases (current is MySQL):

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

Storage config:

AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
