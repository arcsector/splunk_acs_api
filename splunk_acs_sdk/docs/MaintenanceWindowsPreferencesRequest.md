# MaintenanceWindowsPreferencesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_freezes** | [**MaintenanceWindowsChangeFreezeRequest**](MaintenanceWindowsChangeFreezeRequest.md) |  | 
**record_version** | **int** | Version of the record. | [optional] 

## Example

```python
from splunk_acs_sdk.models.maintenance_windows_preferences_request import MaintenanceWindowsPreferencesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceWindowsPreferencesRequest from a JSON string
maintenance_windows_preferences_request_instance = MaintenanceWindowsPreferencesRequest.from_json(json)
# print the JSON string representation of the object
print(MaintenanceWindowsPreferencesRequest.to_json())

# convert the object into a dict
maintenance_windows_preferences_request_dict = maintenance_windows_preferences_request_instance.to_dict()
# create an instance of MaintenanceWindowsPreferencesRequest from a dict
maintenance_windows_preferences_request_from_dict = MaintenanceWindowsPreferencesRequest.from_dict(maintenance_windows_preferences_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


