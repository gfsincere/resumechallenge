build:
	docker build --force-rm $(options) -t resumechallenge:latest .

build-prod:
	$(MAKE) build options="--target production"

compose-start:
	docker-compose up --remove-orphans $(options)

compose-stop:
	docker-compose down --remove-orphans $(options)

compose-manage:
	docker-compose run --rm web python manage.py $(cmd)