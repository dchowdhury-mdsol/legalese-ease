#!/bin/bash
set -e

# Make sure AWS CLI is installed and configured with the necessary permissions
: ${ENVIRONMENT:?Set to working environment}
TABLE_NAME="legalese-ease-$ENVIRONMENT"

# Setting all other required env vars
: ${ID:?Set to ID}
: ${QUERY:?Set to AI Query}
: ${QUERY_TYPE:?Set to Query Type}
: ${COMPLETION:?Set to AI Response}
: ${RESPONSE_ACCEPTED:=false} # Defaults response as accepted as false, will be true if reviewed by lawyer
: ${ACCEPTANCE_TARGET:=0.97} # Default current GPT 3.5 acceptance targets
: ${ACTUAL_RESPONSE:=None} # Default will set to None for actual response and assume query response is accepted


python src/python/QueryFormat.py "$ID" "$QUERY" "$COMPLETION" "$RESPONSE_ACCEPTED" "$ACCEPTANCE_TARGET" "$QUERY_TYPE" "$ACTUAL_RESPONSE" "$ENVIRONMENT"
