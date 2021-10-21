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


**запуск только базы**
docker-compose -f docker-compose-postgres.yml up -d
docker-compose -f docker-compose-postgres.yml logs
docker exec test_for_restapi_db_postgres_test_1 pg_dump -v -h localhost -p 5432 -U postgres djangodb >dump_django.sql

в настройках settings.py 
нужно изменить

DATABASES = {
    'default': {
            ...
        'PORT' : '4040'
            ...
    }
}