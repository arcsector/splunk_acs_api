# CapabilitiesInfo

capabilities list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grantable_capabilities** | **List[str]** |  | [optional] 
**system_capabilities** | **List[str]** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.capabilities_info import CapabilitiesInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CapabilitiesInfo from a JSON string
capabilities_info_instance = CapabilitiesInfo.from_json(json)
# print the JSON string representation of the object
print(CapabilitiesInfo.to_json())

# convert the object into a dict
capabilities_info_dict = capabilities_info_instance.to_dict()
# create an instance of CapabilitiesInfo from a dict
capabilities_info_from_dict = CapabilitiesInfo.from_dict(capabilities_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


