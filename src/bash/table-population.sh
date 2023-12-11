#!/bin/bash
set -e

# Make sure AWS CLI is installed and configured with the necessary permissions

# Assigning command line arguments to variables
ENVIRONMENT=$1
ID=$2
QUERY=$3
QUERY_TYPE=$4
COMPLETION=$5
RESPONSE_ACCEPTED=${6:-false} # Default to false if not provided
ACCEPTANCE_TARGET=${7:-0.97} # Default to 0.97 if not provided
ACTUAL_RESPONSE=${8:-None} # Default to None if not provided

TABLE_NAME="legalese-ease-$ENVIRONMENT"

# Checking if required variables are set
: ${ENVIRONMENT:?Set to working environment}
: ${ID:?Set to ID}
: ${QUERY:?Set to AI Query}
: ${QUERY_TYPE:?Set to Query Type}
: ${COMPLETION:?Set to AI Response}

python src/python/QueryFormat.py "$ID" "$QUERY" "$COMPLETION" "$RESPONSE_ACCEPTED" "$ACCEPTANCE_TARGET" "$QUERY_TYPE" "$ACTUAL_RESPONSE" "$ENVIRONMENT"
