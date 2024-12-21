# DescribeStack200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**StackStatus**](StackStatus.md) |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.describe_stack200_response import DescribeStack200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DescribeStack200Response from a JSON string
describe_stack200_response_instance = DescribeStack200Response.from_json(json)
# print the JSON string representation of the object
print(DescribeStack200Response.to_json())

# convert the object into a dict
describe_stack200_response_dict = describe_stack200_response_instance.to_dict()
# create an instance of DescribeStack200Response from a dict
describe_stack200_response_from_dict = DescribeStack200Response.from_dict(describe_stack200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


