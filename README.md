# **Автотест на создание заказа и проверку возможности получение информации о заказе по трек номеру и SQL-запросы к БД**.

## **SQL-запросы к базе данных**.
SQL-запросы и скриншоты ответов на них содержатся в файле: SQL запросы Практический блок.docx

## **Автотест на создание заказа и проверку возможности получение информации о заказе по трек номеру**.
**Файлы отвечающие за автотест:**
1. configuration.py - URL адрес и ручки, для отправки запросов.
2. data.py - Тела запросов
3. sender_stand_request.py - Запросы.
4. tests.py - Автотест.
5. Screenshot_for_tests.jpg - Скриншот выполнения теста.
6. README.md - Описание проекта.
7. .gitignore - файл игнорирование в Git.

**Запуск автотеста**
1. Для запуска теста в PyCharm должны быть установлены пакеты pytest и requests.
2. Для запуска теста не забыть поменять значение URL_SERVICE в файле configuration.py на адрес запущенного тестового стенда.
3. Запуск теста выполняется командой: "pytest tests.py".

**В автотесте реализованы шаги:**
1. Выполняется запрос на создание заказа.
2. Сохраняется номер трека заказа.
3. Выполняется запрос на получения заказа по треку заказа.
4. Проверяется, что код ответа равен 200.

## **Задания из тренажера**.
**Работа с базой данных**
**Задание 1**
Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 
**Задание 2**
Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
Для этого: выведи все трекеры заказов и их статусы. 
**Статусы определяются по следующему правилу:**
Если поле finished == true, то вывести статус 2.
Если поле canсelled == true, то вывести статус -1.
Если поле inDelivery == true, то вывести статус 1.
Для остальных случаев вывести 0.

**Автоматизация теста к API**
**Теперь автоматизируй сценарий, который подготовили коллеги-тестировщики:**
Клиент создает заказ.
Проверяется, что по треку заказа можно получить данные о заказе.
**Шаги автотеста:**
Выполнить запрос на создание заказа.
Сохранить номер трека заказа.
Выполнить запрос на получения заказа по треку заказа.
Проверить, что код ответа равен 200.

**Технические примечания:**
К проекту добавь файлы .gitignore и README.MD .
