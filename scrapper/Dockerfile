FROM python:3.8.2-alpine
MAINTAINER anuj chourasiya <anujchourasiyadp@gmail.com>

COPY ./ /root/
RUN pwd
WORKDIR /root/
RUN pip3 install -r requirements.txt
RUN apk add git
RUN pip3 install git+git://github.com/miguelgrinberg/flask-whooshalchemy.git
ENTRYPOINT ["/usr/local/bin/python3","runscript.py"]
