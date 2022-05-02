# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Скачайте код
- Создайте excel файл с напитками. В качестве примера, возьмите `wine3.xlsx`.
 
- Установите необходимые библиотеки с помощью команды 
  ```
  pip install -r requirements.txt
  ```
- Запустите сайт командой 
    ```
    python3 main.py
    ```
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Описание функций main.py
----

def count_years_of_work()
-
Автоматически подсчитывает количество лет, прошедших с основания винодельни.

def get_drinks_from_excel()
-
Принимает excel файл с напитками, разбирает его, и возвращает напитки и информацию по ним в виде словаря.
