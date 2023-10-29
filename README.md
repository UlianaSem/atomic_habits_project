# Atomic habits project

## Описание проекта

В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек

В рамках проекта реализована бэкенд-часть SPA веб-приложения. 

## Технологии

- Linux
- Python
- Poetry
- Django
- DRF
- PostgreSQL
- Redis
- Celery

## Зависимости

Зависимости, необходимые для работы проекта, указаны в файле pyproject.toml.
Чтобы установить зависимости, используйте команду `poetry install`

## Документация

Документация находится по ссылкам:
1. Для загрузки schema.yaml `api/schema/`
2. Swagger `api/schema/swagger-ui`
3. Redoc `api/schema/redoc/`

## Как запустить проект

Для запуска проекта необходимо выполнить следующие шаги:
1. При необходимости установите Redis на компьютер командой `sudo apt install redis`
2. Cклонируйте репозиторий себе на компьютер
3. Установите необходимые зависимости командой `poetry install`
4. Создайте БД
5. Создайте файл .env и заполните его, используя образец из файла .env.example
6. Выполните миграции командой `python manage.py migrate`
7. Заполните местоположение по умолчанию командой `python manage.py fill_location`
8. Запустите Celery worker командой `celery -A config worker --loglevel=info`
9. Как отдельный процесс запустите Celery beat командой `celery -A config beat --loglevel=info`

## Файл .env.example

1. `DATABASES_NAME, DATABASES_USER, DATABASES_PASSWORD, DATABASES_HOST` - данные для подключения к БД
2. `EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_HOST, EMAIL_PORT, EMAIL_USE_SSL` - данные для осуществления Email рассылки
3. `TELEGRAM_BOT_TOKEN` - токен Telegram бота
4. `SECRET_KEY, DEBUG`

## Авторы

UlianaSem

## Связь с авторами

https://github.com/UlianaSem/