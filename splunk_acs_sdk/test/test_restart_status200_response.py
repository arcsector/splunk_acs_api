# coding: utf-8

"""
    Splunk Cloud Admin API

    API for managing splunk cloud stacks. (c) 2020 Splunk Inc. All rights reserved. I acknowledge that Splunk is not responsible for the installation or use of any application that is not a supported Splunk application and Splunk specifically disclaims the accuracy, integrity, quality, legality, usefulness or security of such application or its use. Installation and use of an application that is not a supported Splunk application is at your own risk. Please note that if data leaves Splunk Cloud as a result of installing or using such application, Splunk’s security attestations do not apply to data outside Splunk Cloud. Learn more about installing private apps (link to https://docs.splunk.com/Documentation/SplunkCloud/8.2.2109/Config/ManageApps). Access and use is subject to the Splunk General Terms (https://www.splunk.com/en_us/legal/splunk-general-terms.html) and Splunk's Website Terms and Conditions (https://www.splunk.com/en_us/legal/terms/terms-of-use.html).

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.restart_status200_response import RestartStatus200Response

class TestRestartStatus200Response(unittest.TestCase):
    """RestartStatus200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestartStatus200Response:
        """Test RestartStatus200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestartStatus200Response`
        """
        model = RestartStatus200Response()
        if include_optional:
            return RestartStatus200Response(
                shc_status = [
                    openapi_client.models.restart_status.RestartStatus(
                        captain = '', 
                        rolling_restart_initiated = True, 
                        service_ready = True, )
                    ]
            )
        else:
            return RestartStatus200Response(
        )
        """

    def testRestartStatus200Response(self):
        """Test RestartStatus200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
