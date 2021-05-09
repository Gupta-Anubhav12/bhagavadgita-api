FROM python:3.7.4-slim

# Create Working directory
RUN mkdir /app
WORKDIR /app/

#Copy dependencies
COPY requirements.txt ./

# Install dependencies
RUN pip install -r requirements.txt --no-cache-dir

COPY . .