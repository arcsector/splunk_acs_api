# SelfStorageLocationServiceAccountsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**service_accounts** | [**SelfStorageLocationServiceAccounts**](SelfStorageLocationServiceAccounts.md) |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.self_storage_location_service_accounts_response import SelfStorageLocationServiceAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SelfStorageLocationServiceAccountsResponse from a JSON string
self_storage_location_service_accounts_response_instance = SelfStorageLocationServiceAccountsResponse.from_json(json)
# print the JSON string representation of the object
print(SelfStorageLocationServiceAccountsResponse.to_json())

# convert the object into a dict
self_storage_location_service_accounts_response_dict = self_storage_location_service_accounts_response_instance.to_dict()
# create an instance of SelfStorageLocationServiceAccountsResponse from a dict
self_storage_location_service_accounts_response_from_dict = SelfStorageLocationServiceAccountsResponse.from_dict(self_storage_location_service_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


