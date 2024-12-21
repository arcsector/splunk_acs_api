# EnableObservabilityCapabilitiesResponse

CO2 spec value of the o11y key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**centralized_rbac_enabled** | **bool** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.enable_observability_capabilities_response import EnableObservabilityCapabilitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnableObservabilityCapabilitiesResponse from a JSON string
enable_observability_capabilities_response_instance = EnableObservabilityCapabilitiesResponse.from_json(json)
# print the JSON string representation of the object
print(EnableObservabilityCapabilitiesResponse.to_json())

# convert the object into a dict
enable_observability_capabilities_response_dict = enable_observability_capabilities_response_instance.to_dict()
# create an instance of EnableObservabilityCapabilitiesResponse from a dict
enable_observability_capabilities_response_from_dict = EnableObservabilityCapabilitiesResponse.from_dict(enable_observability_capabilities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


