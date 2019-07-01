# Python version
FROM python:3.7-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Copy files
COPY . /code

# Copy Pipfile
#COPY Pipfile /code

# Install dependencies
RUN pip install --upgrade setuptools
RUN sudo apt-get install python3-venv
RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip install tox
RUN pip install -r requirements.txt



