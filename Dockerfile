FROM ghcr.io/osgeo/gdal:ubuntu-small-3.7.0
LABEL MAINTAINER = "Osca Mwongera <oscamwongera@gmail.com>"

# set environment variables
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

RUN apt-get update -y && \
    apt-get install -y python3-pip && \
    apt-get install -y gcc gdal-bin libgdal-dev && \
    apt-get autoremove -y

RUN python -m pip install --upgrade pip

RUN pip install GDAL==$(gdal-config --version) --global-option=build_ext --global-option="-I/usr/include/gdal"

COPY requirements.txt .

RUN pip install -r requirements.txt

# create directory for the app user
COPY . .

#CMD ["python", "manage.py", "runserver"]
