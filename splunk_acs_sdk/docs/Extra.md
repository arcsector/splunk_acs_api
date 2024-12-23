# Extra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_indexes** | **List[int]** |  | [optional] 
**org_id** | **str** |  | [optional] 
**partition_style** | **str** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.extra import Extra

# TODO update the JSON string below
json = "{}"
# create an instance of Extra from a JSON string
extra_instance = Extra.from_json(json)
# print the JSON string representation of the object
print(Extra.to_json())

# convert the object into a dict
extra_dict = extra_instance.to_dict()
# create an instance of Extra from a dict
extra_from_dict = Extra.from_dict(extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


