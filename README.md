# Yatube API

## Описание

Этот проект представляет собой API для социальной сети Yatube. API позволяет пользователям создавать и просматривать публикации, группы, комментарии и подписываться на других пользователей.

## Установка

1.  Клонируйте репозиторий:
    ```bash
    git clone <repository_url>
    ```
2.  Создайте и активируйте виртуальное окружение:
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # Linux/macOS
    venv\Scripts\activate.bat  # Windows
    ```
3.  Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
4.  Выполните миграции:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5.  Создайте суперпользователя:
    ```bash
    python manage.py createsuperuser
    ```
6.  Запустите сервер:
    ```bash
    python manage.py runserver
    ```

## Примеры API

### Получение JWT-токена:

```bash
POST /api/token/
Content-Type: application/json

{
    "username": "your_username",
    "password": "your_password"
}