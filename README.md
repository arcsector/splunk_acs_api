# Splunk ACS API SDK Creation

The goal of this repo is to facilitate the easy creation of SDKs from an OpenAPIv3 spec from Splunk's ACS API spec.

## Prerequisites

The following need to be installed to build from source:

0. OpenJDK/Java
1. [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator)
2. Linux shell
3. wget

## How to Use

After installing the prerequisites above:

0. Execute the `get_api_spec.sh` file to grab the openapi spec file from Splunk.
1. After downloading, run the `generate_api_spec.sh` file to convert the openapi spec into python code
2. Optional: Install the sdk with `cd splunk_acs_sdk/; pip install .`
