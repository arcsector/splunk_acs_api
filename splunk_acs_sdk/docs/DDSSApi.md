# splunk_acs_sdk.DDSSApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_self_storage_location**](DDSSApi.md#create_self_storage_location) | **POST** /{stack}/adminconfig/v2/cloud-resources/self-storage-locations/buckets | 
[**describe_self_storage_location**](DDSSApi.md#describe_self_storage_location) | **GET** /{stack}/adminconfig/v2/cloud-resources/self-storage-locations/buckets/{bucketPath} | 
[**get_self_storage_location_policy**](DDSSApi.md#get_self_storage_location_policy) | **GET** /{stack}/adminconfig/v2/cloud-resources/self-storage-locations/buckets/{bucketName}/policy | 
[**get_self_storage_location_prefix**](DDSSApi.md#get_self_storage_location_prefix) | **GET** /{stack}/adminconfig/v2/cloud-resources/self-storage-locations/configs/prefix | 
[**get_self_storage_location_service_accounts**](DDSSApi.md#get_self_storage_location_service_accounts) | **GET** /{stack}/adminconfig/v2/cloud-resources/self-storage-locations/configs/service-accounts | 
[**list_self_storage_locations**](DDSSApi.md#list_self_storage_locations) | **GET** /{stack}/adminconfig/v2/cloud-resources/self-storage-locations/buckets | 


# **create_self_storage_location**
> SelfStorageLocationInfo create_self_storage_location(stack, self_storage_location_body)



Create self storage location on the stack

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.self_storage_location_body import SelfStorageLocationBody
from splunk_acs_sdk.models.self_storage_location_info import SelfStorageLocationInfo
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
    api_instance = splunk_acs_sdk.DDSSApi(api_client)
    stack = 'stack_example' # str | the stack name
    self_storage_location_body = splunk_acs_sdk.SelfStorageLocationBody() # SelfStorageLocationBody | Self Storage Location Info

    try:
        api_response = api_instance.create_self_storage_location(stack, self_storage_location_body)
        print("The response of DDSSApi->create_self_storage_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DDSSApi->create_self_storage_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **self_storage_location_body** | [**SelfStorageLocationBody**](SelfStorageLocationBody.md)| Self Storage Location Info | 

### Return type

[**SelfStorageLocationInfo**](SelfStorageLocationInfo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | successfully submitted a new self storage location |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **describe_self_storage_location**
> SelfStorageLocationInfo describe_self_storage_location(stack, bucket_path)



Describe a configured self storage location on the stack

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.self_storage_location_info import SelfStorageLocationInfo
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
    api_instance = splunk_acs_sdk.DDSSApi(api_client)
    stack = 'stack_example' # str | the stack name
    bucket_path = 'bucket_path_example' # str | bucket path of the self storage location

    try:
        api_response = api_instance.describe_self_storage_location(stack, bucket_path)
        print("The response of DDSSApi->describe_self_storage_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DDSSApi->describe_self_storage_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **bucket_path** | **str**| bucket path of the self storage location | 

### Return type

[**SelfStorageLocationInfo**](SelfStorageLocationInfo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully describe a specific self storage location |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self_storage_location_policy**
> SelfStorageLocationPolicy get_self_storage_location_policy(stack, bucket_name)



Get the IAM policy to configure S3 bucket for self storage location

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.self_storage_location_policy import SelfStorageLocationPolicy
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
    api_instance = splunk_acs_sdk.DDSSApi(api_client)
    stack = 'stack_example' # str | the stack name
    bucket_name = 'bucket_name_example' # str | bucket for self storage location

    try:
        api_response = api_instance.get_self_storage_location_policy(stack, bucket_name)
        print("The response of DDSSApi->get_self_storage_location_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DDSSApi->get_self_storage_location_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **bucket_name** | **str**| bucket for self storage location | 

### Return type

[**SelfStorageLocationPolicy**](SelfStorageLocationPolicy.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | self storage policy response |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self_storage_location_prefix**
> SelfStorageLocationPrefix get_self_storage_location_prefix(stack)



Get the bucket prefix required to configure self storage location(s)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.self_storage_location_prefix import SelfStorageLocationPrefix
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
    api_instance = splunk_acs_sdk.DDSSApi(api_client)
    stack = 'stack_example' # str | the stack name

    try:
        api_response = api_instance.get_self_storage_location_prefix(stack)
        print("The response of DDSSApi->get_self_storage_location_prefix:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DDSSApi->get_self_storage_location_prefix: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 

### Return type

[**SelfStorageLocationPrefix**](SelfStorageLocationPrefix.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | self storage location response |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self_storage_location_service_accounts**
> SelfStorageLocationServiceAccountsResponse get_self_storage_location_service_accounts(stack)



Get the service account for GCS bucket required to configure self storage location(s)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.self_storage_location_service_accounts_response import SelfStorageLocationServiceAccountsResponse
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
    api_instance = splunk_acs_sdk.DDSSApi(api_client)
    stack = 'stack_example' # str | the stack name

    try:
        api_response = api_instance.get_self_storage_location_service_accounts(stack)
        print("The response of DDSSApi->get_self_storage_location_service_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DDSSApi->get_self_storage_location_service_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 

### Return type

[**SelfStorageLocationServiceAccountsResponse**](SelfStorageLocationServiceAccountsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | self storage service account response |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_self_storage_locations**
> ListSelfStorageLocations200Response list_self_storage_locations(stack, count=count, offset=offset)



List all configured self storage locations on the stack

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.list_self_storage_locations200_response import ListSelfStorageLocations200Response
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
    api_instance = splunk_acs_sdk.DDSSApi(api_client)
    stack = 'stack_example' # str | the stack name
    count = 30 # int | The maximum number of results to return. (optional) (default to 30)
    offset = 0 # int | The offset to start returning items from. (optional) (default to 0)

    try:
        api_response = api_instance.list_self_storage_locations(stack, count=count, offset=offset)
        print("The response of DDSSApi->list_self_storage_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DDSSApi->list_self_storage_locations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **count** | **int**| The maximum number of results to return. | [optional] [default to 30]
 **offset** | **int**| The offset to start returning items from. | [optional] [default to 0]

### Return type

[**ListSelfStorageLocations200Response**](ListSelfStorageLocations200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list of available self storage locations |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

