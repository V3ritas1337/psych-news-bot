# A dockerfile must always start by importing the base image.
# We use the keyword 'FROM' to do that.
# In our example, we want import the python image.
# So we write 'python' for the image name and 'latest' for the version.
FROM python:latest

COPY ./ .
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip install -U python-dateutil
RUN pip install -U pyyaml
RUN pip install -U feedparser
RUN pip install -U python_telegram_bot
RUN pip install -U telegram

CMD [ "python3", "./main.py" ]