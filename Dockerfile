FROM python:3.12-slim

#Working Directory
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

#COPYing local file to image
COPY . .

EXPOSE 8000

CMD [ "fastapi","dev","--host","0.0.0.0","-port","8000" ]

