FROM python:3.9.7-slim-buster


WORKDIR .
RUN apt upgrade && apt upgrage -y
COPY . .
RUN pip3 install -r requirements.txt

CMD ["python3", "userbot.py"]
