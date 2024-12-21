# LimitConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | **List[str]** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.limit_configuration_response import LimitConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LimitConfigurationResponse from a JSON string
limit_configuration_response_instance = LimitConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(LimitConfigurationResponse.to_json())

# convert the object into a dict
limit_configuration_response_dict = limit_configuration_response_instance.to_dict()
# create an instance of LimitConfigurationResponse from a dict
limit_configuration_response_from_dict = LimitConfigurationResponse.from_dict(limit_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


