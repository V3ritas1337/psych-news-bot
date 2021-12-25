# A dockerfile must always start by importing the base image.
# We use the keyword 'FROM' to do that.
# In our example, we want import the python image.
# So we write 'python' for the image name and 'latest' for the version.
FROM python:3.7.6

COPY ./ .
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip install pipenv 
RUN pipenv install 

CMD [ "pipenv", "run", "python", "./main.py" ]