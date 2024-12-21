# MaintenanceWindowsChangeFreezeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_initiated_freezes** | [**List[MaintenanceWindowsCustomerInitiatedFreezeResponse]**](MaintenanceWindowsCustomerInitiatedFreezeResponse.md) |  | 
**splunk_initiated_freezes** | [**List[MaintenanceWindowsSplunkInitiatedFreezeResponse]**](MaintenanceWindowsSplunkInitiatedFreezeResponse.md) |  | 

## Example

```python
from splunk_acs_sdk.models.maintenance_windows_change_freeze_response import MaintenanceWindowsChangeFreezeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceWindowsChangeFreezeResponse from a JSON string
maintenance_windows_change_freeze_response_instance = MaintenanceWindowsChangeFreezeResponse.from_json(json)
# print the JSON string representation of the object
print(MaintenanceWindowsChangeFreezeResponse.to_json())

# convert the object into a dict
maintenance_windows_change_freeze_response_dict = maintenance_windows_change_freeze_response_instance.to_dict()
# create an instance of MaintenanceWindowsChangeFreezeResponse from a dict
maintenance_windows_change_freeze_response_from_dict = MaintenanceWindowsChangeFreezeResponse.from_dict(maintenance_windows_change_freeze_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


