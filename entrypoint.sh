#!/bin/sh

sleep 2

python manage.py migrate
python manage.py migrate dishes

if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
  python manage.py createsuperuser \
    --noinput \
    --username "$DJANGO_SUPERUSER_USERNAME" \
    --email $DJANGO_SUPERUSER_EMAIL
fi

python manage.py collectstatic --noinput
gunicorn foodgram_project.wsgi:application --bind 0.0.0.0:8000

exec "$@"