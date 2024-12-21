# OutboundResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_ranges** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**port** | **int** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.outbound_response import OutboundResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OutboundResponse from a JSON string
outbound_response_instance = OutboundResponse.from_json(json)
# print the JSON string representation of the object
print(OutboundResponse.to_json())

# convert the object into a dict
outbound_response_dict = outbound_response_instance.to_dict()
# create an instance of OutboundResponse from a dict
outbound_response_from_dict = OutboundResponse.from_dict(outbound_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


