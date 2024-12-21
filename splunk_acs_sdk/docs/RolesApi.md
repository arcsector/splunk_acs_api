# splunk_acs_sdk.RolesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role**](RolesApi.md#create_role) | **POST** /{stack}/adminconfig/v2/roles | 
[**delete_role**](RolesApi.md#delete_role) | **DELETE** /{stack}/adminconfig/v2/roles/{roleName} | 
[**describe_role**](RolesApi.md#describe_role) | **GET** /{stack}/adminconfig/v2/roles/{roleName} | 
[**list_roles**](RolesApi.md#list_roles) | **GET** /{stack}/adminconfig/v2/roles | 
[**patch_role_info**](RolesApi.md#patch_role_info) | **PATCH** /{stack}/adminconfig/v2/roles/{roleName} | 


# **create_role**
> RolesResponse create_role(stack, post_roles_request, federated_search_manage_ack=federated_search_manage_ack)



create a new role on the stack

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.post_roles_request import PostRolesRequest
from splunk_acs_sdk.models.roles_response import RolesResponse
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
    api_instance = splunk_acs_sdk.RolesApi(api_client)
    stack = 'stack_example' # str | the stack name
    post_roles_request = splunk_acs_sdk.PostRolesRequest() # PostRolesRequest | Role Request Body
    federated_search_manage_ack = 'federated_search_manage_ack_example' # str | Set Federated-Search-Manage-Ack to 'Y' to acknowledge your acceptance that roles with fsh_manage capability can send search results data outside the compliant environment (optional)

    try:
        api_response = api_instance.create_role(stack, post_roles_request, federated_search_manage_ack=federated_search_manage_ack)
        print("The response of RolesApi->create_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->create_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **post_roles_request** | [**PostRolesRequest**](PostRolesRequest.md)| Role Request Body | 
 **federated_search_manage_ack** | **str**| Set Federated-Search-Manage-Ack to &#39;Y&#39; to acknowledge your acceptance that roles with fsh_manage capability can send search results data outside the compliant environment | [optional] 

### Return type

[**RolesResponse**](RolesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully created a new role |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> delete_role(stack, role_name)



delete a specific role

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
    api_instance = splunk_acs_sdk.RolesApi(api_client)
    stack = 'stack_example' # str | the stack name
    role_name = 'role_name_example' # str | role name

    try:
        api_instance.delete_role(stack, role_name)
    except Exception as e:
        print("Exception when calling RolesApi->delete_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **role_name** | **str**| role name | 

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
**200** | Role Successfully deleted |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **describe_role**
> RolesResponse describe_role(stack, role_name)



describe a specific role

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.roles_response import RolesResponse
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
    api_instance = splunk_acs_sdk.RolesApi(api_client)
    stack = 'stack_example' # str | the stack name
    role_name = 'role_name_example' # str | role name

    try:
        api_response = api_instance.describe_role(stack, role_name)
        print("The response of RolesApi->describe_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->describe_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **role_name** | **str**| role name | 

### Return type

[**RolesResponse**](RolesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Role Object Info |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_roles**
> ListRoles200Response list_roles(stack, count=count, offset=offset)



list all roles

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.list_roles200_response import ListRoles200Response
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
    api_instance = splunk_acs_sdk.RolesApi(api_client)
    stack = 'stack_example' # str | the stack name
    count = 30 # int | The maximum number of results to return. (optional) (default to 30)
    offset = 0 # int | The offset to start returning items from. (optional) (default to 0)

    try:
        api_response = api_instance.list_roles(stack, count=count, offset=offset)
        print("The response of RolesApi->list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->list_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **count** | **int**| The maximum number of results to return. | [optional] [default to 30]
 **offset** | **int**| The offset to start returning items from. | [optional] [default to 0]

### Return type

[**ListRoles200Response**](ListRoles200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list of roles |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_role_info**
> RolesResponse patch_role_info(stack, role_name, roles_request, federated_search_manage_ack=federated_search_manage_ack)



Modify a specific role on the stack

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.roles_request import RolesRequest
from splunk_acs_sdk.models.roles_response import RolesResponse
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
    api_instance = splunk_acs_sdk.RolesApi(api_client)
    stack = 'stack_example' # str | the stack name
    role_name = 'role_name_example' # str | role name
    roles_request = splunk_acs_sdk.RolesRequest() # RolesRequest | Modify role object info
    federated_search_manage_ack = 'federated_search_manage_ack_example' # str | Set Federated-Search-Manage-Ack to 'Y' to acknowledge your acceptance that roles with fsh_manage capability can send search results data outside the compliant environment (optional)

    try:
        api_response = api_instance.patch_role_info(stack, role_name, roles_request, federated_search_manage_ack=federated_search_manage_ack)
        print("The response of RolesApi->patch_role_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->patch_role_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **role_name** | **str**| role name | 
 **roles_request** | [**RolesRequest**](RolesRequest.md)| Modify role object info | 
 **federated_search_manage_ack** | **str**| Set Federated-Search-Manage-Ack to &#39;Y&#39; to acknowledge your acceptance that roles with fsh_manage capability can send search results data outside the compliant environment | [optional] 

### Return type

[**RolesResponse**](RolesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully modified a specific role role |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

