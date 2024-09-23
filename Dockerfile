FROM python:3.9-slim
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir requests schedule python-dotenv
CMD ["python3", "bot_script.py"]