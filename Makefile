tag=latest
registry=blacktonystark
image=resumechallenge


build:
	docker build --force-rm $(options) -t resumechallenge:latest .

build-prod:
	$(MAKE) build options="--target production"

compose-start:
	docker-compose up --remove-orphans $(options)

push:
	docker tag $(image):latest $(registry)/$(image):$(tag)
	docker push $(registry)/$(image):$(tag)

compose-stop:
	docker-compose down --remove-orphans $(options)

compose-manage:
	docker-compose run --rm web python manage.py $(cmd)

start-server:
	python manage.py runserver 0.0.0.0:8000

helm-deploy:
	helm upgrade --install --debug resume ./helm/resumechallenge	