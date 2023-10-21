FROM python:3.9.6-buster

# Install dependencies
RUN apt-get update && apt-get install -y --reinstall build-essential \
gcc supervisor sqlite3\
   && rm -rf /var/lib/apt/lists/*
# Expose port
EXPOSE 8000

# Copy requirements.txt and install packages
COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . /
USER root
# Make script executable
RUN chmod +x /run_app.sh

# Change permissions of the database file to read-only
RUN chmod 444 /db.sqlite3

RUN chown "$USER":"$USER" /db.sqlite3
RUN chown -R 1001:1001 /
# Run the application
CMD ["/run_app.sh"]