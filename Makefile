manage_py := sudo docker compose exec -it backend python3 ./app/manage.py

run:
	python3 ./app/manage.py runserver 0.0.0.0:8000

shell:
	$(manage_py) shell_plus --print-sql

makemigrations:
	$(manage_py) makemigrations

migrate:
	$(manage_py) migrate

collectstatic:
	$(manage_py) collectstatic --no-input && \
	sudo docker cp backend:/tmp/static /tmp/static && \
	sudo docker cp /tmp/static nginx:/etc/nginx/static
