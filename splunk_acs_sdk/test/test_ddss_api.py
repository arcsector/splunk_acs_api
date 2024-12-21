# coding: utf-8

"""
    Splunk Cloud Admin API

    API for managing splunk cloud stacks. (c) 2020 Splunk Inc. All rights reserved. I acknowledge that Splunk is not responsible for the installation or use of any application that is not a supported Splunk application and Splunk specifically disclaims the accuracy, integrity, quality, legality, usefulness or security of such application or its use. Installation and use of an application that is not a supported Splunk application is at your own risk. Please note that if data leaves Splunk Cloud as a result of installing or using such application, Splunk’s security attestations do not apply to data outside Splunk Cloud. Learn more about installing private apps (link to https://docs.splunk.com/Documentation/SplunkCloud/8.2.2109/Config/ManageApps). Access and use is subject to the Splunk General Terms (https://www.splunk.com/en_us/legal/splunk-general-terms.html) and Splunk's Website Terms and Conditions (https://www.splunk.com/en_us/legal/terms/terms-of-use.html).

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.ddss_api import DDSSApi


class TestDDSSApi(unittest.TestCase):
    """DDSSApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DDSSApi()

    def tearDown(self) -> None:
        pass

    def test_create_self_storage_location(self) -> None:
        """Test case for create_self_storage_location

        """
        pass

    def test_describe_self_storage_location(self) -> None:
        """Test case for describe_self_storage_location

        """
        pass

    def test_get_self_storage_location_policy(self) -> None:
        """Test case for get_self_storage_location_policy

        """
        pass

    def test_get_self_storage_location_prefix(self) -> None:
        """Test case for get_self_storage_location_prefix

        """
        pass

    def test_get_self_storage_location_service_accounts(self) -> None:
        """Test case for get_self_storage_location_service_accounts

        """
        pass

    def test_list_self_storage_locations(self) -> None:
        """Test case for list_self_storage_locations

        """
        pass


if __name__ == '__main__':
    unittest.main()