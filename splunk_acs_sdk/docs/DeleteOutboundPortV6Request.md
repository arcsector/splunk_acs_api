# DeleteOutboundPortV6Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subnets** | **List[str]** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.delete_outbound_port_v6_request import DeleteOutboundPortV6Request

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteOutboundPortV6Request from a JSON string
delete_outbound_port_v6_request_instance = DeleteOutboundPortV6Request.from_json(json)
# print the JSON string representation of the object
print(DeleteOutboundPortV6Request.to_json())

# convert the object into a dict
delete_outbound_port_v6_request_dict = delete_outbound_port_v6_request_instance.to_dict()
# create an instance of DeleteOutboundPortV6Request from a dict
delete_outbound_port_v6_request_from_dict = DeleteOutboundPortV6Request.from_dict(delete_outbound_port_v6_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


