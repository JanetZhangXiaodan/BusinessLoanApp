FROM python:3.10

WORKDIR /backend/main

EXPOSE 8080

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . ./

CMD ["python", "main.py"]