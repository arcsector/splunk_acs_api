# splunk_acs_sdk.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_hec**](DefaultApi.md#create_hec) | **POST** /{stack}/adminconfig/v2/inputs/http-event-collectors | 
[**delete_hec**](DefaultApi.md#delete_hec) | **DELETE** /{stack}/adminconfig/v2/inputs/http-event-collectors/{hec} | 
[**describe_hec**](DefaultApi.md#describe_hec) | **GET** /{stack}/adminconfig/v2/inputs/http-event-collectors/{hec} | 
[**list_hecs**](DefaultApi.md#list_hecs) | **GET** /{stack}/adminconfig/v2/inputs/http-event-collectors | 
[**patch_hec**](DefaultApi.md#patch_hec) | **PATCH** /{stack}/adminconfig/v2/inputs/http-event-collectors/{hec} | 
[**update_hec**](DefaultApi.md#update_hec) | **PUT** /{stack}/adminconfig/v2/inputs/http-event-collectors/{hec} | 


# **create_hec**
> CreateHEC202Response create_hec(stack, hec_spec)



Create hec token for the stack

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.create_hec202_response import CreateHEC202Response
from splunk_acs_sdk.models.hec_spec import HecSpec
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
    api_instance = splunk_acs_sdk.DefaultApi(api_client)
    stack = 'stack_example' # str | the stack name
    hec_spec = splunk_acs_sdk.HecSpec() # HecSpec | Hec Info

    try:
        api_response = api_instance.create_hec(stack, hec_spec)
        print("The response of DefaultApi->create_hec:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_hec: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **hec_spec** | [**HecSpec**](HecSpec.md)| Hec Info | 

### Return type

[**CreateHEC202Response**](CreateHEC202Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | successfully submitted a new hec token |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_hec**
> str delete_hec(stack, hec, body)



delete HEC

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
    api_instance = splunk_acs_sdk.DefaultApi(api_client)
    stack = 'stack_example' # str | the stack name
    hec = 'hec_example' # str | hec name
    body = None # object | Name of the HEC Object to be deleted

    try:
        api_response = api_instance.delete_hec(stack, hec, body)
        print("The response of DefaultApi->delete_hec:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_hec: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **hec** | **str**| hec name | 
 **body** | **object**| Name of the HEC Object to be deleted | 

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
**202** | successfully submitted hec token deletion |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **describe_hec**
> DescribeHec200Response describe_hec(stack, hec)



Get detailed Info about a particular HEC

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.describe_hec200_response import DescribeHec200Response
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
    api_instance = splunk_acs_sdk.DefaultApi(api_client)
    stack = 'stack_example' # str | the stack name
    hec = 'hec_example' # str | hec name

    try:
        api_response = api_instance.describe_hec(stack, hec)
        print("The response of DefaultApi->describe_hec:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->describe_hec: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **hec** | **str**| hec name | 

### Return type

[**DescribeHec200Response**](DescribeHec200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hec Object Info |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_hecs**
> ListHECs200Response list_hecs(stack, count=count, offset=offset)



List of all HEC objects

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.list_hecs200_response import ListHECs200Response
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
    api_instance = splunk_acs_sdk.DefaultApi(api_client)
    stack = 'stack_example' # str | the stack name
    count = 30 # int | The maximum number of results to return. (optional) (default to 30)
    offset = 0 # int | The offset to start returning items from. (optional) (default to 0)

    try:
        api_response = api_instance.list_hecs(stack, count=count, offset=offset)
        print("The response of DefaultApi->list_hecs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_hecs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **count** | **int**| The maximum number of results to return. | [optional] [default to 30]
 **offset** | **int**| The offset to start returning items from. | [optional] [default to 0]

### Return type

[**ListHECs200Response**](ListHECs200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | fetch all hec info |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_hec**
> str patch_hec(stack, hec, hec_spec)



Modify properties of HEC

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.hec_spec import HecSpec
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
    api_instance = splunk_acs_sdk.DefaultApi(api_client)
    stack = 'stack_example' # str | the stack name
    hec = 'hec_example' # str | hec name
    hec_spec = splunk_acs_sdk.HecSpec() # HecSpec | Modify Hec object

    try:
        api_response = api_instance.patch_hec(stack, hec, hec_spec)
        print("The response of DefaultApi->patch_hec:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->patch_hec: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **hec** | **str**| hec name | 
 **hec_spec** | [**HecSpec**](HecSpec.md)| Modify Hec object | 

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
**202** | successfully submitted a hec token update |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_hec**
> str update_hec(stack, hec, hec_spec)



Modify properties of HEC

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.hec_spec import HecSpec
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
    api_instance = splunk_acs_sdk.DefaultApi(api_client)
    stack = 'stack_example' # str | the stack name
    hec = 'hec_example' # str | hec name
    hec_spec = splunk_acs_sdk.HecSpec() # HecSpec | Modify Hec object

    try:
        api_response = api_instance.update_hec(stack, hec, hec_spec)
        print("The response of DefaultApi->update_hec:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_hec: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **hec** | **str**| hec name | 
 **hec_spec** | [**HecSpec**](HecSpec.md)| Modify Hec object | 

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
**202** | successfully submitted a hec token update |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

