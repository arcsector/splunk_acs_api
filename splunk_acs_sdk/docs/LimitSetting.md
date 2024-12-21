# LimitSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_value** | **float** |  | [optional] 
**max_value** | **float** |  | [optional] 
**min_value** | **float** |  | [optional] 
**setting** | **str** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.limit_setting import LimitSetting

# TODO update the JSON string below
json = "{}"
# create an instance of LimitSetting from a JSON string
limit_setting_instance = LimitSetting.from_json(json)
# print the JSON string representation of the object
print(LimitSetting.to_json())

# convert the object into a dict
limit_setting_dict = limit_setting_instance.to_dict()
# create an instance of LimitSetting from a dict
limit_setting_from_dict = LimitSetting.from_dict(limit_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


