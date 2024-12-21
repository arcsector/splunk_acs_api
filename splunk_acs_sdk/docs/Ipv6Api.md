# splunk_acs_sdk.Ipv6Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**describe_allowlist_v6**](Ipv6Api.md#describe_allowlist_v6) | **GET** /{stack}/adminconfig/v2/access/{feature}/ipallowlists-v6 | 


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

