# splunk_acs_sdk.ObservabilityApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enable_rbac_on_o11y**](ObservabilityApi.md#enable_rbac_on_o11y) | **PUT** /{stack}/adminconfig/v2/observability/enable-centralized-rbac | 
[**get_observability_pairing_status**](ObservabilityApi.md#get_observability_pairing_status) | **GET** /{stack}/adminconfig/v2/observability/sso-pairing/{pairingId} | 
[**post_observability_capabilities_on_splunk**](ObservabilityApi.md#post_observability_capabilities_on_splunk) | **POST** /{stack}/adminconfig/v2/observability/capabilities | 
[**post_observability_pairing**](ObservabilityApi.md#post_observability_pairing) | **POST** /{stack}/adminconfig/v2/observability/sso-pairing | 


# **enable_rbac_on_o11y**
> enable_rbac_on_o11y(o11y_access_token, stack)



set the paired Splunk Cloud stack as the RBAC source for Splunk Observability Cloud organization

### Example


```python
import splunk_acs_sdk
from splunk_acs_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = splunk_acs_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with splunk_acs_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = splunk_acs_sdk.ObservabilityApi(api_client)
    o11y_access_token = 'o11y_access_token_example' # str | Observability Admin Access Token
    stack = 'stack_example' # str | The stack name.

    try:
        api_instance.enable_rbac_on_o11y(o11y_access_token, stack)
    except Exception as e:
        print("Exception when calling ObservabilityApi->enable_rbac_on_o11y: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o11y_access_token** | **str**| Observability Admin Access Token | 
 **stack** | **str**| The stack name. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | set the paired Splunk Cloud stack as the RBAC source for Splunk Observability Cloud organization |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_observability_pairing_status**
> GetEcSsoPairingStatusResponse get_observability_pairing_status(o11y_access_token, stack, pairing_id)



Gets a status for pairing your Splunk Cloud stack with the Observability cloud Org.

### Example


```python
import splunk_acs_sdk
from splunk_acs_sdk.models.get_ec_sso_pairing_status_response import GetEcSsoPairingStatusResponse
from splunk_acs_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = splunk_acs_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with splunk_acs_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = splunk_acs_sdk.ObservabilityApi(api_client)
    o11y_access_token = 'o11y_access_token_example' # str | Observability Admin Access Token
    stack = 'stack_example' # str | The stack name.
    pairing_id = 'pairing_id_example' # str | A pairing ID.

    try:
        api_response = api_instance.get_observability_pairing_status(o11y_access_token, stack, pairing_id)
        print("The response of ObservabilityApi->get_observability_pairing_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservabilityApi->get_observability_pairing_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o11y_access_token** | **str**| Observability Admin Access Token | 
 **stack** | **str**| The stack name. | 
 **pairing_id** | **str**| A pairing ID. | 

### Return type

[**GetEcSsoPairingStatusResponse**](GetEcSsoPairingStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully found pairing status for the provided pairing ID |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_observability_capabilities_on_splunk**
> EnableObservabilityCapabilitiesResponse post_observability_capabilities_on_splunk(stack)



enables the o11y-splunk centralized RBAC integration including the addition of o11y roles and capabilities on the stack.

### Example


```python
import splunk_acs_sdk
from splunk_acs_sdk.models.enable_observability_capabilities_response import EnableObservabilityCapabilitiesResponse
from splunk_acs_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = splunk_acs_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with splunk_acs_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = splunk_acs_sdk.ObservabilityApi(api_client)
    stack = 'stack_example' # str | The stack name.

    try:
        api_response = api_instance.post_observability_capabilities_on_splunk(stack)
        print("The response of ObservabilityApi->post_observability_capabilities_on_splunk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservabilityApi->post_observability_capabilities_on_splunk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | **str**| The stack name. | 

### Return type

[**EnableObservabilityCapabilitiesResponse**](EnableObservabilityCapabilitiesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successfully submitted request to update stack&#39;s spec |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_observability_pairing**
> CreateEcSsoPairingResponse post_observability_pairing(o11y_access_token, stack)



Pair your Splunk Cloud stack to the Observability cloud org to use the stack as Identity Provider

### Example


```python
import splunk_acs_sdk
from splunk_acs_sdk.models.create_ec_sso_pairing_response import CreateEcSsoPairingResponse
from splunk_acs_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = splunk_acs_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with splunk_acs_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = splunk_acs_sdk.ObservabilityApi(api_client)
    o11y_access_token = 'o11y_access_token_example' # str | Observability Admin Access Token
    stack = 'stack_example' # str | The stack name.

    try:
        api_response = api_instance.post_observability_pairing(o11y_access_token, stack)
        print("The response of ObservabilityApi->post_observability_pairing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservabilityApi->post_observability_pairing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o11y_access_token** | **str**| Observability Admin Access Token | 
 **stack** | **str**| The stack name. | 

### Return type

[**CreateEcSsoPairingResponse**](CreateEcSsoPairingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully started pairing Splunk Cloud stack to the Observability Org |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

