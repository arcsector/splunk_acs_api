# AddOutboundportsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outbound_ports** | [**List[AddOutboundportsRequestOutboundPortsInner]**](AddOutboundportsRequestOutboundPortsInner.md) |  | [optional] 
**reason** | **str** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.add_outboundports_request import AddOutboundportsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddOutboundportsRequest from a JSON string
add_outboundports_request_instance = AddOutboundportsRequest.from_json(json)
# print the JSON string representation of the object
print(AddOutboundportsRequest.to_json())

# convert the object into a dict
add_outboundports_request_dict = add_outboundports_request_instance.to_dict()
# create an instance of AddOutboundportsRequest from a dict
add_outboundports_request_from_dict = AddOutboundportsRequest.from_dict(add_outboundports_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


