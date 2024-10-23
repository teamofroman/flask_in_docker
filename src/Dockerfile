FROM python:3.12-slim

WORKDIR /flaskapp
RUN apt update && \
    apt install -y netcat-traditional curl && \
    apt clean autoclean && apt autoremove --yes
COPY requirements.txt .
RUN pip3 install --upgrade pip -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["./docker-entrypoint.bash"]
