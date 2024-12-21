# MaintenanceWindowsCustomerInitiatedFreezeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applies_to** | **str** | Type of changes the change freeze applies to. | 
**end_date** | **str** | Date (YYYY/MM/DD) when the change freeze ends. | 
**id** | **str** | Unique identifier (UUID) of the change freeze. This field should be left empty for new change freezes. | [optional] 
**reason** | **str** | Reason for the change freeze. | 
**start_date** | **str** | Date (YYYY/MM/DD) when the change freeze starts. | 

## Example

```python
from splunk_acs_sdk.models.maintenance_windows_customer_initiated_freeze_request import MaintenanceWindowsCustomerInitiatedFreezeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceWindowsCustomerInitiatedFreezeRequest from a JSON string
maintenance_windows_customer_initiated_freeze_request_instance = MaintenanceWindowsCustomerInitiatedFreezeRequest.from_json(json)
# print the JSON string representation of the object
print(MaintenanceWindowsCustomerInitiatedFreezeRequest.to_json())

# convert the object into a dict
maintenance_windows_customer_initiated_freeze_request_dict = maintenance_windows_customer_initiated_freeze_request_instance.to_dict()
# create an instance of MaintenanceWindowsCustomerInitiatedFreezeRequest from a dict
maintenance_windows_customer_initiated_freeze_request_from_dict = MaintenanceWindowsCustomerInitiatedFreezeRequest.from_dict(maintenance_windows_customer_initiated_freeze_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


