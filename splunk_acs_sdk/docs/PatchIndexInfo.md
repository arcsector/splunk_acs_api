# PatchIndexInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_data_size_mb** | **int** |  | [optional] 
**searchable_days** | **int** |  | [optional] 
**self_storage_bucket_path** | **str** |  | [optional] 
**splunk_archival_retention_days** | **int** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.patch_index_info import PatchIndexInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PatchIndexInfo from a JSON string
patch_index_info_instance = PatchIndexInfo.from_json(json)
# print the JSON string representation of the object
print(PatchIndexInfo.to_json())

# convert the object into a dict
patch_index_info_dict = patch_index_info_instance.to_dict()
# create an instance of PatchIndexInfo from a dict
patch_index_info_from_dict = PatchIndexInfo.from_dict(patch_index_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


