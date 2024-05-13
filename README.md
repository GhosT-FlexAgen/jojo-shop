# JoJo Shops

Проект интеренет магазина на Fastapi и react с применением sqlalchemy, redux, and Postgresql. 
Реализован в рамках дисциплины "Человеко-машинные интерфейсы".

## API магазина

url: http://localhost:8000/docs

<img src="./images/images8.png" alt="product"/>

## Инструкция по использования

<ul>
    <li>
        Установиить Python
    </li>
    <li>
        Установиить postgresql
    </li>
    <li>
        Установиить Pipenv pip install pipenv
    </li>
    <li>
        Установиить Npm and Nodejs
    </li>
    <li>
        перейти в папку backend и выполнить команду pipenv install
    </li>
    <li>
       перейти в папку  frontend и выполнить команду npm install
    </li>
    <li>
        запустить backend, выполнив команду uvicorn main:app --reload в директории backend/app 
    </li>
    <li>
        запустить frontend, выполнив команду npm start
    </li>
</ul>

## Краткий отчёт о прототипе магазина

Страница авторизации

<img src="./images/images13.png" alt="Страница авторизации" />

Страница регистрации

<img src="./images/images14.png" alt="Страница регистрации" />

Домашняя страница

<img src="./images/images1.png" alt="Домашняя страница" />

Просмотр информации о товаре

<img src="./images/images2.png" alt="Просмотр информации о товаре">

Корзина

<img src="./images/images3.png" alt="Корзина" />

Оплата товара (используется сторонний сервис оплаты - Stripe).

<img src="./images/images4.png" alt="Оплата товара" />

Страница заказов пользователя.

<img src="./images/images11.png" alt="Страница заказов пользователя." />

Информация о Заказе.

<img src="./images/images10.png" alt="Информация о Заказе." />

Панель администратора. Список пользователей.

<img src="./images/images5.png" alt="Панель администратора. Список пользователей." />

Панель администратора и менеджера. Список товаров.

<img src="./images/images6.png" alt="Панель администратора и менеджера. Список товаров." />

Панель администратора и менеджера. Добавление товара.

<img src="./images/images7.png" alt="Панель администратора и менеджера. Добавление товара." />

Панель администратора и менеджера. Изменение информации о товаре.

<img src="./images/images12.png" alt="Панель администратора и менеджера. Изменение информации о товаре." />

Панель администратора и менеджера. Список заказов.

<img src="./images/images9.png" alt="Панель администратора и менеджера. Список заказов." />