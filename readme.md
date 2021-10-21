**Запуск проекта:**
docker-compose up -d

**логи проекта:**
docker-compose logs

**загрузка базы проект**
docker-compose -f docker-compose-postgres.yml exec -T db_postgres_test psql -U postgres djangodb <dump_django.sql

**запуск генерации событий:**
docker exec -it test_for_restapi_db_postgres_1 psql -U postgres djangodb
./manage.py generator_event

**запуск проекта в браузере:**
localhost:8001/api/v0/

**запуск локального сервера для почты**
python -m smtpd -n -c DebuggingServer localhost:1025

**запуск теста**
тест только на отправку почты
./manage.py test


