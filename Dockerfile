FROM python:3.9.7

WORKDIR /python

ADD . /python

RUN pip install -r requirements.txt

CMD ["python" ,"first.py"]


