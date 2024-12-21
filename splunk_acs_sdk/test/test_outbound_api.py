# coding: utf-8

"""
    Splunk Cloud Admin API

    API for managing splunk cloud stacks. (c) 2020 Splunk Inc. All rights reserved. I acknowledge that Splunk is not responsible for the installation or use of any application that is not a supported Splunk application and Splunk specifically disclaims the accuracy, integrity, quality, legality, usefulness or security of such application or its use. Installation and use of an application that is not a supported Splunk application is at your own risk. Please note that if data leaves Splunk Cloud as a result of installing or using such application, Splunk’s security attestations do not apply to data outside Splunk Cloud. Learn more about installing private apps (link to https://docs.splunk.com/Documentation/SplunkCloud/8.2.2109/Config/ManageApps). Access and use is subject to the Splunk General Terms (https://www.splunk.com/en_us/legal/splunk-general-terms.html) and Splunk's Website Terms and Conditions (https://www.splunk.com/en_us/legal/terms/terms-of-use.html).

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.outbound_api import OutboundApi


class TestOutboundApi(unittest.TestCase):
    """OutboundApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OutboundApi()

    def tearDown(self) -> None:
        pass

    def test_add_outboundports(self) -> None:
        """Test case for add_outboundports

        """
        pass

    def test_delete_outboundport(self) -> None:
        """Test case for delete_outboundport

        """
        pass

    def test_describe_outboundports(self) -> None:
        """Test case for describe_outboundports

        """
        pass

    def test_get_outboundports(self) -> None:
        """Test case for get_outboundports

        """
        pass


if __name__ == '__main__':
    unittest.main()
