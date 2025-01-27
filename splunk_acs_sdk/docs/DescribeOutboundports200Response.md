# DescribeOutboundports200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outboundports** | [**List[OutboundResponse]**](OutboundResponse.md) | the subnets from where the stack feature can access to | [optional] 

## Example

```python
from splunk_acs_sdk.models.describe_outboundports200_response import DescribeOutboundports200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DescribeOutboundports200Response from a JSON string
describe_outboundports200_response_instance = DescribeOutboundports200Response.from_json(json)
# print the JSON string representation of the object
print(DescribeOutboundports200Response.to_json())

# convert the object into a dict
describe_outboundports200_response_dict = describe_outboundports200_response_instance.to_dict()
# create an instance of DescribeOutboundports200Response from a dict
describe_outboundports200_response_from_dict = DescribeOutboundports200Response.from_dict(describe_outboundports200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


