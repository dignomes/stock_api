FROM python:3.9.6-slim-buster
RUN apt-get update && apt-get install -y --reinstall build-essential \
gcc supervisor\
   && rm -rf /var/lib/apt/lists/*
EXPOSE 8000

RUN pip install --no-cache-dir -r requirements.txt
COPY ./ /

RUN chmod +x /run_app.sh


CMD ["/run_app.sh"]
