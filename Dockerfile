FROM python:3.8-slim-buster

WORKDIR /DockerTest

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . .

EXPOSE 8888

ENTRYPOINT [ "jupyter-lab","--ip", "0.0.0.0", "--allow-root" ]