# PartitionProjection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id_key_name** | **str** |  | [optional] 
**account_ids** | **List[str]** |  | 
**region_key_name** | **str** |  | [optional] 
**regions** | **List[str]** |  | 
**time_key_name** | **str** |  | [optional] 
**time_range** | **str** |  | [optional] 
**time_unit** | **str** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.partition_projection import PartitionProjection

# TODO update the JSON string below
json = "{}"
# create an instance of PartitionProjection from a JSON string
partition_projection_instance = PartitionProjection.from_json(json)
# print the JSON string representation of the object
print(PartitionProjection.to_json())

# convert the object into a dict
partition_projection_dict = partition_projection_instance.to_dict()
# create an instance of PartitionProjection from a dict
partition_projection_from_dict = PartitionProjection.from_dict(partition_projection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


