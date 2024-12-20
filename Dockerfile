FROM python:3.12.6-slim AS production

# Accept environment variables

# Set environment variables


# Install system dependencies required for building Postgres and website packages
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    build-essential \
    zlib1g-dev \
    bash \
    libffi-dev \
    openssl \
    libpq-dev \
    musl-dev \
    postgresql \
#    python-django-extensions \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1
WORKDIR /app/

COPY requirements/prod.txt ./requirements/prod.txt
RUN pip install --no-cache-dir -r requirements/prod.txt

COPY manage.py  ./manage.py
COPY setup.cfg ./setup.cfg
COPY resumechall ./resumechall
COPY static ./static
COPY Makefile ./Makefile
COPY . .
EXPOSE 8000


FROM production AS development

#RUN pip install --upgrade pip setuptools wheel
COPY requirements/prod.txt ./requirements/prod.txt
COPY requirements/dev.txt ./requirements/dev.txt
RUN pip install --no-cache-dir -r requirements/dev.txt
#RUN pip install --no-cache-dir -r requirements/prod.txt

COPY . .
