 FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 WORKDIR /code
 COPY requirements.txt /code/
 # REMOVE ME
 COPY calvertjournal.html /code/
 RUN pip install -r requirements.txt
 COPY . /code/
