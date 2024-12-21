# UpdateManagedGlueResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managed_glue_resources** | [**List[ManagedGlueResources]**](ManagedGlueResources.md) |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.update_managed_glue_resources import UpdateManagedGlueResources

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateManagedGlueResources from a JSON string
update_managed_glue_resources_instance = UpdateManagedGlueResources.from_json(json)
# print the JSON string representation of the object
print(UpdateManagedGlueResources.to_json())

# convert the object into a dict
update_managed_glue_resources_dict = update_managed_glue_resources_instance.to_dict()
# create an instance of UpdateManagedGlueResources from a dict
update_managed_glue_resources_from_dict = UpdateManagedGlueResources.from_dict(update_managed_glue_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


