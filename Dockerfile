FROM node:10-alpine

WORKDIR /code/

COPY package.json /code/
RUN npm install 
COPY . /code/

# RUN npm rebuild node-sass

