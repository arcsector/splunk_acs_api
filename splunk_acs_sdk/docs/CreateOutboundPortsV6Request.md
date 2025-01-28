# CreateOutboundPortsV6Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outbound_ports** | [**List[CreateOutboundPortsV6RequestOutboundPortsInner]**](CreateOutboundPortsV6RequestOutboundPortsInner.md) |  | [optional] 
**reason** | **str** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.create_outbound_ports_v6_request import CreateOutboundPortsV6Request

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOutboundPortsV6Request from a JSON string
create_outbound_ports_v6_request_instance = CreateOutboundPortsV6Request.from_json(json)
# print the JSON string representation of the object
print(CreateOutboundPortsV6Request.to_json())

# convert the object into a dict
create_outbound_ports_v6_request_dict = create_outbound_ports_v6_request_instance.to_dict()
# create an instance of CreateOutboundPortsV6Request from a dict
create_outbound_ports_v6_request_from_dict = CreateOutboundPortsV6Request.from_dict(create_outbound_ports_v6_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


