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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class MaintenanceWindowsCustomerInitiatedFreezeRequest(BaseModel):
    """
    MaintenanceWindowsCustomerInitiatedFreezeRequest
    """ # noqa: E501
    applies_to: StrictStr = Field(description="Type of changes the change freeze applies to.", alias="appliesTo")
    end_date: StrictStr = Field(description="Date (YYYY/MM/DD) when the change freeze ends.", alias="endDate")
    id: Optional[StrictStr] = Field(default=None, description="Unique identifier (UUID) of the change freeze. This field should be left empty for new change freezes.")
    reason: StrictStr = Field(description="Reason for the change freeze.")
    start_date: StrictStr = Field(description="Date (YYYY/MM/DD) when the change freeze starts.", alias="startDate")
    __properties: ClassVar[List[str]] = ["appliesTo", "endDate", "id", "reason", "startDate"]

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
        """Create an instance of MaintenanceWindowsCustomerInitiatedFreezeRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MaintenanceWindowsCustomerInitiatedFreezeRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "appliesTo": obj.get("appliesTo"),
            "endDate": obj.get("endDate"),
            "id": obj.get("id"),
            "reason": obj.get("reason"),
            "startDate": obj.get("startDate")
        })
        return _obj


