# Квалификационное задание для разработчиков Python в FunBox

----
### Задание заключалось в реализации web-приложения для простого учета посещенных ссылок.
К приложению предъявлялись следующие требования:
* Приложение написано на языке Python 3.7+
* Приложение представляет JSON API по HTTP
* Приложение предоставляет 2 HTTP ресурса:
`POST /api/v1/visited_links` и `GET /api/v1/visited_domains?from={from_time}&to={to_time}`
* Первый ресурс служит для передачи в сервис массива ссылок в POST-запросе. Временем их посещения считается время получения запроса сервисом.
* Второй ресурс служит для получения GET-запросом списка уникальных доменов, посещенных за переданный интервал времени.
* Для хранения данных сервис должен использовать БД Redis.
* Код должен быть покрыт тестами.
---
### Для запуска сначала установите зависимости:
#### `pip install -r requirements.txt`

---
### Далее, в файле settings.py настройте БД Redis в константе `REDIS_HOST`, а также `SECRET_KEY`.