# FROM python:3.13.0a6-slim-bookworm
FROM python:3.10-slim

# Inside Container
# make a new folder inside container
WORKDIR /app

# Outside Container -> Inside Container
# this contains the libraries want to install to run the app
COPY requirements.txt requirements.txt

# Inside Container
# Install the python libraries used for the app
RUN pip3 install -r requirements.txt

# Outside Container -> Inside Container
# . means everything in the current directory
# first period . - /app (outside container)
# second period . /app (inside container)
COPY . .

EXPOSE ${PORT}

ENV PYTHONUNBUFFERED=1

# CMD (Command)
# python3 -m flask run --host=0.0.0.0 --port=4567
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567", "--debug"]