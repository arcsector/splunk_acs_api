# GetEcSsoPairingStatusResponse

Status for pairing Splunk Cloud stack with Observability organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pairing_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from splunk_acs_sdk.models.get_ec_sso_pairing_status_response import GetEcSsoPairingStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEcSsoPairingStatusResponse from a JSON string
get_ec_sso_pairing_status_response_instance = GetEcSsoPairingStatusResponse.from_json(json)
# print the JSON string representation of the object
print(GetEcSsoPairingStatusResponse.to_json())

# convert the object into a dict
get_ec_sso_pairing_status_response_dict = get_ec_sso_pairing_status_response_instance.to_dict()
# create an instance of GetEcSsoPairingStatusResponse from a dict
get_ec_sso_pairing_status_response_from_dict = GetEcSsoPairingStatusResponse.from_dict(get_ec_sso_pairing_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


