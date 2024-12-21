# RestartResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.restart_response import RestartResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RestartResponse from a JSON string
restart_response_instance = RestartResponse.from_json(json)
# print the JSON string representation of the object
print(RestartResponse.to_json())

# convert the object into a dict
restart_response_dict = restart_response_instance.to_dict()
# create an instance of RestartResponse from a dict
restart_response_from_dict = RestartResponse.from_dict(restart_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


