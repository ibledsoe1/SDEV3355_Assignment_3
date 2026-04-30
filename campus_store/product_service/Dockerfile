FROM python:3.13
WORKDIR /app

# install dependencies
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "uvicorn", "arc:app", "--host", "0.0.0.0", "--port", "8000" ]