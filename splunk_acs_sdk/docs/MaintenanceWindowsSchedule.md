# MaintenanceWindowsSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **str** | The duration of the maintenance window. | 
**last_modified_timestamp** | **datetime** | Time at which the maintenance window was last modified. Format is RFC3339. | 
**last_summary** | **str** | The summary or reason for the maintenance. | [optional] 
**mw_type** | **str** | The type of upgrade performed in the maintenance window. | 
**operations** | [**List[MaintenanceWindowsOperation]**](MaintenanceWindowsOperation.md) |  | [optional] 
**requested_entity** | **str** | The entity which requested the maintenance window, either the customer or Splunk. | 
**requested_user** | **str** | The user who requested the maintenance window. | [optional] 
**schedule_id** | **str** | UUID of the maintenance window. | 
**schedule_start_timestamp** | **datetime** | Time at which the maintenance window is scheduled to begin. Format is RFC3339. | 
**status** | **str** | The status of the maintenance window schedule. | 
**zero_downtime** | **bool** | True if the maintenance window will have no impact on the uptime of the stack. | 

## Example

```python
from splunk_acs_sdk.models.maintenance_windows_schedule import MaintenanceWindowsSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceWindowsSchedule from a JSON string
maintenance_windows_schedule_instance = MaintenanceWindowsSchedule.from_json(json)
# print the JSON string representation of the object
print(MaintenanceWindowsSchedule.to_json())

# convert the object into a dict
maintenance_windows_schedule_dict = maintenance_windows_schedule_instance.to_dict()
# create an instance of MaintenanceWindowsSchedule from a dict
maintenance_windows_schedule_from_dict = MaintenanceWindowsSchedule.from_dict(maintenance_windows_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


