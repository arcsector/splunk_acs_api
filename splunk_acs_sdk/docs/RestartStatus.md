# RestartStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**captain** | **str** |  | [optional] 
**rolling_restart_initiated** | **bool** |  | [optional] 
**service_ready** | **bool** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.restart_status import RestartStatus

# TODO update the JSON string below
json = "{}"
# create an instance of RestartStatus from a JSON string
restart_status_instance = RestartStatus.from_json(json)
# print the JSON string representation of the object
print(RestartStatus.to_json())

# convert the object into a dict
restart_status_dict = restart_status_instance.to_dict()
# create an instance of RestartStatus from a dict
restart_status_from_dict = RestartStatus.from_dict(restart_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


