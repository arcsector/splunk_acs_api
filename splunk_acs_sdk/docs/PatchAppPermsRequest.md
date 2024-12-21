# PatchAppPermsRequest

patch permissions apps body

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read** | **List[str]** |  | [optional] 
**write** | **List[str]** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.patch_app_perms_request import PatchAppPermsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchAppPermsRequest from a JSON string
patch_app_perms_request_instance = PatchAppPermsRequest.from_json(json)
# print the JSON string representation of the object
print(PatchAppPermsRequest.to_json())

# convert the object into a dict
patch_app_perms_request_dict = patch_app_perms_request_instance.to_dict()
# create an instance of PatchAppPermsRequest from a dict
patch_app_perms_request_from_dict = PatchAppPermsRequest.from_dict(patch_app_perms_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


