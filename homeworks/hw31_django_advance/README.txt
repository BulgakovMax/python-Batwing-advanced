
 How to work with app
 In terminal on root directory
1. docker-compose up --build
 in new terminal screen
2. docker-compose exec web bash
3. sudo chmod -R 777 *
3. python manage.py migrate
4. python manage.py createsuperuser
5. python manage.py loaddata seed/auth.json
6. python manage.py loaddata seed/main.json
7. python manage.py loaddata seed/product.json


 How to dump data to seed
1. docker-compose exec web bash
2. sudo chmod -R 777 *
3. python manage.py dumpdata auth --indent 4 > seed/auth.json
4. python manage.py dumpdata main --indent 4 > seed/main.json
5. python manage.py dumpdata product --indent 4 > seed/product.json