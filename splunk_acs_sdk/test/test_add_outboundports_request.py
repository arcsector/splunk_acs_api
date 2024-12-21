# coding: utf-8

"""
    Splunk Cloud Admin API

    API for managing splunk cloud stacks. (c) 2020 Splunk Inc. All rights reserved. I acknowledge that Splunk is not responsible for the installation or use of any application that is not a supported Splunk application and Splunk specifically disclaims the accuracy, integrity, quality, legality, usefulness or security of such application or its use. Installation and use of an application that is not a supported Splunk application is at your own risk. Please note that if data leaves Splunk Cloud as a result of installing or using such application, Splunk’s security attestations do not apply to data outside Splunk Cloud. Learn more about installing private apps (link to https://docs.splunk.com/Documentation/SplunkCloud/8.2.2109/Config/ManageApps). Access and use is subject to the Splunk General Terms (https://www.splunk.com/en_us/legal/splunk-general-terms.html) and Splunk's Website Terms and Conditions (https://www.splunk.com/en_us/legal/terms/terms-of-use.html).

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.add_outboundports_request import AddOutboundportsRequest

class TestAddOutboundportsRequest(unittest.TestCase):
    """AddOutboundportsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddOutboundportsRequest:
        """Test AddOutboundportsRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddOutboundportsRequest`
        """
        model = AddOutboundportsRequest()
        if include_optional:
            return AddOutboundportsRequest(
                outbound_ports = [
                    openapi_client.models.add_outboundports_request_outbound_ports_inner.AddOutboundports_request_outboundPorts_inner(
                        port = 56, 
                        subnets = [
                            ''
                            ], )
                    ],
                reason = ''
            )
        else:
            return AddOutboundportsRequest(
        )
        """

    def testAddOutboundportsRequest(self):
        """Test AddOutboundportsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
