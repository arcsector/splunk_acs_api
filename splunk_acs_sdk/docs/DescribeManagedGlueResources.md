# DescribeManagedGlueResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managed_glue_resources** | [**List[ManagedGlueResources]**](ManagedGlueResources.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.describe_managed_glue_resources import DescribeManagedGlueResources

# TODO update the JSON string below
json = "{}"
# create an instance of DescribeManagedGlueResources from a JSON string
describe_managed_glue_resources_instance = DescribeManagedGlueResources.from_json(json)
# print the JSON string representation of the object
print(DescribeManagedGlueResources.to_json())

# convert the object into a dict
describe_managed_glue_resources_dict = describe_managed_glue_resources_instance.to_dict()
# create an instance of DescribeManagedGlueResources from a dict
describe_managed_glue_resources_from_dict = DescribeManagedGlueResources.from_dict(describe_managed_glue_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


