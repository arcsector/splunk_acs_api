# DeleteOutboundportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subnets** | **List[str]** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.delete_outboundport_request import DeleteOutboundportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteOutboundportRequest from a JSON string
delete_outboundport_request_instance = DeleteOutboundportRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteOutboundportRequest.to_json())

# convert the object into a dict
delete_outboundport_request_dict = delete_outboundport_request_instance.to_dict()
# create an instance of DeleteOutboundportRequest from a dict
delete_outboundport_request_from_dict = DeleteOutboundportRequest.from_dict(delete_outboundport_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


