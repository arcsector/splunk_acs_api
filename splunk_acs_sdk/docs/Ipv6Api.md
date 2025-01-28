# splunk_acs_sdk.Ipv6Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_allowlist_v6**](Ipv6Api.md#create_allowlist_v6) | **POST** /{stack}/adminconfig/v2/access/{feature}/ipallowlists-v6 | 
[**create_outbound_ports_v6**](Ipv6Api.md#create_outbound_ports_v6) | **POST** /{stack}/adminconfig/v2/access/outbound-ports-v6 | 
[**delete_allowlist_v6**](Ipv6Api.md#delete_allowlist_v6) | **DELETE** /{stack}/adminconfig/v2/access/{feature}/ipallowlists-v6/{subnet} | 
[**delete_allowlists_v6**](Ipv6Api.md#delete_allowlists_v6) | **DELETE** /{stack}/adminconfig/v2/access/{feature}/ipallowlists-v6 | 
[**delete_outbound_port_v6**](Ipv6Api.md#delete_outbound_port_v6) | **DELETE** /{stack}/adminconfig/v2/access/outbound-ports-v6/{port} | 
[**describe_allowlist_v6**](Ipv6Api.md#describe_allowlist_v6) | **GET** /{stack}/adminconfig/v2/access/{feature}/ipallowlists-v6 | 
[**describe_outboundports_v6**](Ipv6Api.md#describe_outboundports_v6) | **GET** /{stack}/adminconfig/v2/access/outbound-ports-v6/{port} | 
[**list_outbound_ports_v6**](Ipv6Api.md#list_outbound_ports_v6) | **GET** /{stack}/adminconfig/v2/access/outbound-ports-v6 | 


# **create_allowlist_v6**
> WarningResponse create_allowlist_v6(stack, feature, delete_outbound_port_v6_request)



add ipv6 subnets to the allowlist for the feature, if they don't already exist

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.delete_outbound_port_v6_request import DeleteOutboundPortV6Request
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
    api_instance = splunk_acs_sdk.Ipv6Api(api_client)
    stack = 'stack_example' # str | the stack name
    feature = 'feature_example' # str | the feature the access rules apply towards
    delete_outbound_port_v6_request = splunk_acs_sdk.DeleteOutboundPortV6Request() # DeleteOutboundPortV6Request | the new subnets

    try:
        api_response = api_instance.create_allowlist_v6(stack, feature, delete_outbound_port_v6_request)
        print("The response of Ipv6Api->create_allowlist_v6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Ipv6Api->create_allowlist_v6: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **feature** | **str**| the feature the access rules apply towards | 
 **delete_outbound_port_v6_request** | [**DeleteOutboundPortV6Request**](DeleteOutboundPortV6Request.md)| the new subnets | 

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
**200** | accepted request to add new ipv6 allowlist |  -  |
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
    api_instance = splunk_acs_sdk.Ipv6Api(api_client)
    stack = 'stack_example' # str | the stack name
    create_outbound_ports_v6_request = splunk_acs_sdk.CreateOutboundPortsV6Request() # CreateOutboundPortsV6Request | the new ipv6 subnets

    try:
        api_response = api_instance.create_outbound_ports_v6(stack, create_outbound_ports_v6_request)
        print("The response of Ipv6Api->create_outbound_ports_v6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Ipv6Api->create_outbound_ports_v6: %s\n" % e)
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

# **delete_allowlist_v6**
> WarningResponse delete_allowlist_v6(stack, feature, subnet)



delete an existing ipv6 subnet if it exists, from where the feature is accessible from

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
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
    api_instance = splunk_acs_sdk.Ipv6Api(api_client)
    stack = 'stack_example' # str | the stack name
    feature = 'feature_example' # str | the feature the access rules apply towards
    subnet = 'subnet_example' # str | the ipv6 subnet to be deleted

    try:
        api_response = api_instance.delete_allowlist_v6(stack, feature, subnet)
        print("The response of Ipv6Api->delete_allowlist_v6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Ipv6Api->delete_allowlist_v6: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **feature** | **str**| the feature the access rules apply towards | 
 **subnet** | **str**| the ipv6 subnet to be deleted | 

### Return type

[**WarningResponse**](WarningResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | accepted request to delete the ipv6 allowlist |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_allowlists_v6**
> WarningResponse delete_allowlists_v6(stack, feature, delete_outbound_port_v6_request)



delete existing ipv6 subnets (if they exists) from where the splunk cloud stack feature is accessible from

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.delete_outbound_port_v6_request import DeleteOutboundPortV6Request
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
    api_instance = splunk_acs_sdk.Ipv6Api(api_client)
    stack = 'stack_example' # str | the stack name
    feature = 'feature_example' # str | the feature the access rules apply towards
    delete_outbound_port_v6_request = splunk_acs_sdk.DeleteOutboundPortV6Request() # DeleteOutboundPortV6Request | the ipv6 subnets to be deleted

    try:
        api_response = api_instance.delete_allowlists_v6(stack, feature, delete_outbound_port_v6_request)
        print("The response of Ipv6Api->delete_allowlists_v6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Ipv6Api->delete_allowlists_v6: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **feature** | **str**| the feature the access rules apply towards | 
 **delete_outbound_port_v6_request** | [**DeleteOutboundPortV6Request**](DeleteOutboundPortV6Request.md)| the ipv6 subnets to be deleted | 

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
**200** | accepted request to delete the ipv6 allowlist |  -  |
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
    api_instance = splunk_acs_sdk.Ipv6Api(api_client)
    stack = 'stack_example' # str | the stack name
    port = 56 # int | the ipv6 outbound port to be deleted
    delete_outbound_port_v6_request = splunk_acs_sdk.DeleteOutboundPortV6Request() # DeleteOutboundPortV6Request | the ipv6 subnets to delete outbound ports for

    try:
        api_instance.delete_outbound_port_v6(stack, port, delete_outbound_port_v6_request)
    except Exception as e:
        print("Exception when calling Ipv6Api->delete_outbound_port_v6: %s\n" % e)
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

# **describe_allowlist_v6**
> DescribeAllowlistV6200Response describe_allowlist_v6(stack, feature)



describe the allowlist with its status and ipv6 subnets from where the feature is accessible from

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.describe_allowlist_v6200_response import DescribeAllowlistV6200Response
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
    api_instance = splunk_acs_sdk.Ipv6Api(api_client)
    stack = 'stack_example' # str | the stack name
    feature = 'feature_example' # str | the feature the access rules apply towards

    try:
        api_response = api_instance.describe_allowlist_v6(stack, feature)
        print("The response of Ipv6Api->describe_allowlist_v6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Ipv6Api->describe_allowlist_v6: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **feature** | **str**| the feature the access rules apply towards | 

### Return type

[**DescribeAllowlistV6200Response**](DescribeAllowlistV6200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list of ipv6 subnets |  -  |
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
    api_instance = splunk_acs_sdk.Ipv6Api(api_client)
    stack = 'stack_example' # str | the stack name
    port = 56 # int | the port on which we want to get the allowed ipv6 subnets

    try:
        api_response = api_instance.describe_outboundports_v6(stack, port)
        print("The response of Ipv6Api->describe_outboundports_v6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Ipv6Api->describe_outboundports_v6: %s\n" % e)
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
    api_instance = splunk_acs_sdk.Ipv6Api(api_client)
    stack = 'stack_example' # str | the stack name

    try:
        api_response = api_instance.list_outbound_ports_v6(stack)
        print("The response of Ipv6Api->list_outbound_ports_v6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Ipv6Api->list_outbound_ports_v6: %s\n" % e)
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

