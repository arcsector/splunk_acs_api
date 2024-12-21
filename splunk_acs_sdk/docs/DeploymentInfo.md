# DeploymentInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the id of the latest deployment task | 
**status** | **str** | the status of the last deployment task, possible values are new, completed, pending, running, failed. | [optional] 
**timestamp** | **str** | timestamp of the latest deployment task | [optional] 

## Example

```python
from splunk_acs_sdk.models.deployment_info import DeploymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentInfo from a JSON string
deployment_info_instance = DeploymentInfo.from_json(json)
# print the JSON string representation of the object
print(DeploymentInfo.to_json())

# convert the object into a dict
deployment_info_dict = deployment_info_instance.to_dict()
# create an instance of DeploymentInfo from a dict
deployment_info_from_dict = DeploymentInfo.from_dict(deployment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


