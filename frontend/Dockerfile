FROM node:latest

WORKDIR /app

EXPOSE 3000

COPY package*.json ./

RUN npm install --silent

COPY . ./

COPY requirements.txt ./

RUN apt-get update && apt-get install -y python3-pip && pip3 install --no-cache-dir -r requirements.txt

CMD ["npm", "start"]