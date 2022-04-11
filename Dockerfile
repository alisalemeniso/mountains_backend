#FROM python:3.9-alpine
FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1

RUN mkdir /mountains_backend
WORKDIR /mountains_backend
COPY . .
COPY ./requirements.txt /requirements.txt
#RUN apt-get install libpq-dev python3-dev build-essential postgresql-server-dev-all libproj-dev musl-dev
#apk add --no-cache --virtual build-deps gcc python3-dev musl-dev proj proj-dev proj-util && apk add postgresql-dev
#apt-get musl-dev proj proj-dev proj-util gdal-dev && apk add postgresql-dev

#RUN apt-get install binutils libproj-dev gdal-bin

#RUN pip install -U pip setuptools
#RUN pip install wheel
#RUN pip install --upgrade pip
#RUN pip install numpy
RUN apt-get update \
    && apt-get -y install libpq-dev python3-dev gcc postgresql-client libjpeg-dev \
    linux-libc-dev postgresql-server-dev-all musl-dev zlib1g zlib1g-dev
    #&& apt-get -y install gdal-bin libgdal-dev
#RUN export CPLUS_INCLUDE_PATH=/usr/include/gdal
#RUN C_INCLUDE_PATH=/usr/include/gdal
#RUN pip install GDAL

RUN pip install -r requirements.txt

RUN adduser user
USER user

RUN ls -l