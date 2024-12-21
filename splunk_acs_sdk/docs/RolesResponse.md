# RolesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | **List[str]** |  | [optional] 
**rt_srch_jobs_quota** | **int** |  | [optional] 
**srch_disk_quota** | **int** |  | [optional] 
**srch_filter** | **str** |  | [optional] 
**srch_indexes_allowed** | **List[str]** |  | [optional] 
**srch_indexes_default** | **List[str]** |  | [optional] 
**srch_jobs_quota** | **int** |  | [optional] 
**srch_time_earliest** | **int** |  | [optional] 
**srch_time_win** | **int** |  | [optional] 
**cumulative_rt_srch_jobs_quota** | **int** |  | [optional] 
**cumulative_srch_jobs_quota** | **int** |  | [optional] 
**default_app** | **str** |  | [optional] 
**imported** | [**ImportedRolesInfo**](ImportedRolesInfo.md) |  | [optional] 
**name** | **str** |  | 

## Example

```python
from splunk_acs_sdk.models.roles_response import RolesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RolesResponse from a JSON string
roles_response_instance = RolesResponse.from_json(json)
# print the JSON string representation of the object
print(RolesResponse.to_json())

# convert the object into a dict
roles_response_dict = roles_response_instance.to_dict()
# create an instance of RolesResponse from a dict
roles_response_from_dict = RolesResponse.from_dict(roles_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


