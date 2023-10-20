FROM python:3.9.6-slim-buster
RUN apt-get update && apt-get install -y --reinstall build-essential \
  gcc supervisor\
   && rm -rf /var/lib/apt/lists/*
EXPOSE 8000

COPY ./ /

RUN chmod +x /start.sh

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["/run_app.sh"]
