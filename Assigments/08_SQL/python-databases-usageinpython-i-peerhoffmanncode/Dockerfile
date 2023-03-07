# base image
FROM python:3.11.0-slim

# install netcat
RUN apt-get update && \
    apt-get -y install netcat && \
    apt-get clean

# set working directory
WORKDIR /code

# add and install requirements
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

# add app
COPY . /code

CMD ["python", "-m", "unittest"]
