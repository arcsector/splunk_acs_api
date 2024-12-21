# splunk_acs_sdk.EMEKApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**describe_emek_waiver**](EMEKApi.md#describe_emek_waiver) | **GET** /{stack}/adminconfig/v2/emek/waiver | 
[**get_emek_policy**](EMEKApi.md#get_emek_policy) | **GET** /{stack}/adminconfig/v2/emek/key-policy | 
[**put_emek_key**](EMEKApi.md#put_emek_key) | **PUT** /{stack}/adminconfig/v2/emek/key | 


# **describe_emek_waiver**
> str describe_emek_waiver(stack)



Generate legal waiver for EMEK

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = splunk_acs_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = splunk_acs_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with splunk_acs_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = splunk_acs_sdk.EMEKApi(api_client)
    stack = 'stack_example' # str | the stack name

    try:
        api_response = api_instance.describe_emek_waiver(stack)
        print("The response of EMEKApi->describe_emek_waiver:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EMEKApi->describe_emek_waiver: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EMEK legal waiver |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_emek_policy**
> EmekPolicy get_emek_policy(stack, emek_legal_ack)



Generate the key policy for EMEK

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.emek_policy import EmekPolicy
from splunk_acs_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = splunk_acs_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = splunk_acs_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with splunk_acs_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = splunk_acs_sdk.EMEKApi(api_client)
    stack = 'stack_example' # str | the stack name
    emek_legal_ack = 'emek_legal_ack_example' # str | EMEK-Legal-Ack is required for generating key policy

    try:
        api_response = api_instance.get_emek_policy(stack, emek_legal_ack)
        print("The response of EMEKApi->get_emek_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EMEKApi->get_emek_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **emek_legal_ack** | **str**| EMEK-Legal-Ack is required for generating key policy | 

### Return type

[**EmekPolicy**](EmekPolicy.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | key policy response |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_emek_key**
> EmekKeyUploadResponse put_emek_key(stack, put_emek_key_request=put_emek_key_request)



EMEK Key upload

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.emek_key_upload_response import EmekKeyUploadResponse
from splunk_acs_sdk.models.put_emek_key_request import PutEmekKeyRequest
from splunk_acs_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = splunk_acs_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = splunk_acs_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with splunk_acs_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = splunk_acs_sdk.EMEKApi(api_client)
    stack = 'stack_example' # str | the stack name
    put_emek_key_request = splunk_acs_sdk.PutEmekKeyRequest() # PutEmekKeyRequest | Key ARN to be uploaded (optional)

    try:
        api_response = api_instance.put_emek_key(stack, put_emek_key_request=put_emek_key_request)
        print("The response of EMEKApi->put_emek_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EMEKApi->put_emek_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **put_emek_key_request** | [**PutEmekKeyRequest**](PutEmekKeyRequest.md)| Key ARN to be uploaded | [optional] 

### Return type

[**EmekKeyUploadResponse**](EmekKeyUploadResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | EMEK key upload accepted |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

