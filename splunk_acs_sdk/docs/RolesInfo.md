# RolesInfo


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

## Example

```python
from splunk_acs_sdk.models.roles_info import RolesInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RolesInfo from a JSON string
roles_info_instance = RolesInfo.from_json(json)
# print the JSON string representation of the object
print(RolesInfo.to_json())

# convert the object into a dict
roles_info_dict = roles_info_instance.to_dict()
# create an instance of RolesInfo from a dict
roles_info_from_dict = RolesInfo.from_dict(roles_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


