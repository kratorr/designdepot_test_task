# Тестовое задание для компании ДизайнДепо

Тестовое задание для компании ДизайнДепо на должность Junior python developer

Проект представляет собой простой блог на сделанным на фреймворке Django.
За основу взять админ панель Django, куда был добавлен WYSIWYG — редактор (django-ckeditor), так как по ТЗ в посты блога необходимо вставлять картинки, цитаты и т.д.


## Как запустить dev версию


Склонировать git репозиторий 

```bash
https://github.com/kratorr/designdepot_test_task
```

Создать виртуальное окружение

```bash
python3 -m venv venv
```
Активировать его
```bash
source venv/bin/activate
```
Установить зависимости
```bash
pip install -r requirements.txt
```
Примените миграции
```bash
python manage.py migrate
```
Создайте суперпользователя
```bash
python manage.py createsuperuser
```
Запустите сервер:

```bash
python manage.py runserver
```
Админка доступна по адресу:
```bash
http://127.0.0.1:8000/
```


## Как запустить prod-версию сайта



Настроить бэкенд: создать файл `.env` в каталоге `my_blog` со следующими настройками:

- `DEBUG` — дебаг-режим. Поставьте `False`.
- `SECRET_KEY` — секретный ключ проекта. 
- `ALLOWED_HOSTS` — [см. документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)
