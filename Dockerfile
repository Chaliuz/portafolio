FROM node:10-alpine
# FROM node:10-bullseye
# FROM node:10-buster

WORKDIR /home/code/

COPY ./package.json /home/code/
RUN npm install 
COPY . /home/code/

RUN npm rebuild node-sass

