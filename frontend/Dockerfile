FROM python:3.11-slim
WORKDIR /app

COPY . .
EXPOSE 3000

RUN pip install requests
CMD [ "python", "fr.py" ]