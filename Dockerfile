FROM python:3

# install some utilities
RUN apt-get update && apt-get install nano

# Install Python requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python source code to the image
COPY src /src

# Copy the tests to the image
COPY test /test

# keep container running
CMD sleep infinity