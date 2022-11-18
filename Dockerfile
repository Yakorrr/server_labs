FROM python:3.10.7
ENV FLASK_APP=files
COPY requirements.txt /opt
RUN python3 -m pip install -r /opt/requirements.txt
COPY files /opt/files
WORKDIR /opt
CMD flask --app files run --host 0.0.0.0 -p $PORT
