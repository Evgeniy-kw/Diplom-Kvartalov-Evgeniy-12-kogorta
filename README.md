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