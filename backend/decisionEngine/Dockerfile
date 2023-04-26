FROM python:3.10

WORKDIR /app/decisionengine

EXPOSE 8082

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . ./

CMD ["python", "decisionengine.py"]