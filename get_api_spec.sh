#!/bin/bash

curl https://admin.splunk.com/service/info/specs/v2/openapi.json | jq . > openapi.json
