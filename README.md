# Описание

Проект представляет собой API для проекта yatube.

Ключевые моменты:

Применены вьюсеты.

Для аутентификации использованы JWT-токены.

У неаутентифицированных пользователей доступ к API только на чтение. Исключение — эндпоинт /follow/.

Аутентифицированным пользователям разрешено изменение и удаление своего контента; в остальных случаях доступ предоставляется только для чтения.

### **Стек**
![python version](https://img.shields.io/badge/Python-3.10.2-green)
![django version](https://img.shields.io/badge/Django-3.2.16-green)
![djangorestframework version](https://img.shields.io/badge/djangorestframework-3.12.4-green)
![PyJWT version](https://img.shields.io/badge/PyJWT-2.1.0-green)
![Pillow version](https://img.shields.io/badge/Pillow-9.3.0-green)
![requests version](https://img.shields.io/badge/requests-2.26.0-green)

# Установка

## 1) Склонировать репозиторий

git clone https://github.com/artyom-vah/api_final_yatube.git

## 2) Создать и активировать виртуальное окружение для проекта

python -m venv venv

source venv/scripts/activate

## 3) Установить зависимости
python pip install -r requirements.txt

## 4) Сделать миграции
python manage.py makemigrations
python manage.py migrate

## 5) Запустить сервер
python manage.py runserver

# Примеры

Для доступа к API необходимо получить токен: 

Нужно выполнить POST-запрос http://127.0.0.1:8000/api/v1/jwt/create/ передав поля username и password. API вернет JWT-токен

Дальше, передав токен можно будет обращаться к методам, например: 

/api/v1/posts/ (GET, POST, PUT, PATCH, DELETE)

При отправке запроса передавайте токен в заголовке Authorization: Bearer <токен>
