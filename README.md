# Лабораторная работа №5
 <div>
 <img src="https://img.shields.io/badge/language-Django-blue.svg" alt="Go Language">
 </div>


Цель работы: Завершение бэкенда для SPA
Порядок показа: выполнить авторизацию через swagger в режиме инкогнито, получить список заявок в swagger; использовать содержимое куки/localStorage+authorization из браузера для заголовков остальных запросов через insomnia/postman. Далее в insomnia/postman выполнить GET списка заявок: 401/403 для гостя, для создателя только его заявки. Выполнить PUT завершения заявки: для создателя 403 статус, для модератора успех и обновление полей. Выполнить GET списка заявок - для модератора все заявки. Показать содержимое Redis
Контрольные вопросы: куки, сессия, redis, jwt, авторизация, аутентификация
Sequence диаграмма: весь набор HTTP запросов по бизнес-процессу без БД и нативного приложения: аутентификация, список услуг без черновика, добавление услуги в заявку, еще раз список услуг с черновиком, просмотр черновой заявки, формирование заявки, обращение к асинхронному сервису и обратно, список заявок с данными от асинхронного. Добавить домены в качестве Lifeline, при добавлении сообщений выбирать методы доменов из диаграммы классов, передавать ключевые входные и выходные данные через arguments в скобках у Message
