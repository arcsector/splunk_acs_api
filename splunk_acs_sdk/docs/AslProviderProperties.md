# AslProviderProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_database** | **str** |  | 
**remote_database** | **str** |  | 
**remote_tables** | **List[str]** |  | 
**resource_share_arn** | **str** |  | 
**resource_share_name** | **str** |  | 

## Example

```python
from splunk_acs_sdk.models.asl_provider_properties import AslProviderProperties

# TODO update the JSON string below
json = "{}"
# create an instance of AslProviderProperties from a JSON string
asl_provider_properties_instance = AslProviderProperties.from_json(json)
# print the JSON string representation of the object
print(AslProviderProperties.to_json())

# convert the object into a dict
asl_provider_properties_dict = asl_provider_properties_instance.to_dict()
# create an instance of AslProviderProperties from a dict
asl_provider_properties_from_dict = AslProviderProperties.from_dict(asl_provider_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


