FROM alpine:3.4
MAINTAINER @ashmastaflash

RUN apk add -U \
  python \
  py-pip

COPY app/ /app/

COPY requirements.txt /app/

RUN /usr/bin/python2.7 \
    -mpip install -r /app/requirements.txt

RUN adduser \
        -D \
        -s /bin/sh \
        -h /app \
        builtwithgetter

RUN chown -R builtwithgetter:builtwithgetter /app

ENTRYPOINT /usr/bin/python2.7 /app/application.py
