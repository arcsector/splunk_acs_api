# ManagedGlueResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_provider** | **str** |  | 
**database** | **str** |  | 
**extra** | [**Extra**](Extra.md) |  | [optional] 
**field_delimiter** | **str** |  | [optional] 
**file_format** | **str** |  | 
**location_prefix** | **str** |  | 
**partition_projection** | [**PartitionProjection**](PartitionProjection.md) |  | 
**source_type** | **str** |  | 
**table** | **str** |  | 

## Example

```python
from splunk_acs_sdk.models.managed_glue_resources import ManagedGlueResources

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedGlueResources from a JSON string
managed_glue_resources_instance = ManagedGlueResources.from_json(json)
# print the JSON string representation of the object
print(ManagedGlueResources.to_json())

# convert the object into a dict
managed_glue_resources_dict = managed_glue_resources_instance.to_dict()
# create an instance of ManagedGlueResources from a dict
managed_glue_resources_from_dict = ManagedGlueResources.from_dict(managed_glue_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


