# splunk_acs_sdk.PlatformOrchestratorApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**describe_workflow**](PlatformOrchestratorApi.md#describe_workflow) | **GET** /{stack}/adminconfig/v2/workflows/{workflowName} | 


# **describe_workflow**
> List[DescribeWorkflowResponseObject] describe_workflow(stack, workflow_name)



Get a workflow status given a workflow name

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import splunk_acs_sdk
from splunk_acs_sdk.models.describe_workflow_response_object import DescribeWorkflowResponseObject
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
    api_instance = splunk_acs_sdk.PlatformOrchestratorApi(api_client)
    stack = 'stack_example' # str | the stack name
    workflow_name = 'workflow_name_example' # str | Name/ID of the workflow

    try:
        api_response = api_instance.describe_workflow(stack, workflow_name)
        print("The response of PlatformOrchestratorApi->describe_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformOrchestratorApi->describe_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| the stack name | 
 **workflow_name** | **str**| Name/ID of the workflow | 

### Return type

[**List[DescribeWorkflowResponseObject]**](DescribeWorkflowResponseObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully list all scheduled workflow status |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

