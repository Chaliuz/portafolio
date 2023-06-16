FROM ubuntu:bionic
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1
WORKDIR /code/
# COPY requirements.txt /code/
# COPY . /code/

VOLUME ./code/ /home/code/
RUN apt update && apt install curl 

# Install old version node:
RUN curl -fsSL https://deb.nodesource.com/setup_10.x | bash - && apt-get install -y nodejs 

# Install all dependencies:
RUN npm install 
RUN npm start


