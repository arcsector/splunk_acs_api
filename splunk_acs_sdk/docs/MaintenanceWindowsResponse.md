# MaintenanceWindowsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_link** | **str** |  | 
**schedules** | [**List[MaintenanceWindowsSchedule]**](MaintenanceWindowsSchedule.md) |  | 

## Example

```python
from splunk_acs_sdk.models.maintenance_windows_response import MaintenanceWindowsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceWindowsResponse from a JSON string
maintenance_windows_response_instance = MaintenanceWindowsResponse.from_json(json)
# print the JSON string representation of the object
print(MaintenanceWindowsResponse.to_json())

# convert the object into a dict
maintenance_windows_response_dict = maintenance_windows_response_instance.to_dict()
# create an instance of MaintenanceWindowsResponse from a dict
maintenance_windows_response_from_dict = MaintenanceWindowsResponse.from_dict(maintenance_windows_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


