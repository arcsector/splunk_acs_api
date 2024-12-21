# MaintenanceWindowsOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sfdc_tickets** | **List[str]** | List of SFDC tickets associated with the operation. | [optional] 
**app_name** | **str** | Name of the app to be upgraded. | [optional] 
**end_time** | **datetime** | Time at which the operation ended. | [optional] 
**metadata** | **object** | A map containing metadata about the operation (e.g. targetVersion, lastStatusBeforeCanceled, etc...). | [optional] 
**notes** | **List[str]** | Notes for the customer. | [optional] 
**operation_description** | **str** | Description of the operation. | 
**operation_status** | **str** | Status of the operation. | 
**operation_type** | **str** | Type of the operation. | 
**start_time** | **datetime** | Time at which the operation started. | [optional] 
**target_version** | **str** | Target version after the upgrade. | [optional] 
**zero_downtime** | **bool** | True if the operation will have no impact on the uptime of the stack. | 

## Example

```python
from splunk_acs_sdk.models.maintenance_windows_operation import MaintenanceWindowsOperation

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceWindowsOperation from a JSON string
maintenance_windows_operation_instance = MaintenanceWindowsOperation.from_json(json)
# print the JSON string representation of the object
print(MaintenanceWindowsOperation.to_json())

# convert the object into a dict
maintenance_windows_operation_dict = maintenance_windows_operation_instance.to_dict()
# create an instance of MaintenanceWindowsOperation from a dict
maintenance_windows_operation_from_dict = MaintenanceWindowsOperation.from_dict(maintenance_windows_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


