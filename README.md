# BusinessLoanApp

## `4 scenarios for loan payment (decisionengine.py)`

T, T : Profit and Average asserts > Loan -> max(60, 100) = 100 \
T, F : Profit and Average asserts < Loan -> max(60, 20) = 60 \
F, T : Loss and Average asserts > Loan -> max(20, 100) = 100 \
F, F : Loss and Average asserts < Loan -> max(20, 20) = 20

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



## `Option 2 : Run via Docker` (Must install Docker Desktop) 

### Code is currently modified to run in Docker, to run locally on CMD, please change URL in main.py to localhost:..
![image](https://user-images.githubusercontent.com/15668158/234494358-fc43483f-ab86-4182-9b25-21645b38a3df.png)


### Open 1 CMD


1) key this in CMD \
cd BusinessLoanApp \
docker compose up

open webpage and key in http://localhost:3000


![image](https://user-images.githubusercontent.com/15668158/234493752-64b25fdd-f3dc-44a6-b252-3ed7738ea56a.png)

![image](https://user-images.githubusercontent.com/15668158/234493972-b3b73c9b-dc52-4800-925a-7fb1592957c2.png)

![image](https://user-images.githubusercontent.com/15668158/234503975-1d905014-b893-49b5-a7c2-94a42be582fe.png)

## `Running Unittest for backend` 

1) On CMD \

cd backend\main \
python3 maintests.py

cd accounting \
python3 accountingtests.py

cd decisionEngine \
python3 decisionenginetests.py


