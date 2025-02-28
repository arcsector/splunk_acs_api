# splunk_acs_sdk.CapabilitiesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_capabilities**](CapabilitiesApi.md#list_capabilities) | **GET** /{stack}/adminconfig/v2/capabilities | 


# **list_capabilities**
> CapabilitiesInfo list_capabilities(stack, grantable_only=grantable_only)



list capabilities

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.capabilities_info import CapabilitiesInfo
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
    api_instance = splunk_acs_sdk.CapabilitiesApi(api_client)
    stack = 'stack_example' # str | the stack name
    grantable_only = True # bool | only show grantable capabilities (optional)

    try:
        api_response = api_instance.list_capabilities(stack, grantable_only=grantable_only)
        print("The response of CapabilitiesApi->list_capabilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CapabilitiesApi->list_capabilities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **grantable_only** | **bool**| only show grantable capabilities | [optional] 

### Return type

[**CapabilitiesInfo**](CapabilitiesInfo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list of capabilities |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

