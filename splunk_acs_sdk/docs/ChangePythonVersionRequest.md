# ChangePythonVersionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**python_version** | **str** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.change_python_version_request import ChangePythonVersionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangePythonVersionRequest from a JSON string
change_python_version_request_instance = ChangePythonVersionRequest.from_json(json)
# print the JSON string representation of the object
print(ChangePythonVersionRequest.to_json())

# convert the object into a dict
change_python_version_request_dict = change_python_version_request_instance.to_dict()
# create an instance of ChangePythonVersionRequest from a dict
change_python_version_request_from_dict = ChangePythonVersionRequest.from_dict(change_python_version_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


