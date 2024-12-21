# SelfStorageLocationPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**policy** | **object** |  | 

## Example

```python
from splunk_acs_sdk.models.self_storage_location_policy import SelfStorageLocationPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of SelfStorageLocationPolicy from a JSON string
self_storage_location_policy_instance = SelfStorageLocationPolicy.from_json(json)
# print the JSON string representation of the object
print(SelfStorageLocationPolicy.to_json())

# convert the object into a dict
self_storage_location_policy_dict = self_storage_location_policy_instance.to_dict()
# create an instance of SelfStorageLocationPolicy from a dict
self_storage_location_policy_from_dict = SelfStorageLocationPolicy.from_dict(self_storage_location_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


