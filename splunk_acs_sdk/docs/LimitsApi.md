# splunk_acs_sdk.LimitsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_limit_config**](LimitsApi.md#add_limit_config) | **POST** /{stack}/adminconfig/v2/limits/{stanza} | 
[**get_all_limits_config**](LimitsApi.md#get_all_limits_config) | **GET** /{stack}/adminconfig/v2/limits | 
[**get_all_limits_config_defaults**](LimitsApi.md#get_all_limits_config_defaults) | **GET** /{stack}/adminconfig/v2/limits/defaults | 
[**get_key_limit_config**](LimitsApi.md#get_key_limit_config) | **GET** /{stack}/adminconfig/v2/limits/{stanza}/{key} | 
[**get_limit_config**](LimitsApi.md#get_limit_config) | **GET** /{stack}/adminconfig/v2/limits/{stanza} | 
[**get_limits_config_defaults**](LimitsApi.md#get_limits_config_defaults) | **GET** /{stack}/adminconfig/v2/limits/{stanza}/defaults | 
[**reset_limit_config**](LimitsApi.md#reset_limit_config) | **POST** /{stack}/adminconfig/v2/limits/{stanza}/reset | 


# **add_limit_config**
> str add_limit_config(stack, stanza, limit_configuration_info)



add limit configuration to the stack

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.limit_configuration_info import LimitConfigurationInfo
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
    api_instance = splunk_acs_sdk.LimitsApi(api_client)
    stack = 'stack_example' # str | the stack name
    stanza = 'stanza_example' # str | stanza name
    limit_configuration_info = splunk_acs_sdk.LimitConfigurationInfo() # LimitConfigurationInfo | Limit Setting Info

    try:
        api_response = api_instance.add_limit_config(stack, stanza, limit_configuration_info)
        print("The response of LimitsApi->add_limit_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LimitsApi->add_limit_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **stanza** | **str**| stanza name | 
 **limit_configuration_info** | [**LimitConfigurationInfo**](LimitConfigurationInfo.md)| Limit Setting Info | 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | successfully submitted a limit configuration update |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_limits_config**
> get_all_limits_config(stack)



get all limits configuration from the stack

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
    api_instance = splunk_acs_sdk.LimitsApi(api_client)
    stack = 'stack_example' # str | the stack name

    try:
        api_instance.get_all_limits_config(stack)
    except Exception as e:
        print("Exception when calling LimitsApi->get_all_limits_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 

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
**200** | All Limits Configuration |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_limits_config_defaults**
> List[LimitStanza] get_all_limits_config_defaults(stack)



get default, minimum and maximum values for all limits configuration from the stack

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.limit_stanza import LimitStanza
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
    api_instance = splunk_acs_sdk.LimitsApi(api_client)
    stack = 'stack_example' # str | the stack name

    try:
        api_response = api_instance.get_all_limits_config_defaults(stack)
        print("The response of LimitsApi->get_all_limits_config_defaults:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LimitsApi->get_all_limits_config_defaults: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 

### Return type

[**List[LimitStanza]**](LimitStanza.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All Limits Configuration&#39;s default, mininimum, and maximum values |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_key_limit_config**
> GetLimitConfig200Response get_key_limit_config(stack, stanza, key)



get limit configuration from the stack

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.get_limit_config200_response import GetLimitConfig200Response
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
    api_instance = splunk_acs_sdk.LimitsApi(api_client)
    stack = 'stack_example' # str | the stack name
    stanza = 'stanza_example' # str | stanza name
    key = 'key_example' # str | key name

    try:
        api_response = api_instance.get_key_limit_config(stack, stanza, key)
        print("The response of LimitsApi->get_key_limit_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LimitsApi->get_key_limit_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **stanza** | **str**| stanza name | 
 **key** | **str**| key name | 

### Return type

[**GetLimitConfig200Response**](GetLimitConfig200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Limit Configuration |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_limit_config**
> GetLimitConfig200Response get_limit_config(stack, stanza)



get limit configuration from the stack

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.get_limit_config200_response import GetLimitConfig200Response
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
    api_instance = splunk_acs_sdk.LimitsApi(api_client)
    stack = 'stack_example' # str | the stack name
    stanza = 'stanza_example' # str | stanza name

    try:
        api_response = api_instance.get_limit_config(stack, stanza)
        print("The response of LimitsApi->get_limit_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LimitsApi->get_limit_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **stanza** | **str**| stanza name | 

### Return type

[**GetLimitConfig200Response**](GetLimitConfig200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Limit Configuration |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_limits_config_defaults**
> LimitStanza get_limits_config_defaults(stack, stanza)



get default, minimum, and maximum values for limit configuration from the stack

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.limit_stanza import LimitStanza
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
    api_instance = splunk_acs_sdk.LimitsApi(api_client)
    stack = 'stack_example' # str | the stack name
    stanza = 'stanza_example' # str | stanza name

    try:
        api_response = api_instance.get_limits_config_defaults(stack, stanza)
        print("The response of LimitsApi->get_limits_config_defaults:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LimitsApi->get_limits_config_defaults: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **stanza** | **str**| stanza name | 

### Return type

[**LimitStanza**](LimitStanza.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Limit Configuration&#39;s default, mininimum, and maximum values |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_limit_config**
> str reset_limit_config(stack, stanza, limit_reset_settings_list)



reset limit configuration on the stack

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.limit_reset_settings_list import LimitResetSettingsList
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
    api_instance = splunk_acs_sdk.LimitsApi(api_client)
    stack = 'stack_example' # str | the stack name
    stanza = 'stanza_example' # str | stanza name
    limit_reset_settings_list = splunk_acs_sdk.LimitResetSettingsList() # LimitResetSettingsList | Limit Setting Info

    try:
        api_response = api_instance.reset_limit_config(stack, stanza, limit_reset_settings_list)
        print("The response of LimitsApi->reset_limit_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LimitsApi->reset_limit_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **stanza** | **str**| stanza name | 
 **limit_reset_settings_list** | [**LimitResetSettingsList**](LimitResetSettingsList.md)| Limit Setting Info | 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | successfully submitted a reset limit configuration update |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

