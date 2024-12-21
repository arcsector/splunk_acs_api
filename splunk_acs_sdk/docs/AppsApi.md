# splunk_acs_sdk.AppsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**describe_app**](AppsApi.md#describe_app) | **GET** /{stack}/adminconfig/v2/apps/{app} | 
[**install_app**](AppsApi.md#install_app) | **POST** /{stack}/adminconfig/v2/apps | 
[**list_apps**](AppsApi.md#list_apps) | **GET** /{stack}/adminconfig/v2/apps | 
[**uninstall_app**](AppsApi.md#uninstall_app) | **DELETE** /{stack}/adminconfig/v2/apps/{app} | 


# **describe_app**
> App describe_app(stack, app)



get an app

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
    api_instance = splunk_acs_sdk.AppsApi(api_client)
    stack = 'stack_example' # str | the stack name
    app = 'app_example' # str | the app name

    try:
        api_response = api_instance.describe_app(stack, app)
        print("The response of AppsApi->describe_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->describe_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **app** | **str**| the app name | 

### Return type

[**App**](App.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully retrieved an app |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **install_app**
> App install_app(stack, acs_legal_ack, splunkbase=splunkbase, x_splunkbase_authorization=x_splunkbase_authorization, x_splunk_authorization=x_splunk_authorization, acs_licensing_ack=acs_licensing_ack, package=package, token=token)



install an app

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
    api_instance = splunk_acs_sdk.AppsApi(api_client)
    stack = 'stack_example' # str | the stack name
    acs_legal_ack = 'acs_legal_ack_example' # str | ACS-Legal-Ack is required for installing private apps
    splunkbase = True # bool | is the app available in splunkbase (optional)
    x_splunkbase_authorization = 'x_splunkbase_authorization_example' # str | Splunkbase sessionID (optional)
    x_splunk_authorization = 'x_splunk_authorization_example' # str | The app inspect token (optional)
    acs_licensing_ack = 'acs_licensing_ack_example' # str | ACS-Licensing-Ack is required for installing splunkbase apps (optional)
    package = None # bytearray | the pre-approved app package file in tar.gz format (optional)
    token = 'token_example' # str | the splunkbase authentication token (optional)

    try:
        api_response = api_instance.install_app(stack, acs_legal_ack, splunkbase=splunkbase, x_splunkbase_authorization=x_splunkbase_authorization, x_splunk_authorization=x_splunk_authorization, acs_licensing_ack=acs_licensing_ack, package=package, token=token)
        print("The response of AppsApi->install_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->install_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **acs_legal_ack** | **str**| ACS-Legal-Ack is required for installing private apps | 
 **splunkbase** | **bool**| is the app available in splunkbase | [optional] 
 **x_splunkbase_authorization** | **str**| Splunkbase sessionID | [optional] 
 **x_splunk_authorization** | **str**| The app inspect token | [optional] 
 **acs_licensing_ack** | **str**| ACS-Licensing-Ack is required for installing splunkbase apps | [optional] 
 **package** | **bytearray**| the pre-approved app package file in tar.gz format | [optional] 
 **token** | **str**| the splunkbase authentication token | [optional] 

### Return type

[**App**](App.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully installed a new app |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_apps**
> ListApps200Response list_apps(stack, count=count, offset=offset, splunkbase=splunkbase)



list apps available on the stacks

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.list_apps200_response import ListApps200Response
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
    api_instance = splunk_acs_sdk.AppsApi(api_client)
    stack = 'stack_example' # str | the stack name
    count = 30 # int | The maximum number of results to return. (optional) (default to 30)
    offset = 0 # int | The offset to start returning items from. (optional) (default to 0)
    splunkbase = True # bool | filter apps based on splunkbase and non-splunkbase apps (optional)

    try:
        api_response = api_instance.list_apps(stack, count=count, offset=offset, splunkbase=splunkbase)
        print("The response of AppsApi->list_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->list_apps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **count** | **int**| The maximum number of results to return. | [optional] [default to 30]
 **offset** | **int**| The offset to start returning items from. | [optional] [default to 0]
 **splunkbase** | **bool**| filter apps based on splunkbase and non-splunkbase apps | [optional] 

### Return type

[**ListApps200Response**](ListApps200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully retrieved apps |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uninstall_app**
> uninstall_app(stack, app)



uninstall the app

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
    api_instance = splunk_acs_sdk.AppsApi(api_client)
    stack = 'stack_example' # str | the stack name
    app = 'app_example' # str | the app name

    try:
        api_instance.uninstall_app(stack, app)
    except Exception as e:
        print("Exception when calling AppsApi->uninstall_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **app** | **str**| the app name | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | successfully submitted a request to delete the app |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

