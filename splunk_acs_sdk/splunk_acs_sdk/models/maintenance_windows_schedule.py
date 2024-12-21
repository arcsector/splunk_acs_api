# coding: utf-8

"""
    Splunk Cloud Admin API

    API for managing splunk cloud stacks. (c) 2020 Splunk Inc. All rights reserved. I acknowledge that Splunk is not responsible for the installation or use of any application that is not a supported Splunk application and Splunk specifically disclaims the accuracy, integrity, quality, legality, usefulness or security of such application or its use. Installation and use of an application that is not a supported Splunk application is at your own risk. Please note that if data leaves Splunk Cloud as a result of installing or using such application, Splunk’s security attestations do not apply to data outside Splunk Cloud. Learn more about installing private apps (link to https://docs.splunk.com/Documentation/SplunkCloud/8.2.2109/Config/ManageApps). Access and use is subject to the Splunk General Terms (https://www.splunk.com/en_us/legal/splunk-general-terms.html) and Splunk's Website Terms and Conditions (https://www.splunk.com/en_us/legal/terms/terms-of-use.html).

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from splunk_acs_sdk.models.maintenance_windows_operation import MaintenanceWindowsOperation
from typing import Optional, Set
from typing_extensions import Self

class MaintenanceWindowsSchedule(BaseModel):
    """
    MaintenanceWindowsSchedule
    """ # noqa: E501
    duration: StrictStr = Field(description="The duration of the maintenance window.")
    last_modified_timestamp: datetime = Field(description="Time at which the maintenance window was last modified. Format is RFC3339.", alias="lastModifiedTimestamp")
    last_summary: Optional[StrictStr] = Field(default=None, description="The summary or reason for the maintenance.", alias="lastSummary")
    mw_type: StrictStr = Field(description="The type of upgrade performed in the maintenance window.", alias="mwType")
    operations: Optional[List[MaintenanceWindowsOperation]] = None
    requested_entity: StrictStr = Field(description="The entity which requested the maintenance window, either the customer or Splunk.", alias="requestedEntity")
    requested_user: Optional[StrictStr] = Field(default=None, description="The user who requested the maintenance window.", alias="requestedUser")
    schedule_id: StrictStr = Field(description="UUID of the maintenance window.", alias="scheduleId")
    schedule_start_timestamp: datetime = Field(description="Time at which the maintenance window is scheduled to begin. Format is RFC3339.", alias="scheduleStartTimestamp")
    status: StrictStr = Field(description="The status of the maintenance window schedule.")
    zero_downtime: StrictBool = Field(description="True if the maintenance window will have no impact on the uptime of the stack.", alias="zeroDowntime")
    __properties: ClassVar[List[str]] = ["duration", "lastModifiedTimestamp", "lastSummary", "mwType", "operations", "requestedEntity", "requestedUser", "scheduleId", "scheduleStartTimestamp", "status", "zeroDowntime"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of MaintenanceWindowsSchedule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in operations (list)
        _items = []
        if self.operations:
            for _item_operations in self.operations:
                if _item_operations:
                    _items.append(_item_operations.to_dict())
            _dict['operations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MaintenanceWindowsSchedule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "duration": obj.get("duration"),
            "lastModifiedTimestamp": obj.get("lastModifiedTimestamp"),
            "lastSummary": obj.get("lastSummary"),
            "mwType": obj.get("mwType"),
            "operations": [MaintenanceWindowsOperation.from_dict(_item) for _item in obj["operations"]] if obj.get("operations") is not None else None,
            "requestedEntity": obj.get("requestedEntity"),
            "requestedUser": obj.get("requestedUser"),
            "scheduleId": obj.get("scheduleId"),
            "scheduleStartTimestamp": obj.get("scheduleStartTimestamp"),
            "status": obj.get("status"),
            "zeroDowntime": obj.get("zeroDowntime")
        })
        return _obj


