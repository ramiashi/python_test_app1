FROM ubuntu:16.04


RUN apt-get update -y && \  
    apt-get install python3 -y python3-pip python3-dev 
COPY ./requirements.txt /requirements.txt

RUN pip3 install -r requirements.txt
WORKDIR /src

COPY ./src/python_test_app1.py /src
EXPOSE 5000
ENTRYPOINT [ "python3" ]

CMD [ "/src/python_test_app1.py" ]  
