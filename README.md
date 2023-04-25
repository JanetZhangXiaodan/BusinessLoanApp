# BusinessLoanApp


##Option 1 : Run via CMD

Open 4 CMDs to start 4 services

1) frontend (runs on localhost:3000)

cd frontend
npm start

2) backend - main (runs on localhost:8080)

cd cd backend\main
python3 -m pip install -r requirements.txt
python3 main.py

3) backend - accounting (runs on localhost:8081)

cd cd backend\accounting
python3 -m pip install -r requirements.txt
python3 accounting.py

3) backend - decisionEngine (runs on localhost:8082)

cd cd backend\decisionEngine
python3 -m pip install -r requirements.txt
python3 decisionengine.py

![image](https://user-images.githubusercontent.com/15668158/234329981-99832afa-d047-41ff-8255-77e27a1e6586.png)

##Option 2 : Run via Docker

Open 1 CMD

1) key this in: docker compose up
