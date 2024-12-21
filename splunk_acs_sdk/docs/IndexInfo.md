# IndexInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datatype** | **str** |  | [optional] [default to 'event']
**max_data_size_mb** | **int** |  | [optional] [default to 0]
**name** | **str** |  | 
**searchable_days** | **int** |  | [optional] [default to 90]
**self_storage_bucket_path** | **str** |  | [optional] 
**splunk_archival_retention_days** | **int** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.index_info import IndexInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IndexInfo from a JSON string
index_info_instance = IndexInfo.from_json(json)
# print the JSON string representation of the object
print(IndexInfo.to_json())

# convert the object into a dict
index_info_dict = index_info_instance.to_dict()
# create an instance of IndexInfo from a dict
index_info_from_dict = IndexInfo.from_dict(index_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


