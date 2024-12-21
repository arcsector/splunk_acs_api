# StackStatusMessages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**restart_required** | **bool** | The stack has a notification to restart splunk server. User should restart stack via UI for all configurations to be completed. It may take some time for the correct state for restart-required field to be populated in a Search Head Cluster, given sync delays with different Search Heads | [optional] 

## Example

```python
from splunk_acs_sdk.models.stack_status_messages import StackStatusMessages

# TODO update the JSON string below
json = "{}"
# create an instance of StackStatusMessages from a JSON string
stack_status_messages_instance = StackStatusMessages.from_json(json)
# print the JSON string representation of the object
print(StackStatusMessages.to_json())

# convert the object into a dict
stack_status_messages_dict = stack_status_messages_instance.to_dict()
# create an instance of StackStatusMessages from a dict
stack_status_messages_from_dict = StackStatusMessages.from_dict(stack_status_messages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


