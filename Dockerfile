FROM ubuntu:16.04
MAINTAINER Yifei Kong<kongyifei@gmail.com>

RUN apt-get update && apt-get install -y python3 python3-pip
COPY . /opt/tiger/ping
WORKDIR /opt/tiger/ping
RUN pip3 install -r requirements.txt

EXPOSE 8002

CMD ["python", "app.py"]
