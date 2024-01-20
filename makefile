build:
	docker-compose build

run:
	docker-compose up

test:
	docker-compose run --rm app sh -c "python -Wa manage.py test --noinput"

test-shuffle: only in django 4.0 (update later)
	docker-compose run --rm app sh -c "python -Wa manage.py test --shuffle"

lint:
	docker-compose run --rm app sh -c "flake8"

start-project:
	docker-compose run --rm app sh -c "django-admin startproject app ."

create-app:
	docker-compose run --rm app sh -c "python manage.py startapp $(name)"

makemigrations:
	docker-compose run --rm app sh -c "python manage.py makemigrations"

migrate:
	docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"
