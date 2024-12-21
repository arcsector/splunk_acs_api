# PatchUserRequest

Patch user request body

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_app** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**force_change_pass** | **bool** |  | [optional] 
**full_name** | **str** |  | [optional] 
**old_password** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**roles** | **List[str]** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.patch_user_request import PatchUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchUserRequest from a JSON string
patch_user_request_instance = PatchUserRequest.from_json(json)
# print the JSON string representation of the object
print(PatchUserRequest.to_json())

# convert the object into a dict
patch_user_request_dict = patch_user_request_instance.to_dict()
# create an instance of PatchUserRequest from a dict
patch_user_request_from_dict = PatchUserRequest.from_dict(patch_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


