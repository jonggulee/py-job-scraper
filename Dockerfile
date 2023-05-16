FROM python:3.9.16-slim
WORKDIR /app

COPY . .
RUN pip3 install -r requirements.txt

EXPOSE 4000
CMD [ "python3", "main.py"]