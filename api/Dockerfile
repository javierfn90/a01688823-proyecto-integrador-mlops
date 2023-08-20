# Set the base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the API files to the working directory
COPY . .

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the API dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose the port on which the API runs
EXPOSE 8000

# Command to start the API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]