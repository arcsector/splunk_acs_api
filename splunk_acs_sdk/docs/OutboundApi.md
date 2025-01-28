# splunk_acs_sdk.OutboundApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_outboundports**](OutboundApi.md#add_outboundports) | **POST** /{stack}/adminconfig/v2/access/outbound-ports | 
[**create_outbound_ports_v6**](OutboundApi.md#create_outbound_ports_v6) | **POST** /{stack}/adminconfig/v2/access/outbound-ports-v6 | 
[**delete_outbound_port_v6**](OutboundApi.md#delete_outbound_port_v6) | **DELETE** /{stack}/adminconfig/v2/access/outbound-ports-v6/{port} | 
[**delete_outboundport**](OutboundApi.md#delete_outboundport) | **DELETE** /{stack}/adminconfig/v2/access/outbound-ports/{port} | 
[**describe_outboundports**](OutboundApi.md#describe_outboundports) | **GET** /{stack}/adminconfig/v2/access/outbound-ports/{port} | 
[**describe_outboundports_v6**](OutboundApi.md#describe_outboundports_v6) | **GET** /{stack}/adminconfig/v2/access/outbound-ports-v6/{port} | 
[**get_outboundports**](OutboundApi.md#get_outboundports) | **GET** /{stack}/adminconfig/v2/access/outbound-ports | 
[**list_outbound_ports_v6**](OutboundApi.md#list_outbound_ports_v6) | **GET** /{stack}/adminconfig/v2/access/outbound-ports-v6 | 


# **add_outboundports**
> WarningResponse add_outboundports(stack, add_outboundports_request)



add subnets to the outboundports for the feature, if they don't already exist

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.add_outboundports_request import AddOutboundportsRequest
from splunk_acs_sdk.models.warning_response import WarningResponse
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
    api_instance = splunk_acs_sdk.OutboundApi(api_client)
    stack = 'stack_example' # str | the stack name
    add_outboundports_request = splunk_acs_sdk.AddOutboundportsRequest() # AddOutboundportsRequest | the new subnets

    try:
        api_response = api_instance.add_outboundports(stack, add_outboundports_request)
        print("The response of OutboundApi->add_outboundports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutboundApi->add_outboundports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **add_outboundports_request** | [**AddOutboundportsRequest**](AddOutboundportsRequest.md)| the new subnets | 

### Return type

[**WarningResponse**](WarningResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | successfully submitted request to add an outbound port |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_outbound_ports_v6**
> WarningResponse create_outbound_ports_v6(stack, create_outbound_ports_v6_request)



add ipv6 subnets to the outboundports for the feature, if they don't already exist

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.create_outbound_ports_v6_request import CreateOutboundPortsV6Request
from splunk_acs_sdk.models.warning_response import WarningResponse
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
    api_instance = splunk_acs_sdk.OutboundApi(api_client)
    stack = 'stack_example' # str | the stack name
    create_outbound_ports_v6_request = splunk_acs_sdk.CreateOutboundPortsV6Request() # CreateOutboundPortsV6Request | the new ipv6 subnets

    try:
        api_response = api_instance.create_outbound_ports_v6(stack, create_outbound_ports_v6_request)
        print("The response of OutboundApi->create_outbound_ports_v6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutboundApi->create_outbound_ports_v6: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **create_outbound_ports_v6_request** | [**CreateOutboundPortsV6Request**](CreateOutboundPortsV6Request.md)| the new ipv6 subnets | 

### Return type

[**WarningResponse**](WarningResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | successfully submitted request to add an outbound port with ipv6 subnets |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_outbound_port_v6**
> delete_outbound_port_v6(stack, port, delete_outbound_port_v6_request)



delete an existing ipv6 outbound port if it exists, from where the feature is accessible from

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.delete_outbound_port_v6_request import DeleteOutboundPortV6Request
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
    api_instance = splunk_acs_sdk.OutboundApi(api_client)
    stack = 'stack_example' # str | the stack name
    port = 56 # int | the ipv6 outbound port to be deleted
    delete_outbound_port_v6_request = splunk_acs_sdk.DeleteOutboundPortV6Request() # DeleteOutboundPortV6Request | the ipv6 subnets to delete outbound ports for

    try:
        api_instance.delete_outbound_port_v6(stack, port, delete_outbound_port_v6_request)
    except Exception as e:
        print("Exception when calling OutboundApi->delete_outbound_port_v6: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **port** | **int**| the ipv6 outbound port to be deleted | 
 **delete_outbound_port_v6_request** | [**DeleteOutboundPortV6Request**](DeleteOutboundPortV6Request.md)| the ipv6 subnets to delete outbound ports for | 

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
**202** | successfully submitted request to delete ipv6 outbound port |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_outboundport**
> delete_outboundport(stack, port, delete_outboundport_request)



delete an existing outbound port if it exists, from where the feature is accessible from

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.delete_outboundport_request import DeleteOutboundportRequest
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
    api_instance = splunk_acs_sdk.OutboundApi(api_client)
    stack = 'stack_example' # str | the stack name
    port = 56 # int | the outbound port to be deleted
    delete_outboundport_request = splunk_acs_sdk.DeleteOutboundportRequest() # DeleteOutboundportRequest | the subnets to delete outbound ports for

    try:
        api_instance.delete_outboundport(stack, port, delete_outboundport_request)
    except Exception as e:
        print("Exception when calling OutboundApi->delete_outboundport: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **port** | **int**| the outbound port to be deleted | 
 **delete_outboundport_request** | [**DeleteOutboundportRequest**](DeleteOutboundportRequest.md)| the subnets to delete outbound ports for | 

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
**202** | successfully submitted request to delete outbound port |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **describe_outboundports**
> List[OutboundResponse] describe_outboundports(stack, port)



describe the outboundports with ports and subnets

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.outbound_response import OutboundResponse
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
    api_instance = splunk_acs_sdk.OutboundApi(api_client)
    stack = 'stack_example' # str | the stack name
    port = 56 # int | the outbound port to be deleted

    try:
        api_response = api_instance.describe_outboundports(stack, port)
        print("The response of OutboundApi->describe_outboundports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutboundApi->describe_outboundports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **port** | **int**| the outbound port to be deleted | 

### Return type

[**List[OutboundResponse]**](OutboundResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list of outbound ports |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **describe_outboundports_v6**
> List[OutboundResponse] describe_outboundports_v6(stack, port)



describe the outboundports with ports and ipv6 subnets

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.outbound_response import OutboundResponse
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
    api_instance = splunk_acs_sdk.OutboundApi(api_client)
    stack = 'stack_example' # str | the stack name
    port = 56 # int | the port on which we want to get the allowed ipv6 subnets

    try:
        api_response = api_instance.describe_outboundports_v6(stack, port)
        print("The response of OutboundApi->describe_outboundports_v6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutboundApi->describe_outboundports_v6: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **port** | **int**| the port on which we want to get the allowed ipv6 subnets | 

### Return type

[**List[OutboundResponse]**](OutboundResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list of outbound ports |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outboundports**
> List[OutboundResponse] get_outboundports(stack)



describe the outboundports with ports and subnets

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.outbound_response import OutboundResponse
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
    api_instance = splunk_acs_sdk.OutboundApi(api_client)
    stack = 'stack_example' # str | the stack name

    try:
        api_response = api_instance.get_outboundports(stack)
        print("The response of OutboundApi->get_outboundports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutboundApi->get_outboundports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 

### Return type

[**List[OutboundResponse]**](OutboundResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list of outbound ports |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_outbound_ports_v6**
> List[OutboundResponse] list_outbound_ports_v6(stack)



list the outboundports with ports and ipv6 subnets

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.outbound_response import OutboundResponse
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
    api_instance = splunk_acs_sdk.OutboundApi(api_client)
    stack = 'stack_example' # str | the stack name

    try:
        api_response = api_instance.list_outbound_ports_v6(stack)
        print("The response of OutboundApi->list_outbound_ports_v6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutboundApi->list_outbound_ports_v6: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 

### Return type

[**List[OutboundResponse]**](OutboundResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list of outbound ports with ipv6 subnets |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

