FROM python:3.8-slim-buster

ADD . /home/
WORKDIR /home

# RUN --mount=type=secret,id=env soruce /run/secrets/env

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . .

EXPOSE 8888

ENTRYPOINT [ "jupyter-lab","--ip", "0.0.0.0", "--allow-root" ]