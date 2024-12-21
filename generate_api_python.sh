#!/bin/bash

java -jar openapi-generator-cli.jar generate \
  -i openapi.json \
  -g python \
  --skip-validate-spec \
  -o splunk_acs_sdk \
  --package-name splunk_acs_sdk > generation_output.log
