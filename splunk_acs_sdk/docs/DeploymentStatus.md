# DeploymentStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_deployment** | [**DeploymentInfo**](DeploymentInfo.md) |  | 

## Example

```python
from splunk_acs_sdk.models.deployment_status import DeploymentStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentStatus from a JSON string
deployment_status_instance = DeploymentStatus.from_json(json)
# print the JSON string representation of the object
print(DeploymentStatus.to_json())

# convert the object into a dict
deployment_status_dict = deployment_status_instance.to_dict()
# create an instance of DeploymentStatus from a dict
deployment_status_from_dict = DeploymentStatus.from_dict(deployment_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


