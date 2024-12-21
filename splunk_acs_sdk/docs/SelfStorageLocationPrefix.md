# SelfStorageLocationPrefix


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**prefix** | **str** |  | 

## Example

```python
from splunk_acs_sdk.models.self_storage_location_prefix import SelfStorageLocationPrefix

# TODO update the JSON string below
json = "{}"
# create an instance of SelfStorageLocationPrefix from a JSON string
self_storage_location_prefix_instance = SelfStorageLocationPrefix.from_json(json)
# print the JSON string representation of the object
print(SelfStorageLocationPrefix.to_json())

# convert the object into a dict
self_storage_location_prefix_dict = self_storage_location_prefix_instance.to_dict()
# create an instance of SelfStorageLocationPrefix from a dict
self_storage_location_prefix_from_dict = SelfStorageLocationPrefix.from_dict(self_storage_location_prefix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


