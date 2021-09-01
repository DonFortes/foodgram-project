![example workflow](https://github.com/DonFortes/foodgram-project/actions/workflows/foodgram.yml/badge.svg)

# Project Title
## Социальная сеть Foodgram.
Технологии: Docker, Django, Gunicorn, PostgreSQL, Nginx, Caddy
### https://nosov.ml/

## Project description
Здесь вы можете добавить свои рецепты, а также увидеть рецепты от других авторов, следить за их обновлениями, добавлять рецепты в избранное, а также сможете подготовить удобный список покупок ингредиентов для выбранных блюд.

### Local development
В корне проекта вы найдете два файла docker-compose. Для того, чтобы запустить локальную разработку проекта - вам нужно переименовать файл docker-compose.yaml в docker-compose-prod.yaml, а docker-compose-dev.yaml в docker-compose.yaml, в котором сохранены настройки для локальной разработки. После чего вам останется лишь выполнить команду:

docker-compose up

Проект будет доступен по локальному адресу: http://127.0.0.1/

После внесения необходимых изменений - переименуйте файлы docker-compose в обратном порядке. Таким образом проект станет готов для деплоя.