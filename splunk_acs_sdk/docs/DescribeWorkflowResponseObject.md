# DescribeWorkflowResponseObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**finished_at** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**started_at** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.describe_workflow_response_object import DescribeWorkflowResponseObject

# TODO update the JSON string below
json = "{}"
# create an instance of DescribeWorkflowResponseObject from a JSON string
describe_workflow_response_object_instance = DescribeWorkflowResponseObject.from_json(json)
# print the JSON string representation of the object
print(DescribeWorkflowResponseObject.to_json())

# convert the object into a dict
describe_workflow_response_object_dict = describe_workflow_response_object_instance.to_dict()
# create an instance of DescribeWorkflowResponseObject from a dict
describe_workflow_response_object_from_dict = DescribeWorkflowResponseObject.from_dict(describe_workflow_response_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


