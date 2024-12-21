# CreateUserRequest

Create user request body

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_role** | **bool** |  | [optional] 
**default_app** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**force_change_pass** | **bool** |  | [optional] 
**full_name** | **str** |  | [optional] 
**name** | **str** |  | 
**password** | **str** |  | 
**roles** | **List[str]** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.create_user_request import CreateUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserRequest from a JSON string
create_user_request_instance = CreateUserRequest.from_json(json)
# print the JSON string representation of the object
print(CreateUserRequest.to_json())

# convert the object into a dict
create_user_request_dict = create_user_request_instance.to_dict()
# create an instance of CreateUserRequest from a dict
create_user_request_from_dict = CreateUserRequest.from_dict(create_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


