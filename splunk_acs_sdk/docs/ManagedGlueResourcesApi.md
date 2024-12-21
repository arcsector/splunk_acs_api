# splunk_acs_sdk.ManagedGlueResourcesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**describe_managed_glue_resources**](ManagedGlueResourcesApi.md#describe_managed_glue_resources) | **GET** /{stack}/adminconfig/v2/cloud-resources/managed-glue-resources | 
[**update_managed_glue_resources**](ManagedGlueResourcesApi.md#update_managed_glue_resources) | **PUT** /{stack}/adminconfig/v2/cloud-resources/managed-glue-resources | 


# **describe_managed_glue_resources**
> DescribeManagedGlueResources describe_managed_glue_resources(stack)



Describe cloud resources managed resources 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.describe_managed_glue_resources import DescribeManagedGlueResources
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
    api_instance = splunk_acs_sdk.ManagedGlueResourcesApi(api_client)
    stack = 'stack_example' # str | the stack name

    try:
        api_response = api_instance.describe_managed_glue_resources(stack)
        print("The response of ManagedGlueResourcesApi->describe_managed_glue_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedGlueResourcesApi->describe_managed_glue_resources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 

### Return type

[**DescribeManagedGlueResources**](DescribeManagedGlueResources.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully submitted a cloud resource permissions update |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_managed_glue_resources**
> str update_managed_glue_resources(stack, update_managed_glue_resources)



add cloud resource permissions for a set of federated providers

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.update_managed_glue_resources import UpdateManagedGlueResources
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
    api_instance = splunk_acs_sdk.ManagedGlueResourcesApi(api_client)
    stack = 'stack_example' # str | the stack name
    update_managed_glue_resources = splunk_acs_sdk.UpdateManagedGlueResources() # UpdateManagedGlueResources | The Federated Providers that will have their permissions updated

    try:
        api_response = api_instance.update_managed_glue_resources(stack, update_managed_glue_resources)
        print("The response of ManagedGlueResourcesApi->update_managed_glue_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedGlueResourcesApi->update_managed_glue_resources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **update_managed_glue_resources** | [**UpdateManagedGlueResources**](UpdateManagedGlueResources.md)| The Federated Providers that will have their permissions updated | 

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
**202** | successfully submitted a cloud resource permissions update |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

