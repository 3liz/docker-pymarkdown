FROM python:3.7-slim-buster
RUN apt-get update && apt-get -y install git
RUN pip install markdown
COPY transform.py /usr/bin/transform.py
ENTRYPOINT ["/usr/bin/transform.py"]
