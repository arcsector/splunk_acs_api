# MaintenanceWindowsCustomerInitiatedFreezeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applies_to** | **str** | Type of changes the change freeze applies to. | 
**created_timestamp** | **datetime** | Time at which the change freeze was created. | 
**end_date** | **str** | Date (YYYY/MM/DD) when the change freeze ends. | 
**id** | **str** | UUID of the change freeze. | 
**last_modified_timestamp** | **datetime** | Time at which the change freeze was last modified. | 
**reason** | **str** | Reason for the change freeze. | 
**start_date** | **str** | Date (YYYY/MM/DD) when the change freeze starts. | 
**tickets** | **List[str]** | SFDC Tickets associated with the change freeze request. | 

## Example

```python
from splunk_acs_sdk.models.maintenance_windows_customer_initiated_freeze_response import MaintenanceWindowsCustomerInitiatedFreezeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceWindowsCustomerInitiatedFreezeResponse from a JSON string
maintenance_windows_customer_initiated_freeze_response_instance = MaintenanceWindowsCustomerInitiatedFreezeResponse.from_json(json)
# print the JSON string representation of the object
print(MaintenanceWindowsCustomerInitiatedFreezeResponse.to_json())

# convert the object into a dict
maintenance_windows_customer_initiated_freeze_response_dict = maintenance_windows_customer_initiated_freeze_response_instance.to_dict()
# create an instance of MaintenanceWindowsCustomerInitiatedFreezeResponse from a dict
maintenance_windows_customer_initiated_freeze_response_from_dict = MaintenanceWindowsCustomerInitiatedFreezeResponse.from_dict(maintenance_windows_customer_initiated_freeze_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


