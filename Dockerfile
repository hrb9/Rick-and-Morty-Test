# Use an official Python image as base
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the Python code into the container
COPY main.py /app

# Install the required Python packages
RUN pip install flask requests

# Expose port 5000 for Flask
EXPOSE 5000

# Command to start the application
CMD ["python", "main.py"]
