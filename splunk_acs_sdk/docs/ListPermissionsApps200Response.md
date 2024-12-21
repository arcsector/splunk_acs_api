# ListPermissionsApps200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tokeninfo** | [**AppPermsList**](AppPermsList.md) |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.list_permissions_apps200_response import ListPermissionsApps200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListPermissionsApps200Response from a JSON string
list_permissions_apps200_response_instance = ListPermissionsApps200Response.from_json(json)
# print the JSON string representation of the object
print(ListPermissionsApps200Response.to_json())

# convert the object into a dict
list_permissions_apps200_response_dict = list_permissions_apps200_response_instance.to_dict()
# create an instance of ListPermissionsApps200Response from a dict
list_permissions_apps200_response_from_dict = ListPermissionsApps200Response.from_dict(list_permissions_apps200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


