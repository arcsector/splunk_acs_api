# PrivateConnectivityEndpoints


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_account_ids** | **List[str]** |  | [optional] 
**endpoint** | **str** |  | [optional] 
**feature** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**private_search_dns_records** | **List[str]** |  | [optional] 
**reason** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.private_connectivity_endpoints import PrivateConnectivityEndpoints

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateConnectivityEndpoints from a JSON string
private_connectivity_endpoints_instance = PrivateConnectivityEndpoints.from_json(json)
# print the JSON string representation of the object
print(PrivateConnectivityEndpoints.to_json())

# convert the object into a dict
private_connectivity_endpoints_dict = private_connectivity_endpoints_instance.to_dict()
# create an instance of PrivateConnectivityEndpoints from a dict
private_connectivity_endpoints_from_dict = PrivateConnectivityEndpoints.from_dict(private_connectivity_endpoints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


