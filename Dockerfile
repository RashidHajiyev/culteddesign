FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app   
#/usr/src/app

# Install PostgreSQL development libraries
RUN apt-get update && apt-get install -y \
    libpq-dev gcc

# Copy the current directory contents into the container at /app
COPY . /app
#COPY . /usr/src/app/

# Upgrade pip to the latest version
RUN pip install --no-cache-dir --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose port 8000 for the Django application
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Command to run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
