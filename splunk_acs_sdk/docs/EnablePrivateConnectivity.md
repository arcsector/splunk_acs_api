# EnablePrivateConnectivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_account_ids** | **List[str]** |  | [optional] 
**feature** | **List[str]** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.enable_private_connectivity import EnablePrivateConnectivity

# TODO update the JSON string below
json = "{}"
# create an instance of EnablePrivateConnectivity from a JSON string
enable_private_connectivity_instance = EnablePrivateConnectivity.from_json(json)
# print the JSON string representation of the object
print(EnablePrivateConnectivity.to_json())

# convert the object into a dict
enable_private_connectivity_dict = enable_private_connectivity_instance.to_dict()
# create an instance of EnablePrivateConnectivity from a dict
enable_private_connectivity_from_dict = EnablePrivateConnectivity.from_dict(enable_private_connectivity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


