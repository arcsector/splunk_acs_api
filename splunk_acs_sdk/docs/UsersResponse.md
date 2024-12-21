# UsersResponse

Splunk user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | **List[str]** |  | 
**default_app** | **str** |  | 
**default_app_source** | **str** |  | 
**email** | **str** |  | 
**full_name** | **str** |  | 
**last_successful_login** | **str** |  | [optional] 
**locked_out** | **bool** |  | 
**name** | **str** |  | 
**roles** | **List[str]** |  | 

## Example

```python
from splunk_acs_sdk.models.users_response import UsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsersResponse from a JSON string
users_response_instance = UsersResponse.from_json(json)
# print the JSON string representation of the object
print(UsersResponse.to_json())

# convert the object into a dict
users_response_dict = users_response_instance.to_dict()
# create an instance of UsersResponse from a dict
users_response_from_dict = UsersResponse.from_dict(users_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


