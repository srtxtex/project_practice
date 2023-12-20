# Персональный помощник для студентов
- Цель проекта:
> Облегчить студентам получение знаний из зарубежных источников, затрачивая на эти задачи минимум времени.

- Функциональность:
> Перевод статьи с английского языка на русский и генерация краткого тезисного конспект текста. 

## Начало работы
1. Инструкции по настройке окружения для скачивания и запуска проекта локально:
   *(Последовательно выполните на машине linux следующие команды)*
- `$ mkdir имя_папки`  *создайте папку в которую вы поместите проект*
- `$ cd имя_папки`
- `$ sudo apt update`
- `$ sudo apt install python3.10-venv`
- `$ python3 -m venv venv_name` *Создайте новое окружение, где venv_name - название окружения*
- `$ source venv_name/bin/activate`
  
2. Импорт и запуск проекта:
- `$ git clone git@github.com:<you-info>.git` *(Склонируйте проект в созданную вами папку)*
- `$pip install -r requirements.txt` *(Установите зависимости из файла)*
- `$python manage.py runserver` *(Запустите приложение)*
- Перейдите по адресу: http://127.0.0.1:8000/ в браузере

### Тесты:
1. Проверка кода на PEP8:
- `$pep8 ApplicationAi/hf.py`
- `$pep8 crs_practice_dj_prt/urls.py`
- `$pep8 pep8 MainApp/forms.py`
- `$pep8 MainApp/models.py`
- `$pep8 MainApp/views.py`
2. Unit тесты:
- 

## Использование
1. Перейдите на главную страницу приложения **Home**;
2. Вставьте в поле **"Текст статьи"** нужный для перевода текст и нажмите на кнопку **Translate**;
   > В поле **"Перевод статьи"** отобразится переведенный на русский язык текст.
3. Нажмите на кнопку **Summary** для генерации краткого содержания статьи;
   > Краткое изложение статьи отобразится в поле **"Краткое содержание статьи"**.

## Команда
- Менеджер проекта - Попова И.К.
- Аналитик данных - Максимова Н.В.
- Инженер по машинному обучению - Запатоцкий Юрий М.
- Full Stack разработчик - Сергеев Владимир В.
- Тестировщик QA инженер - Андрей
- Документалист - Рагимов А.Ю.

## Лицензия
Приложение включает в себя код из библиотеки Python, Django, Pandas, Numpy, Transformers, Hugging face, Bootstrap.
Все компоненты входящие в состав приложения с открытым исходным кодом и имеют разрешающую лицензия GPL.

