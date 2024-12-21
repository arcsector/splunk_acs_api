# splunk_acs_sdk.EnablementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**describe_app_feature_enablement**](EnablementApi.md#describe_app_feature_enablement) | **GET** /{stack}/adminconfig/v2/enablement/{appGroup}/{featureName} | 
[**set_app_feature_enablement**](EnablementApi.md#set_app_feature_enablement) | **POST** /{stack}/adminconfig/v2/enablement/{appGroup}/{featureName} | 


# **describe_app_feature_enablement**
> AppFeatureEnablement describe_app_feature_enablement(stack, app_group, feature_name)



describe the enablement status of an app feature

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.app_feature_enablement import AppFeatureEnablement
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
    api_instance = splunk_acs_sdk.EnablementApi(api_client)
    stack = 'stack_example' # str | the stack name
    app_group = 'app_group_example' # str | the app name
    feature_name = 'feature_name_example' # str | the feature name

    try:
        api_response = api_instance.describe_app_feature_enablement(stack, app_group, feature_name)
        print("The response of EnablementApi->describe_app_feature_enablement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnablementApi->describe_app_feature_enablement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **app_group** | **str**| the app name | 
 **feature_name** | **str**| the feature name | 

### Return type

[**AppFeatureEnablement**](AppFeatureEnablement.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | describe the enablement status of an app feature |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_app_feature_enablement**
> AppFeatureEnablement set_app_feature_enablement(stack, app_group, feature_name, app_feature_enablement)



Enable or disable an app feature

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.app_feature_enablement import AppFeatureEnablement
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
    api_instance = splunk_acs_sdk.EnablementApi(api_client)
    stack = 'stack_example' # str | the stack name
    app_group = 'app_group_example' # str | the app name
    feature_name = 'feature_name_example' # str | the feature name
    app_feature_enablement = splunk_acs_sdk.AppFeatureEnablement() # AppFeatureEnablement | enablement

    try:
        api_response = api_instance.set_app_feature_enablement(stack, app_group, feature_name, app_feature_enablement)
        print("The response of EnablementApi->set_app_feature_enablement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnablementApi->set_app_feature_enablement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **app_group** | **str**| the app name | 
 **feature_name** | **str**| the feature name | 
 **app_feature_enablement** | [**AppFeatureEnablement**](AppFeatureEnablement.md)| enablement | 

### Return type

[**AppFeatureEnablement**](AppFeatureEnablement.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | returns whether the app feature has been enabled or disabled |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

