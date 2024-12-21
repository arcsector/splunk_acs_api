# RestartStatus200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shc_status** | [**List[RestartStatus]**](RestartStatus.md) |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.restart_status200_response import RestartStatus200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestartStatus200Response from a JSON string
restart_status200_response_instance = RestartStatus200Response.from_json(json)
# print the JSON string representation of the object
print(RestartStatus200Response.to_json())

# convert the object into a dict
restart_status200_response_dict = restart_status200_response_instance.to_dict()
# create an instance of RestartStatus200Response from a dict
restart_status200_response_from_dict = RestartStatus200Response.from_dict(restart_status200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


