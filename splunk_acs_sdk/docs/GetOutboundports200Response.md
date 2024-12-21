# GetOutboundports200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outboundports** | [**List[OutboundResponse]**](OutboundResponse.md) | the subnets from where the stack feature can access to | [optional] 

## Example

```python
from splunk_acs_sdk.models.get_outboundports200_response import GetOutboundports200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetOutboundports200Response from a JSON string
get_outboundports200_response_instance = GetOutboundports200Response.from_json(json)
# print the JSON string representation of the object
print(GetOutboundports200Response.to_json())

# convert the object into a dict
get_outboundports200_response_dict = get_outboundports200_response_instance.to_dict()
# create an instance of GetOutboundports200Response from a dict
get_outboundports200_response_from_dict = GetOutboundports200Response.from_dict(get_outboundports200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


