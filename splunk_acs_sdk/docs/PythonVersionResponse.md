# PythonVersionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**python_version** | **str** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.python_version_response import PythonVersionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PythonVersionResponse from a JSON string
python_version_response_instance = PythonVersionResponse.from_json(json)
# print the JSON string representation of the object
print(PythonVersionResponse.to_json())

# convert the object into a dict
python_version_response_dict = python_version_response_instance.to_dict()
# create an instance of PythonVersionResponse from a dict
python_version_response_from_dict = PythonVersionResponse.from_dict(python_version_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


