# Задание

* Реализовать Django + Stripe API
* Django Модель Item с полями (name, description, price)
* GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого
  метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и
  полученный session.id выдаваться в результате запроса (Реализовано)
* GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном
  Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее с
  помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id) (
  Реализовано)


* Запуск используя Docker (Запуск используя докер возможен, но тогда не происходит редирект из-за использования http
  вместо https)
* Использование environment variables (Используется при запуске на удаленном сервере, или докер образе)
* Просмотр Django Моделей в Django Admin панели (Реализовано)
* Запуск приложения на удаленном сервере, доступном для тестирования
* Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей
  стоимостью всех Items (Реализовано)
* Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании
  платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме.
* Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара
  предлагать оплату в соответствующей валюте (Реализовано)
* Реализовать не Stripe Session, а Stripe Payment Intent.

# Доступные ссылки

```bash
admin/ -> админка
buy/<int:item_id>/ -> покупка 
item/<int:item_id>/ -> ссылка на покупку с получением кнопки купить
order/<int:order_id> -> получение информации списка покупок с кнопкой купить
order/new/ -> создание списка покупок
order/<int:order_id>/add/<int:item_id> -> добавление выбранной покупки в выбранный спиок покупок
order/<int:order_id>/buy -> ссылка на список покупок с получением кнопки купить
```

# Запуск

### локалка

```bash
git clone https://github.com/kekoslav42/Stripe-API-test-tast.git
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Docker-compose (Ломается кнопка покупки и не работает редирект(из-за http))
1. Установка docker и docker-compose

Инструкция по установке доступна в официальной инструкции

2. Создать файл .env с переменными окружения в папке infra

```bash
SECRET_KEY = Секретный ключ django
STRIPE_API_KEY = Апи ключ от Stripe
### При использование PostgreSQL(Необходимо раскоментировать в файле сеттингс  строки 59-68)
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER= Пользователь базы данных
POSTGRES_PASSWORD= Пароль базы данных
DB_HOST= Хост базы данных
DB_PORT= Порт базы данных
```

3. Сборка и запуск контейнера(Выполняется в папке infra)

```bash
docker-compose up -d --build
```

4. Сбор статики

```bash
docker-compose exec web python manage.py collectstatic --noinput
```
5. Применение миграций

```bash
docker-compose exec web python manage.py migrate
```
6. Создание суперпользователя 
```bash
docker-compose exec web python manage.py createsuperuser
```