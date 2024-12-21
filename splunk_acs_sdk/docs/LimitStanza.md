# LimitStanza


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**List[LimitSetting]**](LimitSetting.md) |  | [optional] 
**stanza** | **str** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.limit_stanza import LimitStanza

# TODO update the JSON string below
json = "{}"
# create an instance of LimitStanza from a JSON string
limit_stanza_instance = LimitStanza.from_json(json)
# print the JSON string representation of the object
print(LimitStanza.to_json())

# convert the object into a dict
limit_stanza_dict = limit_stanza_instance.to_dict()
# create an instance of LimitStanza from a dict
limit_stanza_from_dict = LimitStanza.from_dict(limit_stanza_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


