FROM python:3.8-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY /compare_app .

CMD ["python", "flask", "run", "--host", "0.0.0.0"]