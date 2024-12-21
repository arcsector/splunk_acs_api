# TokenBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience** | **str** |  | 
**expires_on** | **str** |  | [optional] [default to '+30d']
**type** | **str** |  | [optional] [default to 'static']
**user** | **str** |  | 

## Example

```python
from splunk_acs_sdk.models.token_body import TokenBody

# TODO update the JSON string below
json = "{}"
# create an instance of TokenBody from a JSON string
token_body_instance = TokenBody.from_json(json)
# print the JSON string representation of the object
print(TokenBody.to_json())

# convert the object into a dict
token_body_dict = token_body_instance.to_dict()
# create an instance of TokenBody from a dict
token_body_from_dict = TokenBody.from_dict(token_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


