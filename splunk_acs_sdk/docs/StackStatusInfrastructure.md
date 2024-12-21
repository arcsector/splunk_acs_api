# StackStatusInfrastructure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stack_type** | **str** | the type of the stack (Victoria/Classic) | [optional] 
**stack_version** | **str** | the version of the stack | [optional] 
**status** | **str** | the status of the infrastructure 1) Ready - The stack is ready, and infrastructure is up to date. 2) Pending - The stack has some pending changes that haven&#39;t been applied to the stack yet. The changes could be internal system changes for stacks or user requested changes like modification to allow lists. 3) Failed - There were some errors while applying changes to the stacks were being applied. The changes could be internal system changes for stacks or user requested changes like modification to allow lists. User should reach out to Splunk support for resolution. | [optional] 

## Example

```python
from splunk_acs_sdk.models.stack_status_infrastructure import StackStatusInfrastructure

# TODO update the JSON string below
json = "{}"
# create an instance of StackStatusInfrastructure from a JSON string
stack_status_infrastructure_instance = StackStatusInfrastructure.from_json(json)
# print the JSON string representation of the object
print(StackStatusInfrastructure.to_json())

# convert the object into a dict
stack_status_infrastructure_dict = stack_status_infrastructure_instance.to_dict()
# create an instance of StackStatusInfrastructure from a dict
stack_status_infrastructure_from_dict = StackStatusInfrastructure.from_dict(stack_status_infrastructure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


