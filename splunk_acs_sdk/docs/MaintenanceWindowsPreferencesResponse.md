# MaintenanceWindowsPreferencesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_freezes** | [**MaintenanceWindowsChangeFreezeResponse**](MaintenanceWindowsChangeFreezeResponse.md) |  | 
**record_version** | **int** | Version of the record. | 

## Example

```python
from splunk_acs_sdk.models.maintenance_windows_preferences_response import MaintenanceWindowsPreferencesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceWindowsPreferencesResponse from a JSON string
maintenance_windows_preferences_response_instance = MaintenanceWindowsPreferencesResponse.from_json(json)
# print the JSON string representation of the object
print(MaintenanceWindowsPreferencesResponse.to_json())

# convert the object into a dict
maintenance_windows_preferences_response_dict = maintenance_windows_preferences_response_instance.to_dict()
# create an instance of MaintenanceWindowsPreferencesResponse from a dict
maintenance_windows_preferences_response_from_dict = MaintenanceWindowsPreferencesResponse.from_dict(maintenance_windows_preferences_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


