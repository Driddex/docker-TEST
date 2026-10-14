FROM python:3.11-slim
WORKDIR /app

COPY . .
EXPOSE 8000

RUN pip install Flask
CMD [ "python", "api.py" ]