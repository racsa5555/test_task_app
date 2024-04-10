# Тестовое задание


### 1. Склоньте репозиторий
Git clone `https://github.com/racsa5555/test_task_app.git (или ssh ссылка)`
### 2. Создайте в postgresql базу данных
`psql -U <user>`
`CREATE DATABASE <database_name>`
### 3. Создайте виртуальное окружение в директории test_task_app
`python3 -m venv venv`
### 4. Активируйте его 
`. venv/bin/activate`
### 5. Установите необходимые зависимости 
`pip install -r requirements.txt`
### 6. Создайте .env файл
`nano .env`


Пример файла:


DB_NAME= ...


DB_HOST=localhost


DB_PORT=5432


DB_USER=...


DB_PASS=...


### 7. Проведите миграции
`python3 manage.py makemigrations`
`python3 maange.py migrate`


### 8. Запустите Сервер
`python3 manage.py runserver`

