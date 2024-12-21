# ImportedRolesInfo


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
**roles** | **List[str]** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.imported_roles_info import ImportedRolesInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ImportedRolesInfo from a JSON string
imported_roles_info_instance = ImportedRolesInfo.from_json(json)
# print the JSON string representation of the object
print(ImportedRolesInfo.to_json())

# convert the object into a dict
imported_roles_info_dict = imported_roles_info_instance.to_dict()
# create an instance of ImportedRolesInfo from a dict
imported_roles_info_from_dict = ImportedRolesInfo.from_dict(imported_roles_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


