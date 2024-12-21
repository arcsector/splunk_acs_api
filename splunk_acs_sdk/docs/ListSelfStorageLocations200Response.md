# ListSelfStorageLocations200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**self_storage_locations** | [**List[SelfStorageLocationInfo]**](SelfStorageLocationInfo.md) |  | 

## Example

```python
from splunk_acs_sdk.models.list_self_storage_locations200_response import ListSelfStorageLocations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListSelfStorageLocations200Response from a JSON string
list_self_storage_locations200_response_instance = ListSelfStorageLocations200Response.from_json(json)
# print the JSON string representation of the object
print(ListSelfStorageLocations200Response.to_json())

# convert the object into a dict
list_self_storage_locations200_response_dict = list_self_storage_locations200_response_instance.to_dict()
# create an instance of ListSelfStorageLocations200Response from a dict
list_self_storage_locations200_response_from_dict = ListSelfStorageLocations200Response.from_dict(list_self_storage_locations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


