FROM python:3.9
WORKDIR /app

# Copy the requirements.txt file from the app folder to the container's working directory
COPY app/requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY app/ .

EXPOSE 5000
CMD ["python", "app.py"]
