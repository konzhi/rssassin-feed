FROM python:3.6-alpine

RUN adduser -D rfeed

WORKDIR /home/rfeed

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY rfeed.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP rfeed.py

RUN chown -R rfeed:rfeed ./
USER rfeed

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]