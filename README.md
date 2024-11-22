# Pilot_ADMIN

установка окружения
python -m venv venv

установка библиотек


проверка установлен и запущен ли докер


запуск докера в демоне
sudo docker-compose up --build -d
запуск докера без демона
sudo docker-compose up --build


внесение изменения
python manage.py makemigrations
python manage.py migrate


запуск отдельно админки
python manage.py runserver
python manage.py runserver 0.0.0.0:8080

создание суперпользователя
python manage.py createsuperuser 

????создание пользователя для взаимедействия с админкой и ограниченными правами 
python manage.py create_initial_user

python manage.py populate_tables


<!-- перевод 
python manage.py makemessages -l ruo
python manage.py compilemessages -->


docker compose exec django python manage.py makemigrations
docker compose exec django python manage.py migrate
docker compose exec django python manage.py populate_tables

docker compose exec django logs