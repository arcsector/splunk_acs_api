# SelfStorageLocationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** |  | 
**bucket_path** | **str** |  | 
**description** | **str** |  | 
**folder** | **str** |  | 
**title** | **str** |  | 
**uri** | **str** |  | 

## Example

```python
from splunk_acs_sdk.models.self_storage_location_info import SelfStorageLocationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SelfStorageLocationInfo from a JSON string
self_storage_location_info_instance = SelfStorageLocationInfo.from_json(json)
# print the JSON string representation of the object
print(SelfStorageLocationInfo.to_json())

# convert the object into a dict
self_storage_location_info_dict = self_storage_location_info_instance.to_dict()
# create an instance of SelfStorageLocationInfo from a dict
self_storage_location_info_from_dict = SelfStorageLocationInfo.from_dict(self_storage_location_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


