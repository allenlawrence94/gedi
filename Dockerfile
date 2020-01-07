FROM python:latest

RUN pip install paho-mqtt
COPY pihrPubTest.v2.py main.py

CMD python main.py

