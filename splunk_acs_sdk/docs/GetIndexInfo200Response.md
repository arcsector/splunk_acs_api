# GetIndexInfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indexinfo** | [**IndexResponse**](IndexResponse.md) |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.get_index_info200_response import GetIndexInfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetIndexInfo200Response from a JSON string
get_index_info200_response_instance = GetIndexInfo200Response.from_json(json)
# print the JSON string representation of the object
print(GetIndexInfo200Response.to_json())

# convert the object into a dict
get_index_info200_response_dict = get_index_info200_response_instance.to_dict()
# create an instance of GetIndexInfo200Response from a dict
get_index_info200_response_from_dict = GetIndexInfo200Response.from_dict(get_index_info200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


