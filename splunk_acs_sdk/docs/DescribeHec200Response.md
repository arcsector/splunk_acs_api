# DescribeHec200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_event_collector** | [**HecInfo**](HecInfo.md) |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.describe_hec200_response import DescribeHec200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DescribeHec200Response from a JSON string
describe_hec200_response_instance = DescribeHec200Response.from_json(json)
# print the JSON string representation of the object
print(DescribeHec200Response.to_json())

# convert the object into a dict
describe_hec200_response_dict = describe_hec200_response_instance.to_dict()
# create an instance of DescribeHec200Response from a dict
describe_hec200_response_from_dict = DescribeHec200Response.from_dict(describe_hec200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


