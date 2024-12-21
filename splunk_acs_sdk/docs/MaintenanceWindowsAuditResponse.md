# MaintenanceWindowsAuditResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audits** | [**List[MaintenanceWindowsSchedule]**](MaintenanceWindowsSchedule.md) |  | 

## Example

```python
from splunk_acs_sdk.models.maintenance_windows_audit_response import MaintenanceWindowsAuditResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceWindowsAuditResponse from a JSON string
maintenance_windows_audit_response_instance = MaintenanceWindowsAuditResponse.from_json(json)
# print the JSON string representation of the object
print(MaintenanceWindowsAuditResponse.to_json())

# convert the object into a dict
maintenance_windows_audit_response_dict = maintenance_windows_audit_response_instance.to_dict()
# create an instance of MaintenanceWindowsAuditResponse from a dict
maintenance_windows_audit_response_from_dict = MaintenanceWindowsAuditResponse.from_dict(maintenance_windows_audit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


