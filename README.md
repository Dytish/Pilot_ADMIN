# Pilot_ADMIN

установка окружения
```bash
python -m venv venv
```

# Установка библиотек

Установите необходимые библиотеки из файла requirements.txt если запускаете локально:
```bash
pip install -r requirements.txt
```

# Проверка Docker

Убедитесь, что Docker установлен и запущен:
проверка установлен и запущен ли докер

```bash
sudo systemctl status docker

```

Если Docker не запущен, используйте:
```bash
sudo systemctl start docker
```

# Запуск Docker

Для запуска приложения в Docker в режиме демона:
```bash
sudo docker-compose up --build -d
```
Для запуска Docker без демона (с выводом логов):
```bash
sudo docker-compose up --build
```


# Внесение изменений в базу данных

Сделайте миграции после внесения изменений в модели:
```bash
python manage.py makemigrations
python manage.py migrate
```


Запуск приложения

Для запуска только админки локально:
```bash
python manage.py runserver
```

Для запуска на определенном порту (например, на 8080) и доступе по IP:
```bash
python manage.py runserver 0.0.0.0:8080
```


# создание суперпользователя
```bash
python manage.py createsuperuser 
```


# создание пользователя для взаимедействия с админкой и ограниченными правами 
```bash
python manage.py create_initial_user
```


# заполнение городов
```bash
python manage.py populate_tables
```



```bash
docker exec -it django_container python manage.py migrate
```
