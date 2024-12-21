# LimitResetSettingsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | **List[str]** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.limit_reset_settings_list import LimitResetSettingsList

# TODO update the JSON string below
json = "{}"
# create an instance of LimitResetSettingsList from a JSON string
limit_reset_settings_list_instance = LimitResetSettingsList.from_json(json)
# print the JSON string representation of the object
print(LimitResetSettingsList.to_json())

# convert the object into a dict
limit_reset_settings_list_dict = limit_reset_settings_list_instance.to_dict()
# create an instance of LimitResetSettingsList from a dict
limit_reset_settings_list_from_dict = LimitResetSettingsList.from_dict(limit_reset_settings_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


