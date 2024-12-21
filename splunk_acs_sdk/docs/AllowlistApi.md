# splunk_acs_sdk.AllowlistApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_subnets**](AllowlistApi.md#add_subnets) | **POST** /{stack}/adminconfig/v2/access/{feature}/ipallowlists | 
[**delete_subnet**](AllowlistApi.md#delete_subnet) | **DELETE** /{stack}/adminconfig/v2/access/{feature}/ipallowlists/{subnet} | 
[**delete_subnets**](AllowlistApi.md#delete_subnets) | **DELETE** /{stack}/adminconfig/v2/access/{feature}/ipallowlists | 
[**describe_allowlist**](AllowlistApi.md#describe_allowlist) | **GET** /{stack}/adminconfig/v2/access/{feature}/ipallowlists | 
[**describe_allowlist_v6**](AllowlistApi.md#describe_allowlist_v6) | **GET** /{stack}/adminconfig/v2/access/{feature}/ipallowlists-v6 | 


# **add_subnets**
> WarningResponse add_subnets(stack, feature, add_subnets_request)



add subnets to the allowlist for the feature, if they don't already exist

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.add_subnets_request import AddSubnetsRequest
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
    api_instance = splunk_acs_sdk.AllowlistApi(api_client)
    stack = 'stack_example' # str | the stack name
    feature = 'feature_example' # str | the feature the access rules apply towards
    add_subnets_request = splunk_acs_sdk.AddSubnetsRequest() # AddSubnetsRequest | the new subnets

    try:
        api_response = api_instance.add_subnets(stack, feature, add_subnets_request)
        print("The response of AllowlistApi->add_subnets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllowlistApi->add_subnets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **feature** | **str**| the feature the access rules apply towards | 
 **add_subnets_request** | [**AddSubnetsRequest**](AddSubnetsRequest.md)| the new subnets | 

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
**200** | accepted request to add a new forwarder ipallowlist |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subnet**
> WarningResponse delete_subnet(stack, feature, subnet)



delete an existing ip subnet if it exists, from where the feature is accessible from

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
    api_instance = splunk_acs_sdk.AllowlistApi(api_client)
    stack = 'stack_example' # str | the stack name
    feature = 'feature_example' # str | the feature the access rules apply towards
    subnet = 'subnet_example' # str | the subnet to be deleted

    try:
        api_response = api_instance.delete_subnet(stack, feature, subnet)
        print("The response of AllowlistApi->delete_subnet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllowlistApi->delete_subnet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **feature** | **str**| the feature the access rules apply towards | 
 **subnet** | **str**| the subnet to be deleted | 

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
**200** | accepted request to delete the forwarder ipallowlist |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subnets**
> WarningResponse delete_subnets(stack, feature, add_subnets_request)



delete existing ip subnets (if they exists) from where the splunk cloud stack feature is accessible from

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.add_subnets_request import AddSubnetsRequest
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
    api_instance = splunk_acs_sdk.AllowlistApi(api_client)
    stack = 'stack_example' # str | the stack name
    feature = 'feature_example' # str | the feature the access rules apply towards
    add_subnets_request = splunk_acs_sdk.AddSubnetsRequest() # AddSubnetsRequest | the subnets to be deleted

    try:
        api_response = api_instance.delete_subnets(stack, feature, add_subnets_request)
        print("The response of AllowlistApi->delete_subnets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllowlistApi->delete_subnets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **feature** | **str**| the feature the access rules apply towards | 
 **add_subnets_request** | [**AddSubnetsRequest**](AddSubnetsRequest.md)| the subnets to be deleted | 

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
**200** | accepted request to delete the forwarder ipallowlist |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **describe_allowlist**
> DescribeAllowlist200Response describe_allowlist(stack, feature)



describe the allowlist with its status and subnets from where the feature is accessible from

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.describe_allowlist200_response import DescribeAllowlist200Response
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
    api_instance = splunk_acs_sdk.AllowlistApi(api_client)
    stack = 'stack_example' # str | the stack name
    feature = 'feature_example' # str | the feature the access rules apply towards

    try:
        api_response = api_instance.describe_allowlist(stack, feature)
        print("The response of AllowlistApi->describe_allowlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllowlistApi->describe_allowlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **feature** | **str**| the feature the access rules apply towards | 

### Return type

[**DescribeAllowlist200Response**](DescribeAllowlist200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list of ip subnets |  -  |
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
    api_instance = splunk_acs_sdk.AllowlistApi(api_client)
    stack = 'stack_example' # str | the stack name
    feature = 'feature_example' # str | the feature the access rules apply towards

    try:
        api_response = api_instance.describe_allowlist_v6(stack, feature)
        print("The response of AllowlistApi->describe_allowlist_v6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllowlistApi->describe_allowlist_v6: %s\n" % e)
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

