FROM python:3.7-alpine
WORKDIR /app
COPY main.py /app
COPY db_connector.py /app
COPY backend_testing.py /app
RUN pip install -r requirements.txt
EXPOSE 5000
VOLUME /app/logs
CMD python3 rest_app.py