FROM python:3
MAINTAINER Jean-Baptiste GANDONOU (jean.gandonou@rintio.com)
ADD . /
CMD [ "apt-get install libpq-dev" ]
RUN pip3 install r requirements.txt
CMD [ "python3", "dbVedaSf/server.py" ]
