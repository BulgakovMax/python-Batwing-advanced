 pip install django
 django-admin startproject name_project

 python manage.py startproject name_project
 python manage.py startapp name_app
 python manage.py migrate
 python manage.py createsuperuser

 python manage.py makemigrations
 python manage.py migrate
 python manage.py migrate AppName zero  # скидання міграцій до 0
 python manage.py migrate AppName 0008


 #input in working project
 docker-compose exec web bash

 # input to database
 docker-compose exec db bash
 mysql -u root -p
 'enter password: "22082003"'

 # SQL command:
 SHOW DATABASES;
 USE django;
 SHOW TABLES;
 SHOW COLUMNS FROM ***;
 
 
 Далее необходимо изменить владельца папки, т.к. контейнер запускается как root пользователь.


sudo chown -R $USER:$USER name

 or
chmod -R 0777 * 
 


