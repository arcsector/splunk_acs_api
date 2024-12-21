# splunk_acs_sdk.PermissionsAppsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**describe_permissions_apps**](PermissionsAppsApi.md#describe_permissions_apps) | **GET** /{stack}/adminconfig/v2/permissions/apps/{app} | 
[**list_permissions_apps**](PermissionsAppsApi.md#list_permissions_apps) | **GET** /{stack}/adminconfig/v2/permissions/apps | 
[**patch_permissions_apps**](PermissionsAppsApi.md#patch_permissions_apps) | **PATCH** /{stack}/adminconfig/v2/permissions/apps/{app} | 


# **describe_permissions_apps**
> AppPerms describe_permissions_apps(stack, app)



get an apps permissions

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.app_perms import AppPerms
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
    api_instance = splunk_acs_sdk.PermissionsAppsApi(api_client)
    stack = 'stack_example' # str | the stack name
    app = 'app_example' # str | the app name

    try:
        api_response = api_instance.describe_permissions_apps(stack, app)
        print("The response of PermissionsAppsApi->describe_permissions_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsAppsApi->describe_permissions_apps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **app** | **str**| the app name | 

### Return type

[**AppPerms**](AppPerms.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully retrieved an apps permissions |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_permissions_apps**
> ListPermissionsApps200Response list_permissions_apps(stack, count=count, offset=offset)



List permissions of all apps

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.list_permissions_apps200_response import ListPermissionsApps200Response
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
    api_instance = splunk_acs_sdk.PermissionsAppsApi(api_client)
    stack = 'stack_example' # str | the stack name
    count = 30 # int | The maximum number of results to return. (optional) (default to 30)
    offset = 0 # int | The offset to start returning items from. (optional) (default to 0)

    try:
        api_response = api_instance.list_permissions_apps(stack, count=count, offset=offset)
        print("The response of PermissionsAppsApi->list_permissions_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionsAppsApi->list_permissions_apps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **count** | **int**| The maximum number of results to return. | [optional] [default to 30]
 **offset** | **int**| The offset to start returning items from. | [optional] [default to 0]

### Return type

[**ListPermissionsApps200Response**](ListPermissionsApps200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully List Apps Permissions |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_permissions_apps**
> patch_permissions_apps(stack, app, patch_app_perms_request)



Modify an app's permissions

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.patch_app_perms_request import PatchAppPermsRequest
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
    api_instance = splunk_acs_sdk.PermissionsAppsApi(api_client)
    stack = 'stack_example' # str | the stack name
    app = 'app_example' # str | the app name
    patch_app_perms_request = splunk_acs_sdk.PatchAppPermsRequest() # PatchAppPermsRequest | Modify app permissions

    try:
        api_instance.patch_permissions_apps(stack, app, patch_app_perms_request)
    except Exception as e:
        print("Exception when calling PermissionsAppsApi->patch_permissions_apps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **app** | **str**| the app name | 
 **patch_app_perms_request** | [**PatchAppPermsRequest**](PatchAppPermsRequest.md)| Modify app permissions | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully submitted app permissions update |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

