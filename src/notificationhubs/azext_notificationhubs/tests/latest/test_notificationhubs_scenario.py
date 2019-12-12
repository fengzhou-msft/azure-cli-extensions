# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest
import time

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer, JMESPathCheck)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class NotificationHubsScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_notificationhubs')
    def test_notificationhubs(self, resource_group):

        self.kwargs.update({
            'name': 'test1',
        })

        self.cmd('az notificationhubs check_availability --name "my-hub-ns" -o json', checks=[JMESPathCheck('isAvailiable', 'True')])
        self.cmd('az notificationhubs create --namespace-name "my-hub-ns" --location "japaneast" -o json', checks=[JMESPathCheck('name', 'my-hub-ns')])
        if self.is_live:
            time.sleep(20)
        self.cmd('az notificationhubs show --namespace-name "my-hub-ns" -o json', checks=[JMESPathCheck('name', 'my-hub-ns')])
        self.cmd('az notificationhubs list -o json', checks=[])
        # self.cmd('az notificationhubs get_authorization_rule --namespace-name "my-hub-ns" --name "RootManageSharedAccessKey"', checks=[JMESPathCheck('name', 'RootManageSharedAccessKey')])
        #self.cmd('az notificationhubs update --namespace-name "my-hub-ns" --tags "type=test" -o json', checks=[JMESPathCheck('tags.type', 'test')])
        #self.cmd('az notificationhubs create_or_update_authorization_rule --namespace-name "my-hub-ns" --name "sdk-AuthRules-1788"', checks=[])

        self.cmd('az notificationhubs notification-hub check_notification_hub_availability --namespace-name "my-hub-ns" --name "my-hub-73" -o json', checks=[JMESPathCheck('isAvailiable', 'True')])
        self.cmd('az notificationhubs notification-hub create --namespace-name "my-hub-ns" --notification-hub-name "my-hub-73" --location "japaneast" -o json', checks=[JMESPathCheck('name', 'my-hub-73')])
        if self.is_live:
            time.sleep(20)
        # self.cmd('az notificationhubs notification-hub get_authorization_rule --namespace-name "my-hub-ns" --notification-hub-name "my-hub-73" --name "DefaultListenSharedAccessSignature"', checks=[JMESPathCheck('rights[0]', 'Listen')])    
        self.cmd('az notificationhubs notification-hub show --namespace-name "my-hub-ns" --notification-hub-name "my-hub-73"', checks=[])    
        if self.is_live:
            time.sleep(20)
        self.cmd('az notificationhubs delete --namespace-name "my-hub-ns"', checks=[])
