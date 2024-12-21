# AppFeatureEnablement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.app_feature_enablement import AppFeatureEnablement

# TODO update the JSON string below
json = "{}"
# create an instance of AppFeatureEnablement from a JSON string
app_feature_enablement_instance = AppFeatureEnablement.from_json(json)
# print the JSON string representation of the object
print(AppFeatureEnablement.to_json())

# convert the object into a dict
app_feature_enablement_dict = app_feature_enablement_instance.to_dict()
# create an instance of AppFeatureEnablement from a dict
app_feature_enablement_from_dict = AppFeatureEnablement.from_dict(app_feature_enablement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


