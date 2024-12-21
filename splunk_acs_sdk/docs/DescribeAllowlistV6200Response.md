# DescribeAllowlistV6200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subnets** | **List[str]** | the ipv6 subnets from where the stack feature is accessible from | [optional] 

## Example

```python
from splunk_acs_sdk.models.describe_allowlist_v6200_response import DescribeAllowlistV6200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DescribeAllowlistV6200Response from a JSON string
describe_allowlist_v6200_response_instance = DescribeAllowlistV6200Response.from_json(json)
# print the JSON string representation of the object
print(DescribeAllowlistV6200Response.to_json())

# convert the object into a dict
describe_allowlist_v6200_response_dict = describe_allowlist_v6200_response_instance.to_dict()
# create an instance of DescribeAllowlistV6200Response from a dict
describe_allowlist_v6200_response_from_dict = DescribeAllowlistV6200Response.from_dict(describe_allowlist_v6200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


