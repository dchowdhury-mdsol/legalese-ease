# CONTRIBUTING

This document provides guidelines and instructions to help you get started with Legalese Ease.

## Contents
- [Install Dependencies](#install-dependencies)
- [Running Docker Container](#running-docker-container)
- [Running Tests](#running-tests)
- [Executing Python Scripts](#executing-python-scripts)

## Install Dependencies
To set up your development environment, you need to install several dependencies. Run the following commands:

```bash
pip3 install openai
pip3 install boto3
pip3 install awscli
pip3 install pandas
```

These commands will install necessary packages like `openai`, `boto3`, `awscli`, and `pandas` which are required for the project.

## Running Docker Container
To run the Docker container locally from the provided `Dockerfile`, use these commands:

```bash
docker build -t legalease-app .
docker run -p 8000:8000 legalease-app
```

This will build and run the Docker container, mapping the container's port 8000 to your local port 8000.

## Running Tests
To run unit tests, execute the following command:

```bash
python3 -m unittest discover -s tests
```

This command runs all tests in the `tests` directory.

## Executing Python Scripts
There are several Python scripts that you can run. Here's how to execute them:

### QUERYCOMPLETION
```bash
python3 src/python/DataQueryGPT.py [API_KEY] [PROMPT]
```

### LawyerPackage
```bash
python3 src/python/LawyerPackage.py [username] [question] [ai_model] [approval_status] [--improved_response]
```

### TABLEUPLOAD
```bash
python3 src/python/TableUpload.py [ID] [QUERY] [COMPLETION] [RESPONSE_ACCEPTED] [ACCEPTANCE_TARGET] [QUERY_TYPE] [ACTUAL_RESPONSE] [ENVIRONMENT]
```

### UserPackage
```bash
python3 src/python/UserPackage.py [username] [question] [ai_model]
```

Ensure that the arguments you pass to each script match its expected input parameters.
```

This `CONTRIBUTING.md` file is structured to guide contributors through setting up their environment, running the Docker container, executing tests, and running specific Python scripts.
