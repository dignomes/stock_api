FROM python:3.9.6-buster

# Install dependencies
RUN apt-get update && apt-get install -y --reinstall build-essential \
gcc supervisor sqlite3\
   && rm -rf /var/lib/apt/lists/*
# Expose port
EXPOSE 8000
EXPOSE 5432

# Copy requirements.txt and install packages
COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . /
# Make script executable
RUN chmod +x /run_app.sh


# Run the application
CMD ["/run_app.sh"]