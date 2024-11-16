FROM python:3.12

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install flasgger
COPY . .
ENTRYPOINT [ "python", "app.py" ]