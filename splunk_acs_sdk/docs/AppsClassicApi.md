# splunk_acs_sdk.AppsClassicApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**patch_app_classic**](AppsClassicApi.md#patch_app_classic) | **PATCH** /{stack}/adminconfig/v2/apps/{app} | 


# **patch_app_classic**
> App patch_app_classic(stack, app, x_splunkbase_authorization, acs_licensing_ack, version=version)



update an installed splunkbase apps

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.app import App
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
    api_instance = splunk_acs_sdk.AppsClassicApi(api_client)
    stack = 'stack_example' # str | the stack name
    app = 'app_example' # str | the app name
    x_splunkbase_authorization = 'x_splunkbase_authorization_example' # str | The splunkbase sessionID
    acs_licensing_ack = 'acs_licensing_ack_example' # str | ACS-Licensing-Ack is required for updating splunkbase apps
    version = 'version_example' # str |  (optional)

    try:
        api_response = api_instance.patch_app_classic(stack, app, x_splunkbase_authorization, acs_licensing_ack, version=version)
        print("The response of AppsClassicApi->patch_app_classic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsClassicApi->patch_app_classic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **app** | **str**| the app name | 
 **x_splunkbase_authorization** | **str**| The splunkbase sessionID | 
 **acs_licensing_ack** | **str**| ACS-Licensing-Ack is required for updating splunkbase apps | 
 **version** | **str**|  | [optional] 

### Return type

[**App**](App.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully updated an installed app |  -  |
**202** | successfully submitted an update to an installed app |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

