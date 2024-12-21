# PutEmekKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_arn** | **str** |  | 

## Example

```python
from splunk_acs_sdk.models.put_emek_key_request import PutEmekKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutEmekKeyRequest from a JSON string
put_emek_key_request_instance = PutEmekKeyRequest.from_json(json)
# print the JSON string representation of the object
print(PutEmekKeyRequest.to_json())

# convert the object into a dict
put_emek_key_request_dict = put_emek_key_request_instance.to_dict()
# create an instance of PutEmekKeyRequest from a dict
put_emek_key_request_from_dict = PutEmekKeyRequest.from_dict(put_emek_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


