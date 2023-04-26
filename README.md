# BusinessLoanApp


## `Option 1 : Run via CMD`

### Open 4 CMDs to start 4 services

1) frontend (runs on localhost:3000)

cd frontend \
npm start

![image](https://user-images.githubusercontent.com/15668158/234330961-c08649b5-e96f-4f30-a371-b5be8696cd0e.png)


2) backend - main (runs on localhost:8080)

cd backend\main \
python3 -m pip install -r requirements.txt \
python3 main.py

![image](https://user-images.githubusercontent.com/15668158/234331118-68e159a7-e687-4234-bc0f-df48426dc3bb.png)


3) backend - accounting (runs on localhost:8081)

cd backend\accounting \
python3 -m pip install -r requirements.txt \
python3 accounting.py

![image](https://user-images.githubusercontent.com/15668158/234331210-58c57209-c575-4864-b789-a6a6ab999410.png)


3) backend - decisionEngine (runs on localhost:8082)

cd backend\decisionEngine \
python3 -m pip install -r requirements.txt \
python3 decisionengine.py

![image](https://user-images.githubusercontent.com/15668158/234331679-0b4793ea-da60-42a7-b1a0-c393e1176108.png)

![image](https://user-images.githubusercontent.com/15668158/234341499-16b74d86-a558-4fbe-81f5-dabe5d14d35f.png)



## `Option 2 : Run via Docker` (Must to install Docker Desktop)

### Open 1 CMD


1) key this in: docker compose up
