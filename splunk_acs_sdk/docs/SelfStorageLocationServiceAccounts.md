# SelfStorageLocationServiceAccounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_master** | **str** |  | 
**indexer** | **str** |  | 

## Example

```python
from splunk_acs_sdk.models.self_storage_location_service_accounts import SelfStorageLocationServiceAccounts

# TODO update the JSON string below
json = "{}"
# create an instance of SelfStorageLocationServiceAccounts from a JSON string
self_storage_location_service_accounts_instance = SelfStorageLocationServiceAccounts.from_json(json)
# print the JSON string representation of the object
print(SelfStorageLocationServiceAccounts.to_json())

# convert the object into a dict
self_storage_location_service_accounts_dict = self_storage_location_service_accounts_instance.to_dict()
# create an instance of SelfStorageLocationServiceAccounts from a dict
self_storage_location_service_accounts_from_dict = SelfStorageLocationServiceAccounts.from_dict(self_storage_location_service_accounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


