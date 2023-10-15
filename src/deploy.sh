#!/bin/bash

set -e

: ${OPENAI_API_KEY:?Set to API KEY value for OpenAI}

pushd /src
python3 data.py $OPENAI_API_KEY
popd
