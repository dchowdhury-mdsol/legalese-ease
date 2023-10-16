# Use an appropriate base image (e.g., Ubuntu)
FROM ubuntu:latest

# Set environment variables to avoid any interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Update the package list and install necessary dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    sudo \
    bash   # Install Bash shell

# Install Homebrew using Bash
RUN /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

# Add Homebrew to the PATH
ENV PATH=/home/linuxbrew/.linuxbrew/bin:$PATH

# Install AWS CLI
RUN curl "https://d1vvhvl2y92vvt.cloudfront.net/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install

# Install Terraform
RUN curl -fsSL https://releases.hashicorp.com/terraform/1.3.9/terraform_1.3.9_linux_amd64.zip -o terraform.zip \
    && unzip terraform.zip -d /usr/local/bin \
    && rm terraform.zip

# Install Docker CLI
RUN curl -fsSL https://get.docker.com -o get-docker.sh \
    && sh get-docker.sh

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Stage 2: Use a Python image for your application
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Install pip3
RUN apt-get update && apt-get install -y python3-pip

# Copy your application pip3 requirements file
COPY src/docker/requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Copy all local files into the container
COPY src/python/. .

# Define the command to run your application
CMD ["python", "app.py"]