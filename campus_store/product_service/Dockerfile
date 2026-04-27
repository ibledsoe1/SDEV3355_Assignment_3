FROM python:3.13
WORKDIR /app

# install dependencies
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "runserver.py" ]