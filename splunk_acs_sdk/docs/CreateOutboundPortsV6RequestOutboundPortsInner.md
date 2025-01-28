# CreateOutboundPortsV6RequestOutboundPortsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port** | **int** |  | [optional] 
**subnets** | **List[str]** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.create_outbound_ports_v6_request_outbound_ports_inner import CreateOutboundPortsV6RequestOutboundPortsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOutboundPortsV6RequestOutboundPortsInner from a JSON string
create_outbound_ports_v6_request_outbound_ports_inner_instance = CreateOutboundPortsV6RequestOutboundPortsInner.from_json(json)
# print the JSON string representation of the object
print(CreateOutboundPortsV6RequestOutboundPortsInner.to_json())

# convert the object into a dict
create_outbound_ports_v6_request_outbound_ports_inner_dict = create_outbound_ports_v6_request_outbound_ports_inner_instance.to_dict()
# create an instance of CreateOutboundPortsV6RequestOutboundPortsInner from a dict
create_outbound_ports_v6_request_outbound_ports_inner_from_dict = CreateOutboundPortsV6RequestOutboundPortsInner.from_dict(create_outbound_ports_v6_request_outbound_ports_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


