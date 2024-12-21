# AppPerms

App Permissions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**perms** | [**AppPermsProperties**](AppPermsProperties.md) |  | 

## Example

```python
from splunk_acs_sdk.models.app_perms import AppPerms

# TODO update the JSON string below
json = "{}"
# create an instance of AppPerms from a JSON string
app_perms_instance = AppPerms.from_json(json)
# print the JSON string representation of the object
print(AppPerms.to_json())

# convert the object into a dict
app_perms_dict = app_perms_instance.to_dict()
# create an instance of AppPerms from a dict
app_perms_from_dict = AppPerms.from_dict(app_perms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


