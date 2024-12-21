# StackStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**infrastructure** | [**StackStatusInfrastructure**](StackStatusInfrastructure.md) |  | 
**messages** | [**StackStatusMessages**](StackStatusMessages.md) |  | 

## Example

```python
from splunk_acs_sdk.models.stack_status import StackStatus

# TODO update the JSON string below
json = "{}"
# create an instance of StackStatus from a JSON string
stack_status_instance = StackStatus.from_json(json)
# print the JSON string representation of the object
print(StackStatus.to_json())

# convert the object into a dict
stack_status_dict = stack_status_instance.to_dict()
# create an instance of StackStatus from a dict
stack_status_from_dict = StackStatus.from_dict(stack_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


