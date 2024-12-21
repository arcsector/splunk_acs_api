# splunk_acs_sdk.MaintenanceWindowsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**audit_maintenance_windows_schedule**](MaintenanceWindowsApi.md#audit_maintenance_windows_schedule) | **GET** /{stack}/adminconfig/v2/maintenance-windows/schedules/{scheduleID}/audits | 
[**describe_maintenance_windows_preferences**](MaintenanceWindowsApi.md#describe_maintenance_windows_preferences) | **GET** /{stack}/adminconfig/v2/maintenance-windows/preferences | 
[**describe_maintenance_windows_schedule**](MaintenanceWindowsApi.md#describe_maintenance_windows_schedule) | **GET** /{stack}/adminconfig/v2/maintenance-windows/schedules/{scheduleID} | 
[**list_maintenance_windows_schedules**](MaintenanceWindowsApi.md#list_maintenance_windows_schedules) | **GET** /{stack}/adminconfig/v2/maintenance-windows/schedules | 
[**update_maintenance_windows_preferences**](MaintenanceWindowsApi.md#update_maintenance_windows_preferences) | **PUT** /{stack}/adminconfig/v2/maintenance-windows/preferences | 


# **audit_maintenance_windows_schedule**
> List[MaintenanceWindowsAuditResponse] audit_maintenance_windows_schedule(stack, schedule_id, from_time=from_time, to_time=to_time)



Audit status changes for a specific maintenance window schedule.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.maintenance_windows_audit_response import MaintenanceWindowsAuditResponse
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
    api_instance = splunk_acs_sdk.MaintenanceWindowsApi(api_client)
    stack = 'stack_example' # str | the stack name
    schedule_id = 'schedule_id_example' # str | The maintenance window schedule ID.
    from_time = 'from_time_example' # str | The earliest time to return results from. Format is expected to be YYYY-MM-DD or in RFC3339. UTC is the default timezone. (optional)
    to_time = 'to_time_example' # str | The latest time to return results from. Format is expected to be YYYY-MM-DD or in RFC3339. UTC is the default timezone. (optional)

    try:
        api_response = api_instance.audit_maintenance_windows_schedule(stack, schedule_id, from_time=from_time, to_time=to_time)
        print("The response of MaintenanceWindowsApi->audit_maintenance_windows_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceWindowsApi->audit_maintenance_windows_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **schedule_id** | **str**| The maintenance window schedule ID. | 
 **from_time** | **str**| The earliest time to return results from. Format is expected to be YYYY-MM-DD or in RFC3339. UTC is the default timezone. | [optional] 
 **to_time** | **str**| The latest time to return results from. Format is expected to be YYYY-MM-DD or in RFC3339. UTC is the default timezone. | [optional] 

### Return type

[**List[MaintenanceWindowsAuditResponse]**](MaintenanceWindowsAuditResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully list down status changes for a specific maintenance window schedule |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **describe_maintenance_windows_preferences**
> MaintenanceWindowsPreferencesResponse describe_maintenance_windows_preferences(stack)



Describe maintenance window preferences for a stack.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.maintenance_windows_preferences_response import MaintenanceWindowsPreferencesResponse
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
    api_instance = splunk_acs_sdk.MaintenanceWindowsApi(api_client)
    stack = 'stack_example' # str | the stack name

    try:
        api_response = api_instance.describe_maintenance_windows_preferences(stack)
        print("The response of MaintenanceWindowsApi->describe_maintenance_windows_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceWindowsApi->describe_maintenance_windows_preferences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 

### Return type

[**MaintenanceWindowsPreferencesResponse**](MaintenanceWindowsPreferencesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully described the maintenance window preferences for the stack |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **describe_maintenance_windows_schedule**
> MaintenanceWindowsSchedule describe_maintenance_windows_schedule(stack, schedule_id)



Describe a specific maintenance window schedule

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.maintenance_windows_schedule import MaintenanceWindowsSchedule
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
    api_instance = splunk_acs_sdk.MaintenanceWindowsApi(api_client)
    stack = 'stack_example' # str | the stack name
    schedule_id = 'schedule_id_example' # str | The maintenance window schedule ID.

    try:
        api_response = api_instance.describe_maintenance_windows_schedule(stack, schedule_id)
        print("The response of MaintenanceWindowsApi->describe_maintenance_windows_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceWindowsApi->describe_maintenance_windows_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **schedule_id** | **str**| The maintenance window schedule ID. | 

### Return type

[**MaintenanceWindowsSchedule**](MaintenanceWindowsSchedule.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully described a specific maintenance window schedule |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_maintenance_windows_schedules**
> List[MaintenanceWindowsResponse] list_maintenance_windows_schedules(stack, count=count, next_link=next_link, from_time=from_time, to_time=to_time)



List all scheduled maintenance windows schedules on the stack. The default time range is 30 days. If both fromTime and toTime is empty, the default range is +30 days from current time. If only toTime is given, the default range is -30 days from toTime.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.maintenance_windows_response import MaintenanceWindowsResponse
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
    api_instance = splunk_acs_sdk.MaintenanceWindowsApi(api_client)
    stack = 'stack_example' # str | the stack name
    count = 30 # int | The maximum number of results to return. (optional) (default to 30)
    next_link = 'next_link_example' # str | The key for the next page of the result set. A nextLink with the value null indicates there are no more pages. (optional)
    from_time = 'from_time_example' # str | The earliest time to return results from. Format is expected to be YYYY-MM-DD or in RFC3339. UTC is the default timezone. (optional)
    to_time = 'to_time_example' # str | The latest time to return results from. Format is expected to be YYYY-MM-DD or in RFC3339. UTC is the default timezone. (optional)

    try:
        api_response = api_instance.list_maintenance_windows_schedules(stack, count=count, next_link=next_link, from_time=from_time, to_time=to_time)
        print("The response of MaintenanceWindowsApi->list_maintenance_windows_schedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceWindowsApi->list_maintenance_windows_schedules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **count** | **int**| The maximum number of results to return. | [optional] [default to 30]
 **next_link** | **str**| The key for the next page of the result set. A nextLink with the value null indicates there are no more pages. | [optional] 
 **from_time** | **str**| The earliest time to return results from. Format is expected to be YYYY-MM-DD or in RFC3339. UTC is the default timezone. | [optional] 
 **to_time** | **str**| The latest time to return results from. Format is expected to be YYYY-MM-DD or in RFC3339. UTC is the default timezone. | [optional] 

### Return type

[**List[MaintenanceWindowsResponse]**](MaintenanceWindowsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully listed all scheduled maintenance windows schedules |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_maintenance_windows_preferences**
> update_maintenance_windows_preferences(stack, maintenance_windows_preferences_request=maintenance_windows_preferences_request)



Update maintenance window preferences for a stack.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.maintenance_windows_preferences_request import MaintenanceWindowsPreferencesRequest
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
    api_instance = splunk_acs_sdk.MaintenanceWindowsApi(api_client)
    stack = 'stack_example' # str | the stack name
    maintenance_windows_preferences_request = splunk_acs_sdk.MaintenanceWindowsPreferencesRequest() # MaintenanceWindowsPreferencesRequest |  (optional)

    try:
        api_instance.update_maintenance_windows_preferences(stack, maintenance_windows_preferences_request=maintenance_windows_preferences_request)
    except Exception as e:
        print("Exception when calling MaintenanceWindowsApi->update_maintenance_windows_preferences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **maintenance_windows_preferences_request** | [**MaintenanceWindowsPreferencesRequest**](MaintenanceWindowsPreferencesRequest.md)|  | [optional] 

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
**204** | successfully updated the maintenance window preferences for the stack |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

