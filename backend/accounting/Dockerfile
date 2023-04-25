FROM python:3.10

WORKDIR /backend/accounting

EXPOSE 8081

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . ./

CMD ["python", "accounting.py"]