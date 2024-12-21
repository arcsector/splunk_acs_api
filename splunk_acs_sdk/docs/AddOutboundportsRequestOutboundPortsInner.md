# AddOutboundportsRequestOutboundPortsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port** | **int** |  | [optional] 
**subnets** | **List[str]** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.add_outboundports_request_outbound_ports_inner import AddOutboundportsRequestOutboundPortsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AddOutboundportsRequestOutboundPortsInner from a JSON string
add_outboundports_request_outbound_ports_inner_instance = AddOutboundportsRequestOutboundPortsInner.from_json(json)
# print the JSON string representation of the object
print(AddOutboundportsRequestOutboundPortsInner.to_json())

# convert the object into a dict
add_outboundports_request_outbound_ports_inner_dict = add_outboundports_request_outbound_ports_inner_instance.to_dict()
# create an instance of AddOutboundportsRequestOutboundPortsInner from a dict
add_outboundports_request_outbound_ports_inner_from_dict = AddOutboundportsRequestOutboundPortsInner.from_dict(add_outboundports_request_outbound_ports_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


