# LimitConfigurationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | **object** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.limit_configuration_info import LimitConfigurationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LimitConfigurationInfo from a JSON string
limit_configuration_info_instance = LimitConfigurationInfo.from_json(json)
# print the JSON string representation of the object
print(LimitConfigurationInfo.to_json())

# convert the object into a dict
limit_configuration_info_dict = limit_configuration_info_instance.to_dict()
# create an instance of LimitConfigurationInfo from a dict
limit_configuration_info_from_dict = LimitConfigurationInfo.from_dict(limit_configuration_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


