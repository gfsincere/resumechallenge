FROM python:3.12.6-slim-bookworm as production

ENV PYTHONUNBUFFERED=1
WORKDIR /app/

COPY requirements/prod.txt ./requirements/prod.txt
RUN pip install --no-cache-dir -r requirements/prod.txt

COPY manage.py  ./manage.py
COPY setup.cfg ./setup.cfg
COPY resumechallenge ./resumechallenge
COPY resumechall ./resumechall

EXPOSE 8000

