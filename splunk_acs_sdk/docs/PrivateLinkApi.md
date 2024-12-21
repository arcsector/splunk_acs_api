# splunk_acs_sdk.PrivateLinkApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**describe_private_connectivity**](PrivateLinkApi.md#describe_private_connectivity) | **GET** /{stack}/adminconfig/v2/private-connectivity/endpoints | 
[**enable_private_connectivity**](PrivateLinkApi.md#enable_private_connectivity) | **POST** /{stack}/adminconfig/v2/private-connectivity/endpoints | 
[**update_private_connectivity**](PrivateLinkApi.md#update_private_connectivity) | **PATCH** /{stack}/adminconfig/v2/private-connectivity/endpoints | 
[**validate_private_connectivity**](PrivateLinkApi.md#validate_private_connectivity) | **GET** /{stack}/adminconfig/v2/private-connectivity/eligibility | 


# **describe_private_connectivity**
> DescribePrivateConnectivity describe_private_connectivity(stack, feature=feature)



describes the status, customerAccountIds and endpoint name

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.describe_private_connectivity import DescribePrivateConnectivity
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
    api_instance = splunk_acs_sdk.PrivateLinkApi(api_client)
    stack = 'stack_example' # str | the stack name
    feature = 'feature_example' # str | select which feature endpoint tried to retrieve, supported feature: search, ingest. show all if no feature specified (optional)

    try:
        api_response = api_instance.describe_private_connectivity(stack, feature=feature)
        print("The response of PrivateLinkApi->describe_private_connectivity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateLinkApi->describe_private_connectivity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **feature** | **str**| select which feature endpoint tried to retrieve, supported feature: search, ingest. show all if no feature specified | [optional] 

### Return type

[**DescribePrivateConnectivity**](DescribePrivateConnectivity.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | display status, customerAccountIds and endpoint name if private connectivity is enabled. if private connectivity is disabled status and reason are displayed |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_private_connectivity**
> EnablePrivateConnectivity enable_private_connectivity(stack, enable_private_connectivity)



enables private connectivity and adds provided customerAccountIds to the private network

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.enable_private_connectivity import EnablePrivateConnectivity
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
    api_instance = splunk_acs_sdk.PrivateLinkApi(api_client)
    stack = 'stack_example' # str | the stack name
    enable_private_connectivity = splunk_acs_sdk.EnablePrivateConnectivity() # EnablePrivateConnectivity | Customer AccountIds

    try:
        api_response = api_instance.enable_private_connectivity(stack, enable_private_connectivity)
        print("The response of PrivateLinkApi->enable_private_connectivity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateLinkApi->enable_private_connectivity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **enable_private_connectivity** | [**EnablePrivateConnectivity**](EnablePrivateConnectivity.md)| Customer AccountIds | 

### Return type

[**EnablePrivateConnectivity**](EnablePrivateConnectivity.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | returns customerAccountIds that were added to the private network |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_private_connectivity**
> UpdatePrivateConnectivity update_private_connectivity(stack, enable_private_connectivity)



updates private connectivity and patches provided customerAccountIds to the private network

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.enable_private_connectivity import EnablePrivateConnectivity
from splunk_acs_sdk.models.update_private_connectivity import UpdatePrivateConnectivity
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
    api_instance = splunk_acs_sdk.PrivateLinkApi(api_client)
    stack = 'stack_example' # str | the stack name
    enable_private_connectivity = splunk_acs_sdk.EnablePrivateConnectivity() # EnablePrivateConnectivity | Customer AccountIds

    try:
        api_response = api_instance.update_private_connectivity(stack, enable_private_connectivity)
        print("The response of PrivateLinkApi->update_private_connectivity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateLinkApi->update_private_connectivity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **enable_private_connectivity** | [**EnablePrivateConnectivity**](EnablePrivateConnectivity.md)| Customer AccountIds | 

### Return type

[**UpdatePrivateConnectivity**](UpdatePrivateConnectivity.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | returns customerAccountIds that were added to the private network |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_private_connectivity**
> DescribeEligibilityPrivateConnectivity validate_private_connectivity(stack)



describe the eligibility of stack for enabling private connectivity

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.describe_eligibility_private_connectivity import DescribeEligibilityPrivateConnectivity
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
    api_instance = splunk_acs_sdk.PrivateLinkApi(api_client)
    stack = 'stack_example' # str | the stack name

    try:
        api_response = api_instance.validate_private_connectivity(stack)
        print("The response of PrivateLinkApi->validate_private_connectivity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateLinkApi->validate_private_connectivity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 

### Return type

[**DescribeEligibilityPrivateConnectivity**](DescribeEligibilityPrivateConnectivity.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | display eligibility of the stack for enabling private connectivity |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

