# AppPermsProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read** | **List[str]** |  | [optional] 
**write** | **List[str]** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.app_perms_properties import AppPermsProperties

# TODO update the JSON string below
json = "{}"
# create an instance of AppPermsProperties from a JSON string
app_perms_properties_instance = AppPermsProperties.from_json(json)
# print the JSON string representation of the object
print(AppPermsProperties.to_json())

# convert the object into a dict
app_perms_properties_dict = app_perms_properties_instance.to_dict()
# create an instance of AppPermsProperties from a dict
app_perms_properties_from_dict = AppPermsProperties.from_dict(app_perms_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


