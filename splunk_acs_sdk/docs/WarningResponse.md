# WarningResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warnings** | **List[str]** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.warning_response import WarningResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WarningResponse from a JSON string
warning_response_instance = WarningResponse.from_json(json)
# print the JSON string representation of the object
print(WarningResponse.to_json())

# convert the object into a dict
warning_response_dict = warning_response_instance.to_dict()
# create an instance of WarningResponse from a dict
warning_response_from_dict = WarningResponse.from_dict(warning_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


