# HecSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_indexes** | **List[str]** |  | [optional] 
**default_host** | **str** |  | [optional] 
**default_index** | **str** |  | [optional] 
**default_source** | **str** |  | [optional] 
**default_sourcetype** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**name** | **str** |  | 
**token** | **str** |  | [optional] 
**use_ack** | **bool** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.hec_spec import HecSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HecSpec from a JSON string
hec_spec_instance = HecSpec.from_json(json)
# print the JSON string representation of the object
print(HecSpec.to_json())

# convert the object into a dict
hec_spec_dict = hec_spec_instance.to_dict()
# create an instance of HecSpec from a dict
hec_spec_from_dict = HecSpec.from_dict(hec_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


