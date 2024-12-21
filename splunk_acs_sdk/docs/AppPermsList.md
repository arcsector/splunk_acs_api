# AppPermsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apps** | [**List[AppPerms]**](AppPerms.md) |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.app_perms_list import AppPermsList

# TODO update the JSON string below
json = "{}"
# create an instance of AppPermsList from a JSON string
app_perms_list_instance = AppPermsList.from_json(json)
# print the JSON string representation of the object
print(AppPermsList.to_json())

# convert the object into a dict
app_perms_list_dict = app_perms_list_instance.to_dict()
# create an instance of AppPermsList from a dict
app_perms_list_from_dict = AppPermsList.from_dict(app_perms_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


