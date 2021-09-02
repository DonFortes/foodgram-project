![example workflow](https://github.com/DonFortes/foodgram-project/actions/workflows/foodgram.yml/badge.svg)
# Социальная сеть Foodgram.
![spaghetti-1932466_1920 (1)](https://user-images.githubusercontent.com/53881876/131886433-948bf48b-d0b4-482b-a8a9-e26a6ea45f94.jpg)

### You can see a working project [here.](https://nosov.ml/)
Technologies: Docker, Django, Gunicorn, PostgreSQL, Nginx, Caddy

## Project description
Here you can add your own recipes, as well as see recipes from other authors, follow their updates, add recipes to your favorites, and you can also prepare a convenient shopping list for ingredients for selected dishes.

### Local development
At the root of the project, you will find two docker-compose files. In order to start local development of a project, you need to rename the docker-compose.yaml file to docker-compose-prod.yaml, and docker-compose-dev.yaml to docker-compose.yaml, in which the settings for local development are saved. After that, you just have to execute the command:

docker-compose up

The project will be available at the local address: http://127.0.0.1/

After making the necessary changes, rename the docker-compose files in reverse order. This will make the project ready for deployment.
