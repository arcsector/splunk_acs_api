# HecInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**HecSpec**](HecSpec.md) |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.hec_info import HecInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HecInfo from a JSON string
hec_info_instance = HecInfo.from_json(json)
# print the JSON string representation of the object
print(HecInfo.to_json())

# convert the object into a dict
hec_info_dict = hec_info_instance.to_dict()
# create an instance of HecInfo from a dict
hec_info_from_dict = HecInfo.from_dict(hec_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


