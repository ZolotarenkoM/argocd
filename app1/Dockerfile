FROM python:3.8-slim-buster

WORKDIR /app1

COPY . .
RUN pip3 install -r requirements.txt

env FLASK_APP="app1"
CMD [ "python3", "-m" , "flask", "run",  "--host=0.0.0.0"]
