# MaintenanceWindowsChangeFreezeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_initiated_freezes** | [**List[MaintenanceWindowsCustomerInitiatedFreezeRequest]**](MaintenanceWindowsCustomerInitiatedFreezeRequest.md) |  | 

## Example

```python
from splunk_acs_sdk.models.maintenance_windows_change_freeze_request import MaintenanceWindowsChangeFreezeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceWindowsChangeFreezeRequest from a JSON string
maintenance_windows_change_freeze_request_instance = MaintenanceWindowsChangeFreezeRequest.from_json(json)
# print the JSON string representation of the object
print(MaintenanceWindowsChangeFreezeRequest.to_json())

# convert the object into a dict
maintenance_windows_change_freeze_request_dict = maintenance_windows_change_freeze_request_instance.to_dict()
# create an instance of MaintenanceWindowsChangeFreezeRequest from a dict
maintenance_windows_change_freeze_request_from_dict = MaintenanceWindowsChangeFreezeRequest.from_dict(maintenance_windows_change_freeze_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


