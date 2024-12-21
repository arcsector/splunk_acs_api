# AddSubnetsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subnets** | **List[str]** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.add_subnets_request import AddSubnetsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddSubnetsRequest from a JSON string
add_subnets_request_instance = AddSubnetsRequest.from_json(json)
# print the JSON string representation of the object
print(AddSubnetsRequest.to_json())

# convert the object into a dict
add_subnets_request_dict = add_subnets_request_instance.to_dict()
# create an instance of AddSubnetsRequest from a dict
add_subnets_request_from_dict = AddSubnetsRequest.from_dict(add_subnets_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


