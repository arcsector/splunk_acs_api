# UpdatePrivateConnectivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature** | **List[str]** |  | [optional] 
**patched_customer_account_ids** | **List[str]** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.update_private_connectivity import UpdatePrivateConnectivity

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePrivateConnectivity from a JSON string
update_private_connectivity_instance = UpdatePrivateConnectivity.from_json(json)
# print the JSON string representation of the object
print(UpdatePrivateConnectivity.to_json())

# convert the object into a dict
update_private_connectivity_dict = update_private_connectivity_instance.to_dict()
# create an instance of UpdatePrivateConnectivity from a dict
update_private_connectivity_from_dict = UpdatePrivateConnectivity.from_dict(update_private_connectivity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


