# easy_plans
Приложение для создания, редактирования, хранения и генерации в формате ".docx" индивидуальных планов
студентов музыкальных школ (Училищ и музыкальных ВУЗов). Предназначено для
использования педагогами по специальности. В планах показать этот проект
в инициативах Москвы и реализовать его выпуск и эксплотацию во всех музыкальных
учебных заведениях. Цель - упростить ведение документации педагогам по специальности,
которая не модернезировалась уже пол века.
### интеграции
В проекте существует интеграция с Порталом открытых данных министерства культуры Российской Федерации,
чтобы успешно запустить приложение - необходимо получить ключь API по ссылке:
[Официальный сайт Минкультуры России](https://opendata.mkrf.ru/item/dev)

### Как запустить
Склонируйте репоз
```commandline
git clone https://github.com/AlbertSabirzianov/easy_plans.git
```
Перейдите в директорию с докером
```commandline
cd easy_plans/docker
```
Создайте файл ".env" в этой директории с содержимым
```.properties
POSTGRES_DB=easy_plans
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
DB_HOST=db
DB_PORT=5432

API_KEY=<API ключь, который вы получили на сайте министерства культуры>

```
Запустите проект командой
```commandline
docker compose --env-file .env up -d
```
Приложение будет доступно на порту :8000<br/>
Остановить сервер можно командой
```commandline
docker compose down
```

