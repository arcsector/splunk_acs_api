# splunk-acs-sdk
API for managing splunk cloud stacks. (c) 2020 Splunk Inc. All rights reserved. I acknowledge that Splunk is not responsible for the installation or use of any application that is not a supported Splunk application and Splunk specifically disclaims the accuracy, integrity, quality, legality, usefulness or security of such application or its use. Installation and use of an application that is not a supported Splunk application is at your own risk. Please note that if data leaves Splunk Cloud as a result of installing or using such application, Splunk’s security attestations do not apply to data outside Splunk Cloud. Learn more about installing private apps (link to https://docs.splunk.com/Documentation/SplunkCloud/8.2.2109/Config/ManageApps). Access and use is subject to the Splunk General Terms (https://www.splunk.com/en_us/legal/splunk-general-terms.html) and Splunk's Website Terms and Conditions (https://www.splunk.com/en_us/legal/terms/terms-of-use.html).

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v2
- Package version: 1.0.0
- Generator version: 7.10.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import splunk_acs_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import splunk_acs_sdk
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import splunk_acs_sdk
from splunk_acs_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = splunk_acs_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = splunk_acs_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with splunk_acs_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = splunk_acs_sdk.AppsApi(api_client)
    stack = 'stack_example' # str | the stack name
    app = 'app_example' # str | the app name

    try:
        api_response = api_instance.describe_app(stack, app)
        print("The response of AppsApi->describe_app:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppsApi->describe_app: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AppsApi* | [**describe_app**](docs/AppsApi.md#describe_app) | **GET** /{stack}/adminconfig/v2/apps/{app} | 
*AppsApi* | [**install_app**](docs/AppsApi.md#install_app) | **POST** /{stack}/adminconfig/v2/apps | 
*AppsApi* | [**list_apps**](docs/AppsApi.md#list_apps) | **GET** /{stack}/adminconfig/v2/apps | 
*AppsApi* | [**uninstall_app**](docs/AppsApi.md#uninstall_app) | **DELETE** /{stack}/adminconfig/v2/apps/{app} | 
*AppsClassicApi* | [**patch_app_classic**](docs/AppsClassicApi.md#patch_app_classic) | **PATCH** /{stack}/adminconfig/v2/apps/{app} | 
*AppsVictoriaApi* | [**describe_app_victoria**](docs/AppsVictoriaApi.md#describe_app_victoria) | **GET** /{stack}/adminconfig/v2/apps/victoria/{app} | 
*AppsVictoriaApi* | [**download_app_export_victoria**](docs/AppsVictoriaApi.md#download_app_export_victoria) | **GET** /{stack}/adminconfig/v2/apps/victoria/export/download/{app} | 
*AppsVictoriaApi* | [**install_app_victoria**](docs/AppsVictoriaApi.md#install_app_victoria) | **POST** /{stack}/adminconfig/v2/apps/victoria | 
*AppsVictoriaApi* | [**list_apps_victoria**](docs/AppsVictoriaApi.md#list_apps_victoria) | **GET** /{stack}/adminconfig/v2/apps/victoria | 
*AppsVictoriaApi* | [**patch_app_victoria**](docs/AppsVictoriaApi.md#patch_app_victoria) | **PATCH** /{stack}/adminconfig/v2/apps/victoria/{app} | 
*AppsVictoriaApi* | [**uninstall_app_victoria**](docs/AppsVictoriaApi.md#uninstall_app_victoria) | **DELETE** /{stack}/adminconfig/v2/apps/victoria/{app} | 
*CapabilitiesApi* | [**list_capabilities**](docs/CapabilitiesApi.md#list_capabilities) | **GET** /{stack}/adminconfig/v2/capabilities | 
*CloudResourcesApi* | [**create_self_storage_location**](docs/CloudResourcesApi.md#create_self_storage_location) | **POST** /{stack}/adminconfig/v2/cloud-resources/self-storage-locations/buckets | 
*CloudResourcesApi* | [**describe_managed_glue_resources**](docs/CloudResourcesApi.md#describe_managed_glue_resources) | **GET** /{stack}/adminconfig/v2/cloud-resources/managed-glue-resources | 
*CloudResourcesApi* | [**describe_self_storage_location**](docs/CloudResourcesApi.md#describe_self_storage_location) | **GET** /{stack}/adminconfig/v2/cloud-resources/self-storage-locations/buckets/{bucketPath} | 
*CloudResourcesApi* | [**get_self_storage_location_policy**](docs/CloudResourcesApi.md#get_self_storage_location_policy) | **GET** /{stack}/adminconfig/v2/cloud-resources/self-storage-locations/buckets/{bucketName}/policy | 
*CloudResourcesApi* | [**get_self_storage_location_prefix**](docs/CloudResourcesApi.md#get_self_storage_location_prefix) | **GET** /{stack}/adminconfig/v2/cloud-resources/self-storage-locations/configs/prefix | 
*CloudResourcesApi* | [**get_self_storage_location_service_accounts**](docs/CloudResourcesApi.md#get_self_storage_location_service_accounts) | **GET** /{stack}/adminconfig/v2/cloud-resources/self-storage-locations/configs/service-accounts | 
*CloudResourcesApi* | [**list_self_storage_locations**](docs/CloudResourcesApi.md#list_self_storage_locations) | **GET** /{stack}/adminconfig/v2/cloud-resources/self-storage-locations/buckets | 
*CloudResourcesApi* | [**update_managed_glue_resources**](docs/CloudResourcesApi.md#update_managed_glue_resources) | **PUT** /{stack}/adminconfig/v2/cloud-resources/managed-glue-resources | 
*DDSSApi* | [**create_self_storage_location**](docs/DDSSApi.md#create_self_storage_location) | **POST** /{stack}/adminconfig/v2/cloud-resources/self-storage-locations/buckets | 
*DDSSApi* | [**describe_self_storage_location**](docs/DDSSApi.md#describe_self_storage_location) | **GET** /{stack}/adminconfig/v2/cloud-resources/self-storage-locations/buckets/{bucketPath} | 
*DDSSApi* | [**get_self_storage_location_policy**](docs/DDSSApi.md#get_self_storage_location_policy) | **GET** /{stack}/adminconfig/v2/cloud-resources/self-storage-locations/buckets/{bucketName}/policy | 
*DDSSApi* | [**get_self_storage_location_prefix**](docs/DDSSApi.md#get_self_storage_location_prefix) | **GET** /{stack}/adminconfig/v2/cloud-resources/self-storage-locations/configs/prefix | 
*DDSSApi* | [**get_self_storage_location_service_accounts**](docs/DDSSApi.md#get_self_storage_location_service_accounts) | **GET** /{stack}/adminconfig/v2/cloud-resources/self-storage-locations/configs/service-accounts | 
*DDSSApi* | [**list_self_storage_locations**](docs/DDSSApi.md#list_self_storage_locations) | **GET** /{stack}/adminconfig/v2/cloud-resources/self-storage-locations/buckets | 
*EMEKApi* | [**describe_emek_waiver**](docs/EMEKApi.md#describe_emek_waiver) | **GET** /{stack}/adminconfig/v2/emek/waiver | 
*EMEKApi* | [**get_emek_policy**](docs/EMEKApi.md#get_emek_policy) | **GET** /{stack}/adminconfig/v2/emek/key-policy | 
*EMEKApi* | [**put_emek_key**](docs/EMEKApi.md#put_emek_key) | **PUT** /{stack}/adminconfig/v2/emek/key | 
*EnablementApi* | [**describe_app_feature_enablement**](docs/EnablementApi.md#describe_app_feature_enablement) | **GET** /{stack}/adminconfig/v2/enablement/{appGroup}/{featureName} | 
*EnablementApi* | [**set_app_feature_enablement**](docs/EnablementApi.md#set_app_feature_enablement) | **POST** /{stack}/adminconfig/v2/enablement/{appGroup}/{featureName} | 
*IndexesApi* | [**create_index**](docs/IndexesApi.md#create_index) | **POST** /{stack}/adminconfig/v2/indexes | 
*IndexesApi* | [**delete_index**](docs/IndexesApi.md#delete_index) | **DELETE** /{stack}/adminconfig/v2/indexes/{index} | 
*IndexesApi* | [**get_index_info**](docs/IndexesApi.md#get_index_info) | **GET** /{stack}/adminconfig/v2/indexes/{index} | 
*IndexesApi* | [**list_indexes**](docs/IndexesApi.md#list_indexes) | **GET** /{stack}/adminconfig/v2/indexes | 
*IndexesApi* | [**patch_index_info**](docs/IndexesApi.md#patch_index_info) | **PATCH** /{stack}/adminconfig/v2/indexes/{index} | 
*LimitsApi* | [**add_limit_config**](docs/LimitsApi.md#add_limit_config) | **POST** /{stack}/adminconfig/v2/limits/{stanza} | 
*LimitsApi* | [**get_all_limits_config**](docs/LimitsApi.md#get_all_limits_config) | **GET** /{stack}/adminconfig/v2/limits | 
*LimitsApi* | [**get_all_limits_config_defaults**](docs/LimitsApi.md#get_all_limits_config_defaults) | **GET** /{stack}/adminconfig/v2/limits/defaults | 
*LimitsApi* | [**get_key_limit_config**](docs/LimitsApi.md#get_key_limit_config) | **GET** /{stack}/adminconfig/v2/limits/{stanza}/{key} | 
*LimitsApi* | [**get_limit_config**](docs/LimitsApi.md#get_limit_config) | **GET** /{stack}/adminconfig/v2/limits/{stanza} | 
*LimitsApi* | [**get_limits_config_defaults**](docs/LimitsApi.md#get_limits_config_defaults) | **GET** /{stack}/adminconfig/v2/limits/{stanza}/defaults | 
*LimitsApi* | [**reset_limit_config**](docs/LimitsApi.md#reset_limit_config) | **POST** /{stack}/adminconfig/v2/limits/{stanza}/reset | 
*MaintenanceWindowsApi* | [**audit_maintenance_windows_schedule**](docs/MaintenanceWindowsApi.md#audit_maintenance_windows_schedule) | **GET** /{stack}/adminconfig/v2/maintenance-windows/schedules/{scheduleID}/audits | 
*MaintenanceWindowsApi* | [**describe_maintenance_windows_preferences**](docs/MaintenanceWindowsApi.md#describe_maintenance_windows_preferences) | **GET** /{stack}/adminconfig/v2/maintenance-windows/preferences | 
*MaintenanceWindowsApi* | [**describe_maintenance_windows_schedule**](docs/MaintenanceWindowsApi.md#describe_maintenance_windows_schedule) | **GET** /{stack}/adminconfig/v2/maintenance-windows/schedules/{scheduleID} | 
*MaintenanceWindowsApi* | [**list_maintenance_windows_schedules**](docs/MaintenanceWindowsApi.md#list_maintenance_windows_schedules) | **GET** /{stack}/adminconfig/v2/maintenance-windows/schedules | 
*MaintenanceWindowsApi* | [**update_maintenance_windows_preferences**](docs/MaintenanceWindowsApi.md#update_maintenance_windows_preferences) | **PUT** /{stack}/adminconfig/v2/maintenance-windows/preferences | 
*ManagedGlueResourcesApi* | [**describe_managed_glue_resources**](docs/ManagedGlueResourcesApi.md#describe_managed_glue_resources) | **GET** /{stack}/adminconfig/v2/cloud-resources/managed-glue-resources | 
*ManagedGlueResourcesApi* | [**update_managed_glue_resources**](docs/ManagedGlueResourcesApi.md#update_managed_glue_resources) | **PUT** /{stack}/adminconfig/v2/cloud-resources/managed-glue-resources | 
*ObservabilityApi* | [**enable_rbac_on_o11y**](docs/ObservabilityApi.md#enable_rbac_on_o11y) | **PUT** /{stack}/adminconfig/v2/observability/enable-centralized-rbac | 
*ObservabilityApi* | [**get_observability_pairing_status**](docs/ObservabilityApi.md#get_observability_pairing_status) | **GET** /{stack}/adminconfig/v2/observability/sso-pairing/{pairingId} | 
*ObservabilityApi* | [**post_observability_capabilities_on_splunk**](docs/ObservabilityApi.md#post_observability_capabilities_on_splunk) | **POST** /{stack}/adminconfig/v2/observability/capabilities | 
*ObservabilityApi* | [**post_observability_pairing**](docs/ObservabilityApi.md#post_observability_pairing) | **POST** /{stack}/adminconfig/v2/observability/sso-pairing | 
*PermissionsAppsApi* | [**describe_permissions_apps**](docs/PermissionsAppsApi.md#describe_permissions_apps) | **GET** /{stack}/adminconfig/v2/permissions/apps/{app} | 
*PermissionsAppsApi* | [**list_permissions_apps**](docs/PermissionsAppsApi.md#list_permissions_apps) | **GET** /{stack}/adminconfig/v2/permissions/apps | 
*PermissionsAppsApi* | [**patch_permissions_apps**](docs/PermissionsAppsApi.md#patch_permissions_apps) | **PATCH** /{stack}/adminconfig/v2/permissions/apps/{app} | 
*PlatformOrchestratorApi* | [**describe_workflow**](docs/PlatformOrchestratorApi.md#describe_workflow) | **GET** /{stack}/adminconfig/v2/workflows/{workflowName} | 
*PrivateConnectivityApi* | [**describe_private_connectivity**](docs/PrivateConnectivityApi.md#describe_private_connectivity) | **GET** /{stack}/adminconfig/v2/private-connectivity/endpoints | 
*PrivateConnectivityApi* | [**enable_private_connectivity**](docs/PrivateConnectivityApi.md#enable_private_connectivity) | **POST** /{stack}/adminconfig/v2/private-connectivity/endpoints | 
*PrivateConnectivityApi* | [**update_private_connectivity**](docs/PrivateConnectivityApi.md#update_private_connectivity) | **PATCH** /{stack}/adminconfig/v2/private-connectivity/endpoints | 
*PrivateConnectivityApi* | [**validate_private_connectivity**](docs/PrivateConnectivityApi.md#validate_private_connectivity) | **GET** /{stack}/adminconfig/v2/private-connectivity/eligibility | 
*PrivateLinkApi* | [**describe_private_connectivity**](docs/PrivateLinkApi.md#describe_private_connectivity) | **GET** /{stack}/adminconfig/v2/private-connectivity/endpoints | 
*PrivateLinkApi* | [**enable_private_connectivity**](docs/PrivateLinkApi.md#enable_private_connectivity) | **POST** /{stack}/adminconfig/v2/private-connectivity/endpoints | 
*PrivateLinkApi* | [**update_private_connectivity**](docs/PrivateLinkApi.md#update_private_connectivity) | **PATCH** /{stack}/adminconfig/v2/private-connectivity/endpoints | 
*PrivateLinkApi* | [**validate_private_connectivity**](docs/PrivateLinkApi.md#validate_private_connectivity) | **GET** /{stack}/adminconfig/v2/private-connectivity/eligibility | 
*PythonApi* | [**get_python_version**](docs/PythonApi.md#get_python_version) | **GET** /{stack}/adminconfig/v2/python-runtime | 
*PythonVersionApi* | [**change_python_version**](docs/PythonVersionApi.md#change_python_version) | **POST** /{stack}/adminconfig/v2/python-runtime | 
*RolesApi* | [**create_role**](docs/RolesApi.md#create_role) | **POST** /{stack}/adminconfig/v2/roles | 
*RolesApi* | [**delete_role**](docs/RolesApi.md#delete_role) | **DELETE** /{stack}/adminconfig/v2/roles/{roleName} | 
*RolesApi* | [**describe_role**](docs/RolesApi.md#describe_role) | **GET** /{stack}/adminconfig/v2/roles/{roleName} | 
*RolesApi* | [**list_roles**](docs/RolesApi.md#list_roles) | **GET** /{stack}/adminconfig/v2/roles | 
*RolesApi* | [**patch_role_info**](docs/RolesApi.md#patch_role_info) | **PATCH** /{stack}/adminconfig/v2/roles/{roleName} | 
*TokensApi* | [**create_token**](docs/TokensApi.md#create_token) | **POST** /{stack}/adminconfig/v2/tokens | 
*TokensApi* | [**delete_token**](docs/TokensApi.md#delete_token) | **DELETE** /{stack}/adminconfig/v2/tokens/{tokenID} | 
*TokensApi* | [**get_token_info**](docs/TokensApi.md#get_token_info) | **GET** /{stack}/adminconfig/v2/tokens/{tokenID} | 
*TokensApi* | [**list_tokens**](docs/TokensApi.md#list_tokens) | **GET** /{stack}/adminconfig/v2/tokens | 
*UsersApi* | [**create_user**](docs/UsersApi.md#create_user) | **POST** /{stack}/adminconfig/v2/users | 
*UsersApi* | [**delete_user**](docs/UsersApi.md#delete_user) | **DELETE** /{stack}/adminconfig/v2/users/{userName} | 
*UsersApi* | [**describe_user**](docs/UsersApi.md#describe_user) | **GET** /{stack}/adminconfig/v2/users/{userName} | 
*UsersApi* | [**list_users**](docs/UsersApi.md#list_users) | **GET** /{stack}/adminconfig/v2/users | 
*UsersApi* | [**patch_user**](docs/UsersApi.md#patch_user) | **PATCH** /{stack}/adminconfig/v2/users/{userName} | 
*AllowlistApi* | [**add_subnets**](docs/AllowlistApi.md#add_subnets) | **POST** /{stack}/adminconfig/v2/access/{feature}/ipallowlists | 
*AllowlistApi* | [**delete_subnet**](docs/AllowlistApi.md#delete_subnet) | **DELETE** /{stack}/adminconfig/v2/access/{feature}/ipallowlists/{subnet} | 
*AllowlistApi* | [**delete_subnets**](docs/AllowlistApi.md#delete_subnets) | **DELETE** /{stack}/adminconfig/v2/access/{feature}/ipallowlists | 
*AllowlistApi* | [**describe_allowlist**](docs/AllowlistApi.md#describe_allowlist) | **GET** /{stack}/adminconfig/v2/access/{feature}/ipallowlists | 
*AllowlistApi* | [**describe_allowlist_v6**](docs/AllowlistApi.md#describe_allowlist_v6) | **GET** /{stack}/adminconfig/v2/access/{feature}/ipallowlists-v6 | 
*DefaultApi* | [**create_hec**](docs/DefaultApi.md#create_hec) | **POST** /{stack}/adminconfig/v2/inputs/http-event-collectors | 
*DefaultApi* | [**delete_hec**](docs/DefaultApi.md#delete_hec) | **DELETE** /{stack}/adminconfig/v2/inputs/http-event-collectors/{hec} | 
*DefaultApi* | [**describe_hec**](docs/DefaultApi.md#describe_hec) | **GET** /{stack}/adminconfig/v2/inputs/http-event-collectors/{hec} | 
*DefaultApi* | [**list_hecs**](docs/DefaultApi.md#list_hecs) | **GET** /{stack}/adminconfig/v2/inputs/http-event-collectors | 
*DefaultApi* | [**patch_hec**](docs/DefaultApi.md#patch_hec) | **PATCH** /{stack}/adminconfig/v2/inputs/http-event-collectors/{hec} | 
*DefaultApi* | [**update_hec**](docs/DefaultApi.md#update_hec) | **PUT** /{stack}/adminconfig/v2/inputs/http-event-collectors/{hec} | 
*Ipv6Api* | [**describe_allowlist_v6**](docs/Ipv6Api.md#describe_allowlist_v6) | **GET** /{stack}/adminconfig/v2/access/{feature}/ipallowlists-v6 | 
*OutboundApi* | [**add_outboundports**](docs/OutboundApi.md#add_outboundports) | **POST** /{stack}/adminconfig/v2/access/outbound-ports | 
*OutboundApi* | [**delete_outboundport**](docs/OutboundApi.md#delete_outboundport) | **DELETE** /{stack}/adminconfig/v2/access/outbound-ports/{port} | 
*OutboundApi* | [**describe_outboundports**](docs/OutboundApi.md#describe_outboundports) | **GET** /{stack}/adminconfig/v2/access/outbound-ports/{port} | 
*OutboundApi* | [**get_outboundports**](docs/OutboundApi.md#get_outboundports) | **GET** /{stack}/adminconfig/v2/access/outbound-ports | 
*RestartApi* | [**restart_stack**](docs/RestartApi.md#restart_stack) | **POST** /{stack}/adminconfig/v2/restart-now | 
*RestartApi* | [**restart_status**](docs/RestartApi.md#restart_status) | **GET** /{stack}/adminconfig/v2/restart/status | 
*SystemApi* | [**describe_deployment**](docs/SystemApi.md#describe_deployment) | **GET** /{stack}/adminconfig/v2/deployment/status/{deploymentID} | 
*SystemApi* | [**describe_stack**](docs/SystemApi.md#describe_stack) | **GET** /{stack}/adminconfig/v2/status | 
*SystemApi* | [**list_deployment**](docs/SystemApi.md#list_deployment) | **GET** /{stack}/adminconfig/v2/deployment/status | 
*SystemApi* | [**retry_deployment**](docs/SystemApi.md#retry_deployment) | **POST** /{stack}/adminconfig/v2/deployment/retry | 


## Documentation For Models

 - [AddOutboundportsRequest](docs/AddOutboundportsRequest.md)
 - [AddOutboundportsRequestOutboundPortsInner](docs/AddOutboundportsRequestOutboundPortsInner.md)
 - [AddSubnetsRequest](docs/AddSubnetsRequest.md)
 - [App](docs/App.md)
 - [AppFeatureEnablement](docs/AppFeatureEnablement.md)
 - [AppPerms](docs/AppPerms.md)
 - [AppPermsList](docs/AppPermsList.md)
 - [AppPermsProperties](docs/AppPermsProperties.md)
 - [AslProviderProperties](docs/AslProviderProperties.md)
 - [CapabilitiesInfo](docs/CapabilitiesInfo.md)
 - [ChangePythonVersionRequest](docs/ChangePythonVersionRequest.md)
 - [CreateEcSsoPairingResponse](docs/CreateEcSsoPairingResponse.md)
 - [CreateHEC202Response](docs/CreateHEC202Response.md)
 - [CreateToken200Response](docs/CreateToken200Response.md)
 - [CreateUserRequest](docs/CreateUserRequest.md)
 - [DeleteOutboundportRequest](docs/DeleteOutboundportRequest.md)
 - [DeploymentInfo](docs/DeploymentInfo.md)
 - [DeploymentStatus](docs/DeploymentStatus.md)
 - [DescribeAllowlist200Response](docs/DescribeAllowlist200Response.md)
 - [DescribeAllowlistV6200Response](docs/DescribeAllowlistV6200Response.md)
 - [DescribeEligibilityPrivateConnectivity](docs/DescribeEligibilityPrivateConnectivity.md)
 - [DescribeHec200Response](docs/DescribeHec200Response.md)
 - [DescribeManagedGlueResources](docs/DescribeManagedGlueResources.md)
 - [DescribePrivateConnectivity](docs/DescribePrivateConnectivity.md)
 - [DescribeStack200Response](docs/DescribeStack200Response.md)
 - [DescribeWorkflowResponseObject](docs/DescribeWorkflowResponseObject.md)
 - [EmekKeyUploadResponse](docs/EmekKeyUploadResponse.md)
 - [EmekPolicy](docs/EmekPolicy.md)
 - [EnableObservabilityCapabilitiesResponse](docs/EnableObservabilityCapabilitiesResponse.md)
 - [EnablePrivateConnectivity](docs/EnablePrivateConnectivity.md)
 - [Error](docs/Error.md)
 - [Extra](docs/Extra.md)
 - [GetEcSsoPairingStatusResponse](docs/GetEcSsoPairingStatusResponse.md)
 - [GetIndexInfo200Response](docs/GetIndexInfo200Response.md)
 - [GetLimitConfig200Response](docs/GetLimitConfig200Response.md)
 - [GetOutboundports200Response](docs/GetOutboundports200Response.md)
 - [HecInfo](docs/HecInfo.md)
 - [HecSpec](docs/HecSpec.md)
 - [ImportedRolesInfo](docs/ImportedRolesInfo.md)
 - [IndexInfo](docs/IndexInfo.md)
 - [IndexResponse](docs/IndexResponse.md)
 - [LimitConfigurationInfo](docs/LimitConfigurationInfo.md)
 - [LimitConfigurationResponse](docs/LimitConfigurationResponse.md)
 - [LimitResetSettingsList](docs/LimitResetSettingsList.md)
 - [LimitSetting](docs/LimitSetting.md)
 - [LimitStanza](docs/LimitStanza.md)
 - [ListApps200Response](docs/ListApps200Response.md)
 - [ListDeployment200Response](docs/ListDeployment200Response.md)
 - [ListHECs200Response](docs/ListHECs200Response.md)
 - [ListIndexes200Response](docs/ListIndexes200Response.md)
 - [ListPermissionsApps200Response](docs/ListPermissionsApps200Response.md)
 - [ListRoles200Response](docs/ListRoles200Response.md)
 - [ListSelfStorageLocations200Response](docs/ListSelfStorageLocations200Response.md)
 - [ListTokens200Response](docs/ListTokens200Response.md)
 - [ListUsers200Response](docs/ListUsers200Response.md)
 - [MaintenanceWindowsAuditResponse](docs/MaintenanceWindowsAuditResponse.md)
 - [MaintenanceWindowsChangeFreezeRequest](docs/MaintenanceWindowsChangeFreezeRequest.md)
 - [MaintenanceWindowsChangeFreezeResponse](docs/MaintenanceWindowsChangeFreezeResponse.md)
 - [MaintenanceWindowsCustomerInitiatedFreezeRequest](docs/MaintenanceWindowsCustomerInitiatedFreezeRequest.md)
 - [MaintenanceWindowsCustomerInitiatedFreezeResponse](docs/MaintenanceWindowsCustomerInitiatedFreezeResponse.md)
 - [MaintenanceWindowsOperation](docs/MaintenanceWindowsOperation.md)
 - [MaintenanceWindowsPreferencesRequest](docs/MaintenanceWindowsPreferencesRequest.md)
 - [MaintenanceWindowsPreferencesResponse](docs/MaintenanceWindowsPreferencesResponse.md)
 - [MaintenanceWindowsResponse](docs/MaintenanceWindowsResponse.md)
 - [MaintenanceWindowsSchedule](docs/MaintenanceWindowsSchedule.md)
 - [MaintenanceWindowsSplunkInitiatedFreezeResponse](docs/MaintenanceWindowsSplunkInitiatedFreezeResponse.md)
 - [ManagedGlueResources](docs/ManagedGlueResources.md)
 - [OutboundResponse](docs/OutboundResponse.md)
 - [PartitionProjection](docs/PartitionProjection.md)
 - [PatchAppPermsRequest](docs/PatchAppPermsRequest.md)
 - [PatchIndexInfo](docs/PatchIndexInfo.md)
 - [PatchUserRequest](docs/PatchUserRequest.md)
 - [PostRolesRequest](docs/PostRolesRequest.md)
 - [PrivateConnectivityEndpoints](docs/PrivateConnectivityEndpoints.md)
 - [PutEmekKeyRequest](docs/PutEmekKeyRequest.md)
 - [PythonVersionResponse](docs/PythonVersionResponse.md)
 - [RestartResponse](docs/RestartResponse.md)
 - [RestartStatus](docs/RestartStatus.md)
 - [RestartStatus200Response](docs/RestartStatus200Response.md)
 - [RetryDeployment200Response](docs/RetryDeployment200Response.md)
 - [RolesInfo](docs/RolesInfo.md)
 - [RolesRequest](docs/RolesRequest.md)
 - [RolesResponse](docs/RolesResponse.md)
 - [SelfStorageLocationBody](docs/SelfStorageLocationBody.md)
 - [SelfStorageLocationInfo](docs/SelfStorageLocationInfo.md)
 - [SelfStorageLocationPolicy](docs/SelfStorageLocationPolicy.md)
 - [SelfStorageLocationPrefix](docs/SelfStorageLocationPrefix.md)
 - [SelfStorageLocationServiceAccounts](docs/SelfStorageLocationServiceAccounts.md)
 - [SelfStorageLocationServiceAccountsResponse](docs/SelfStorageLocationServiceAccountsResponse.md)
 - [StackStatus](docs/StackStatus.md)
 - [StackStatusInfrastructure](docs/StackStatusInfrastructure.md)
 - [StackStatusMessages](docs/StackStatusMessages.md)
 - [TokenBody](docs/TokenBody.md)
 - [TokenInfo](docs/TokenInfo.md)
 - [UpdateManagedGlueResources](docs/UpdateManagedGlueResources.md)
 - [UpdatePrivateConnectivity](docs/UpdatePrivateConnectivity.md)
 - [UsersResponse](docs/UsersResponse.md)
 - [WarningResponse](docs/WarningResponse.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="basicAuth"></a>
### basicAuth

- **Type**: HTTP basic authentication

<a id="bearerAuth"></a>
### bearerAuth

- **Type**: Bearer authentication (JWT)


## Author



