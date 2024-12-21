# splunk_acs_sdk.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UsersApi.md#create_user) | **POST** /{stack}/adminconfig/v2/users | 
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /{stack}/adminconfig/v2/users/{userName} | 
[**describe_user**](UsersApi.md#describe_user) | **GET** /{stack}/adminconfig/v2/users/{userName} | 
[**list_users**](UsersApi.md#list_users) | **GET** /{stack}/adminconfig/v2/users | 
[**patch_user**](UsersApi.md#patch_user) | **PATCH** /{stack}/adminconfig/v2/users/{userName} | 


# **create_user**
> UsersResponse create_user(stack, create_user_request, federated_search_manage_ack=federated_search_manage_ack)



create a new user

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.create_user_request import CreateUserRequest
from splunk_acs_sdk.models.users_response import UsersResponse
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
    api_instance = splunk_acs_sdk.UsersApi(api_client)
    stack = 'stack_example' # str | the stack name
    create_user_request = splunk_acs_sdk.CreateUserRequest() # CreateUserRequest | Create User Request Body
    federated_search_manage_ack = 'federated_search_manage_ack_example' # str | Set Federated-Search-Manage-Ack to 'Y' to acknowledge your acceptance that roles with fsh_manage capability can send search results data outside the compliant environment (optional)

    try:
        api_response = api_instance.create_user(stack, create_user_request, federated_search_manage_ack=federated_search_manage_ack)
        print("The response of UsersApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **create_user_request** | [**CreateUserRequest**](CreateUserRequest.md)| Create User Request Body | 
 **federated_search_manage_ack** | **str**| Set Federated-Search-Manage-Ack to &#39;Y&#39; to acknowledge your acceptance that roles with fsh_manage capability can send search results data outside the compliant environment | [optional] 

### Return type

[**UsersResponse**](UsersResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully created a new user |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(stack, user_name)



delete a specific user

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
    api_instance = splunk_acs_sdk.UsersApi(api_client)
    stack = 'stack_example' # str | the stack name
    user_name = 'user_name_example' # str | user name

    try:
        api_instance.delete_user(stack, user_name)
    except Exception as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **user_name** | **str**| user name | 

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
**200** | User Successfully deleted |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **describe_user**
> UsersResponse describe_user(stack, user_name)



describe a specific user

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.users_response import UsersResponse
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
    api_instance = splunk_acs_sdk.UsersApi(api_client)
    stack = 'stack_example' # str | the stack name
    user_name = 'user_name_example' # str | user name

    try:
        api_response = api_instance.describe_user(stack, user_name)
        print("The response of UsersApi->describe_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->describe_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **user_name** | **str**| user name | 

### Return type

[**UsersResponse**](UsersResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User Object Info |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> ListUsers200Response list_users(stack, count=count, offset=offset)



list all users

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.list_users200_response import ListUsers200Response
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
    api_instance = splunk_acs_sdk.UsersApi(api_client)
    stack = 'stack_example' # str | the stack name
    count = 30 # int | The maximum number of results to return. (optional) (default to 30)
    offset = 0 # int | The offset to start returning items from. (optional) (default to 0)

    try:
        api_response = api_instance.list_users(stack, count=count, offset=offset)
        print("The response of UsersApi->list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->list_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **count** | **int**| The maximum number of results to return. | [optional] [default to 30]
 **offset** | **int**| The offset to start returning items from. | [optional] [default to 0]

### Return type

[**ListUsers200Response**](ListUsers200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list of users |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_user**
> UsersResponse patch_user(stack, user_name, patch_user_request, federated_search_manage_ack=federated_search_manage_ack)



Modify a specific user on the stack

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.patch_user_request import PatchUserRequest
from splunk_acs_sdk.models.users_response import UsersResponse
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
    api_instance = splunk_acs_sdk.UsersApi(api_client)
    stack = 'stack_example' # str | the stack name
    user_name = 'user_name_example' # str | user name
    patch_user_request = splunk_acs_sdk.PatchUserRequest() # PatchUserRequest | Modify user object info
    federated_search_manage_ack = 'federated_search_manage_ack_example' # str | Set Federated-Search-Manage-Ack to 'Y' to acknowledge your acceptance that roles with fsh_manage capability can send search results data outside the compliant environment (optional)

    try:
        api_response = api_instance.patch_user(stack, user_name, patch_user_request, federated_search_manage_ack=federated_search_manage_ack)
        print("The response of UsersApi->patch_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->patch_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **user_name** | **str**| user name | 
 **patch_user_request** | [**PatchUserRequest**](PatchUserRequest.md)| Modify user object info | 
 **federated_search_manage_ack** | **str**| Set Federated-Search-Manage-Ack to &#39;Y&#39; to acknowledge your acceptance that roles with fsh_manage capability can send search results data outside the compliant environment | [optional] 

### Return type

[**UsersResponse**](UsersResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully modified a specific user |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

