FROM python:latest

WORKDIR /usr/src/app

ADD app.py /usr/src/app
ADD index.html /usr/src/app
RUN mkdir cgi-bin 
ADD cgi-bin/form.py  /usr/src/app/cgi-bin/form.py
RUN chmod +x /usr/src/app/app.py
RUN chmod +x /usr/src/app/cgi-bin/form.py
CMD [ "python", "./app.py" ]  
