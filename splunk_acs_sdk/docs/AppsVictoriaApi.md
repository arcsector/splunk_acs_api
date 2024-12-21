# splunk_acs_sdk.AppsVictoriaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**describe_app_victoria**](AppsVictoriaApi.md#describe_app_victoria) | **GET** /{stack}/adminconfig/v2/apps/victoria/{app} | 
[**download_app_export_victoria**](AppsVictoriaApi.md#download_app_export_victoria) | **GET** /{stack}/adminconfig/v2/apps/victoria/export/download/{app} | 
[**install_app_victoria**](AppsVictoriaApi.md#install_app_victoria) | **POST** /{stack}/adminconfig/v2/apps/victoria | 
[**list_apps_victoria**](AppsVictoriaApi.md#list_apps_victoria) | **GET** /{stack}/adminconfig/v2/apps/victoria | 
[**patch_app_victoria**](AppsVictoriaApi.md#patch_app_victoria) | **PATCH** /{stack}/adminconfig/v2/apps/victoria/{app} | 
[**uninstall_app_victoria**](AppsVictoriaApi.md#uninstall_app_victoria) | **DELETE** /{stack}/adminconfig/v2/apps/victoria/{app} | 


# **describe_app_victoria**
> App describe_app_victoria(stack, app)



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
    api_instance = splunk_acs_sdk.AppsVictoriaApi(api_client)
    stack = 'stack_example' # str | the stack name
    app = 'app_example' # str | the app name

    try:
        api_response = api_instance.describe_app_victoria(stack, app)
        print("The response of AppsVictoriaApi->describe_app_victoria:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsVictoriaApi->describe_app_victoria: %s\n" % e)
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

# **download_app_export_victoria**
> App download_app_export_victoria(stack, app, default=default, local=local, users=users, confs_only=confs_only)



fetch the app data and returns the selected contents as a tar file

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
    api_instance = splunk_acs_sdk.AppsVictoriaApi(api_client)
    stack = 'stack_example' # str | the stack name
    app = 'app_example' # str | the app name
    default = True # bool | export the default configs for the app etc/apps/<app_id>/default/* (optional)
    local = True # bool | export the local configs for the app under etc/apps/<app_id>/local/* (optional)
    users = True # bool | export the configs and data under etc/users/*/<app_id>/* for the users on which the requester has access over (optional)
    confs_only = True # bool | export only the configs as per request parameters and don’t export any app data (optional)

    try:
        api_response = api_instance.download_app_export_victoria(stack, app, default=default, local=local, users=users, confs_only=confs_only)
        print("The response of AppsVictoriaApi->download_app_export_victoria:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsVictoriaApi->download_app_export_victoria: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **app** | **str**| the app name | 
 **default** | **bool**| export the default configs for the app etc/apps/&lt;app_id&gt;/default/* | [optional] 
 **local** | **bool**| export the local configs for the app under etc/apps/&lt;app_id&gt;/local/* | [optional] 
 **users** | **bool**| export the configs and data under etc/users/*/&lt;app_id&gt;/* for the users on which the requester has access over | [optional] 
 **confs_only** | **bool**| export only the configs as per request parameters and don’t export any app data | [optional] 

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
**200** | successfully exported an app |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **install_app_victoria**
> App install_app_victoria(stack, splunkbase=splunkbase, x_splunkbase_authorization=x_splunkbase_authorization, x_splunk_authorization=x_splunk_authorization, acs_legal_ack=acs_legal_ack, acs_licensing_ack=acs_licensing_ack, splunkbase_id=splunkbase_id, version=version)



install an app for Victoria stack

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
    api_instance = splunk_acs_sdk.AppsVictoriaApi(api_client)
    stack = 'stack_example' # str | the stack name
    splunkbase = True # bool | is the app available in splunkbase (optional)
    x_splunkbase_authorization = 'x_splunkbase_authorization_example' # str | Splunkbase sessionID (optional)
    x_splunk_authorization = 'x_splunk_authorization_example' # str | The app inspect token (optional)
    acs_legal_ack = 'acs_legal_ack_example' # str | ACS-Legal-Ack is required for installing private apps (optional)
    acs_licensing_ack = 'acs_licensing_ack_example' # str | ACS-Licensing-Ack is required for installing splunkbase apps (optional)
    splunkbase_id = 'splunkbase_id_example' # str |  (optional)
    version = 'version_example' # str |  (optional)

    try:
        api_response = api_instance.install_app_victoria(stack, splunkbase=splunkbase, x_splunkbase_authorization=x_splunkbase_authorization, x_splunk_authorization=x_splunk_authorization, acs_legal_ack=acs_legal_ack, acs_licensing_ack=acs_licensing_ack, splunkbase_id=splunkbase_id, version=version)
        print("The response of AppsVictoriaApi->install_app_victoria:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsVictoriaApi->install_app_victoria: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **splunkbase** | **bool**| is the app available in splunkbase | [optional] 
 **x_splunkbase_authorization** | **str**| Splunkbase sessionID | [optional] 
 **x_splunk_authorization** | **str**| The app inspect token | [optional] 
 **acs_legal_ack** | **str**| ACS-Legal-Ack is required for installing private apps | [optional] 
 **acs_licensing_ack** | **str**| ACS-Licensing-Ack is required for installing splunkbase apps | [optional] 
 **splunkbase_id** | **str**|  | [optional] 
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
**200** | successfully installed a new app |  -  |
**202** | successfully submitted an install request of an app |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_apps_victoria**
> ListApps200Response list_apps_victoria(stack, count=count, offset=offset, splunkbase=splunkbase)



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
    api_instance = splunk_acs_sdk.AppsVictoriaApi(api_client)
    stack = 'stack_example' # str | the stack name
    count = 30 # int | The maximum number of results to return. (optional) (default to 30)
    offset = 0 # int | The offset to start returning items from. (optional) (default to 0)
    splunkbase = True # bool | filter apps based on splunkbase and non-splunkbase apps (optional)

    try:
        api_response = api_instance.list_apps_victoria(stack, count=count, offset=offset, splunkbase=splunkbase)
        print("The response of AppsVictoriaApi->list_apps_victoria:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsVictoriaApi->list_apps_victoria: %s\n" % e)
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

# **patch_app_victoria**
> App patch_app_victoria(stack, app, x_splunkbase_authorization, acs_licensing_ack, version=version)



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
    api_instance = splunk_acs_sdk.AppsVictoriaApi(api_client)
    stack = 'stack_example' # str | the stack name
    app = 'app_example' # str | the app name
    x_splunkbase_authorization = 'x_splunkbase_authorization_example' # str | The splunkbase sessionID
    acs_licensing_ack = 'acs_licensing_ack_example' # str | ACS-Licensing-Ack is required for updating splunkbase apps
    version = 'version_example' # str |  (optional)

    try:
        api_response = api_instance.patch_app_victoria(stack, app, x_splunkbase_authorization, acs_licensing_ack, version=version)
        print("The response of AppsVictoriaApi->patch_app_victoria:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsVictoriaApi->patch_app_victoria: %s\n" % e)
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

# **uninstall_app_victoria**
> uninstall_app_victoria(stack, app)



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
    api_instance = splunk_acs_sdk.AppsVictoriaApi(api_client)
    stack = 'stack_example' # str | the stack name
    app = 'app_example' # str | the app name

    try:
        api_instance.uninstall_app_victoria(stack, app)
    except Exception as e:
        print("Exception when calling AppsVictoriaApi->uninstall_app_victoria: %s\n" % e)
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
**200** | successfully deleted the app |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

