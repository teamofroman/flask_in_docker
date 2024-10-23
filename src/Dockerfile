FROM python:3.12-slim

WORKDIR /flaskapp
COPY requirements.txt .
RUN pip3 install --upgrade pip -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "main:create_flask_app()", "-b", "0.0.0.0:5000"]
