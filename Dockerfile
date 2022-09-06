FROM python:3

ENV PYTHONUNBUFFERED 1

# Set the working directory.
WORKDIR /usr/src/app/geographical-distance-calculator

# Copy the project source code.
COPY . ./

# Install geodjango dependencies.
RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin

# Upgrade pip.
RUN pip install --upgrade pip

# Install all pip dependencies.
RUN pip install --no-cache-dir -r requirements.txt
