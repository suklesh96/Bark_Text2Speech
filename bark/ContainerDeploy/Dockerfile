FROM python:3.9

ENV PYTHONUNBUFFERED True

COPY requirements.txt ./

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install git+https://github.com/suno-ai/bark.git
RUN pip install -r requirements.txt

CMD python fast.py