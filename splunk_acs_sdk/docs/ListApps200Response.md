# ListApps200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apps** | [**List[App]**](App.md) |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.list_apps200_response import ListApps200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListApps200Response from a JSON string
list_apps200_response_instance = ListApps200Response.from_json(json)
# print the JSON string representation of the object
print(ListApps200Response.to_json())

# convert the object into a dict
list_apps200_response_dict = list_apps200_response_instance.to_dict()
# create an instance of ListApps200Response from a dict
list_apps200_response_from_dict = ListApps200Response.from_dict(list_apps200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


