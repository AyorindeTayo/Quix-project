# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/webapp

# Copy the current directory contents into the container at /usr/src/app
COPY a-client/ .


# requirments
RUN pip freeze > requirements.txt .


# req
RUN pip freeze > requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the script when the container launches
CMD ["python3", "kafka_producer.py"]
