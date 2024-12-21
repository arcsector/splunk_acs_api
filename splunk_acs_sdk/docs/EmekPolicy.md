# EmekPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**policy** | **object** |  | 
**region** | **str** |  | 

## Example

```python
from splunk_acs_sdk.models.emek_policy import EmekPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of EmekPolicy from a JSON string
emek_policy_instance = EmekPolicy.from_json(json)
# print the JSON string representation of the object
print(EmekPolicy.to_json())

# convert the object into a dict
emek_policy_dict = emek_policy_instance.to_dict()
# create an instance of EmekPolicy from a dict
emek_policy_from_dict = EmekPolicy.from_dict(emek_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


