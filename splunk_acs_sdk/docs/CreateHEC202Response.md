# CreateHEC202Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_event_collector** | [**HecSpec**](HecSpec.md) |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.create_hec202_response import CreateHEC202Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHEC202Response from a JSON string
create_hec202_response_instance = CreateHEC202Response.from_json(json)
# print the JSON string representation of the object
print(CreateHEC202Response.to_json())

# convert the object into a dict
create_hec202_response_dict = create_hec202_response_instance.to_dict()
# create an instance of CreateHEC202Response from a dict
create_hec202_response_from_dict = CreateHEC202Response.from_dict(create_hec202_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


