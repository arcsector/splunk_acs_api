# DescribeEligibilityPrivateConnectivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligible** | **bool** |  | [optional] 
**reason** | **str** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.describe_eligibility_private_connectivity import DescribeEligibilityPrivateConnectivity

# TODO update the JSON string below
json = "{}"
# create an instance of DescribeEligibilityPrivateConnectivity from a JSON string
describe_eligibility_private_connectivity_instance = DescribeEligibilityPrivateConnectivity.from_json(json)
# print the JSON string representation of the object
print(DescribeEligibilityPrivateConnectivity.to_json())

# convert the object into a dict
describe_eligibility_private_connectivity_dict = describe_eligibility_private_connectivity_instance.to_dict()
# create an instance of DescribeEligibilityPrivateConnectivity from a dict
describe_eligibility_private_connectivity_from_dict = DescribeEligibilityPrivateConnectivity.from_dict(describe_eligibility_private_connectivity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


