#!/bin/sh

sleep 2
python manage.py makemigrations api dishes users
python manage.py makemigrations
python manage.py migrate
python manage.py migrate api dishes users
python manage.py createcachetable

if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
  python manage.py createsuperuser \
    --noinput \
    --username "$DJANGO_SUPERUSER_USERNAME" \
    --email $DJANGO_SUPERUSER_EMAIL
fi

python manage.py collectstatic --noinput
gunicorn foodgram_project.wsgi:application --bind 0.0.0.0:8000

exec "$@"