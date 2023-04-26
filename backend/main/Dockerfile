FROM python:3.10

WORKDIR /app/main

EXPOSE 8080

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . ./

CMD ["python", "main.py"]