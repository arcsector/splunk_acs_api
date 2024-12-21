# GetLimitConfig200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limitconfiguration** | [**LimitConfigurationResponse**](LimitConfigurationResponse.md) |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.get_limit_config200_response import GetLimitConfig200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetLimitConfig200Response from a JSON string
get_limit_config200_response_instance = GetLimitConfig200Response.from_json(json)
# print the JSON string representation of the object
print(GetLimitConfig200Response.to_json())

# convert the object into a dict
get_limit_config200_response_dict = get_limit_config200_response_instance.to_dict()
# create an instance of GetLimitConfig200Response from a dict
get_limit_config200_response_from_dict = GetLimitConfig200Response.from_dict(get_limit_config200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


