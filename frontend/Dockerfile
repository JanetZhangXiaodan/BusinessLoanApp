FROM node:12-alpine

WORKDIR /app

EXPOSE 3000

COPY package*.json ./

RUN npm install --silent

COPY . /app/

CMD ["npm", "start"]