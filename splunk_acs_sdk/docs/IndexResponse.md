# IndexResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datatype** | **str** |  | [default to 'event']
**max_data_size_mb** | **int** |  | [default to 0]
**name** | **str** |  | 
**searchable_days** | **int** |  | [default to 90]
**self_storage_bucket_path** | **str** |  | [optional] 
**splunk_archival_retention_days** | **int** |  | [optional] 
**total_event_count** | **str** |  | [optional] 
**total_raw_size_mb** | **str** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.index_response import IndexResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IndexResponse from a JSON string
index_response_instance = IndexResponse.from_json(json)
# print the JSON string representation of the object
print(IndexResponse.to_json())

# convert the object into a dict
index_response_dict = index_response_instance.to_dict()
# create an instance of IndexResponse from a dict
index_response_from_dict = IndexResponse.from_dict(index_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


