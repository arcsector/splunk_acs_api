# SelfStorageLocationBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** |  | 
**description** | **str** |  | [optional] 
**folder** | **str** |  | [optional] 
**title** | **str** |  | 

## Example

```python
from splunk_acs_sdk.models.self_storage_location_body import SelfStorageLocationBody

# TODO update the JSON string below
json = "{}"
# create an instance of SelfStorageLocationBody from a JSON string
self_storage_location_body_instance = SelfStorageLocationBody.from_json(json)
# print the JSON string representation of the object
print(SelfStorageLocationBody.to_json())

# convert the object into a dict
self_storage_location_body_dict = self_storage_location_body_instance.to_dict()
# create an instance of SelfStorageLocationBody from a dict
self_storage_location_body_from_dict = SelfStorageLocationBody.from_dict(self_storage_location_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


