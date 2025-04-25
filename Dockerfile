FROM python:3.11

ARG DIR=/code

WORKDIR $DIR

RUN apt update

COPY requirements.txt ./

RUN python3 -m pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8050

CMD [ "uwsgi", "--ini", "uwsgi.ini" ]
