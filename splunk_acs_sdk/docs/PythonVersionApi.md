# splunk_acs_sdk.PythonVersionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_python_version**](PythonVersionApi.md#change_python_version) | **POST** /{stack}/adminconfig/v2/python-runtime | 


# **change_python_version**
> PythonVersionResponse change_python_version(stack, change_python_version_request)



Change python version on co2 stack spec

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.change_python_version_request import ChangePythonVersionRequest
from splunk_acs_sdk.models.python_version_response import PythonVersionResponse
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
    api_instance = splunk_acs_sdk.PythonVersionApi(api_client)
    stack = 'stack_example' # str | the stack name
    change_python_version_request = splunk_acs_sdk.ChangePythonVersionRequest() # ChangePythonVersionRequest | python version flag

    try:
        api_response = api_instance.change_python_version(stack, change_python_version_request)
        print("The response of PythonVersionApi->change_python_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PythonVersionApi->change_python_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **change_python_version_request** | [**ChangePythonVersionRequest**](ChangePythonVersionRequest.md)| python version flag | 

### Return type

[**PythonVersionResponse**](PythonVersionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | successfully set python version on stack spec |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

