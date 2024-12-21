# ListHECs200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_event_collectors** | [**List[HecInfo]**](HecInfo.md) |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.list_hecs200_response import ListHECs200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListHECs200Response from a JSON string
list_hecs200_response_instance = ListHECs200Response.from_json(json)
# print the JSON string representation of the object
print(ListHECs200Response.to_json())

# convert the object into a dict
list_hecs200_response_dict = list_hecs200_response_instance.to_dict()
# create an instance of ListHECs200Response from a dict
list_hecs200_response_from_dict = ListHECs200Response.from_dict(list_hecs200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


