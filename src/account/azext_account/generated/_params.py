# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azext_account.action import AddProperties


def load_arguments(self, _):

    with self.argument_context('account subscription rename') as c:
        c.argument('subscription_id', help='Subscription Id.')
        c.argument('subscription_name', help='New subscription name')

    with self.argument_context('account subscription cancel') as c:
        c.argument('subscription_id', help='Subscription Id.')

    with self.argument_context('account subscription enable') as c:
        c.argument('subscription_id', help='Subscription Id.')

    with self.argument_context('account subscription list') as c:
        pass

    with self.argument_context('account subscription show') as c:
        c.argument('subscription_id', help='The ID of the target subscription.', id_part='subscription')

    with self.argument_context('account subscription list-location') as c:
        c.argument('subscription_id', help='The ID of the target subscription.')

    with self.argument_context('account tenant list') as c:
        pass

    with self.argument_context('account alias list') as c:
        pass

    with self.argument_context('account alias show') as c:
        c.argument('alias_name', options_list=['--name', '-n'], help='Alias Name')

    with self.argument_context('account alias create') as c:
        c.argument('alias_name', options_list=['--name', '-n'], help='Alias Name')
        c.argument('properties', action=AddProperties, nargs='+', help='Put alias request properties.')

    with self.argument_context('account alias delete') as c:
        c.argument('alias_name', options_list=['--name', '-n'], help='Alias Name')

    with self.argument_context('account alias wait') as c:
        c.argument('alias_name', options_list=['--name', '-n'], help='Alias Name')
