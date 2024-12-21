# DescribePrivateConnectivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoints** | [**List[PrivateConnectivityEndpoints]**](PrivateConnectivityEndpoints.md) |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.describe_private_connectivity import DescribePrivateConnectivity

# TODO update the JSON string below
json = "{}"
# create an instance of DescribePrivateConnectivity from a JSON string
describe_private_connectivity_instance = DescribePrivateConnectivity.from_json(json)
# print the JSON string representation of the object
print(DescribePrivateConnectivity.to_json())

# convert the object into a dict
describe_private_connectivity_dict = describe_private_connectivity_instance.to_dict()
# create an instance of DescribePrivateConnectivity from a dict
describe_private_connectivity_from_dict = DescribePrivateConnectivity.from_dict(describe_private_connectivity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


