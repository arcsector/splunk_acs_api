# coding: utf-8

"""
    Splunk Cloud Admin API

    API for managing splunk cloud stacks. (c) 2020 Splunk Inc. All rights reserved. I acknowledge that Splunk is not responsible for the installation or use of any application that is not a supported Splunk application and Splunk specifically disclaims the accuracy, integrity, quality, legality, usefulness or security of such application or its use. Installation and use of an application that is not a supported Splunk application is at your own risk. Please note that if data leaves Splunk Cloud as a result of installing or using such application, Splunk’s security attestations do not apply to data outside Splunk Cloud. Learn more about installing private apps (link to https://docs.splunk.com/Documentation/SplunkCloud/8.2.2109/Config/ManageApps). Access and use is subject to the Splunk General Terms (https://www.splunk.com/en_us/legal/splunk-general-terms.html) and Splunk's Website Terms and Conditions (https://www.splunk.com/en_us/legal/terms/terms-of-use.html).

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.emek_api import EMEKApi


class TestEMEKApi(unittest.TestCase):
    """EMEKApi unit test stubs"""

    def setUp(self) -> None:
        self.api = EMEKApi()

    def tearDown(self) -> None:
        pass

    def test_describe_emek_waiver(self) -> None:
        """Test case for describe_emek_waiver

        """
        pass

    def test_get_emek_policy(self) -> None:
        """Test case for get_emek_policy

        """
        pass

    def test_put_emek_key(self) -> None:
        """Test case for put_emek_key

        """
        pass


if __name__ == '__main__':
    unittest.main()
