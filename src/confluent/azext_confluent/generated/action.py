# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=protected-access

import argparse
from collections import defaultdict
from knack.util import CLIError


class AddProperties(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.properties = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'publisher':
                d['publisher'] = v[0]
            elif kl == 'product':
                d['product'] = v[0]
            elif kl == 'plan':
                d['plan'] = v[0]
            elif kl == 'license-text-link':
                d['license_text_link'] = v[0]
            elif kl == 'privacy-policy-link':
                d['privacy_policy_link'] = v[0]
            elif kl == 'retrieve-datetime':
                d['retrieve_datetime'] = v[0]
            elif kl == 'signature':
                d['signature'] = v[0]
            elif kl == 'accepted':
                d['accepted'] = v[0]
        return d


class AddOfferDetail(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.offer_detail = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'publisher-id':
                d['publisher_id'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            elif kl == 'plan-id':
                d['plan_id'] = v[0]
            elif kl == 'plan-name':
                d['plan_name'] = v[0]
            elif kl == 'term-unit':
                d['term_unit'] = v[0]
            elif kl == 'status':
                d['status'] = v[0]
        return d


class AddUserDetail(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.user_detail = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'first-name':
                d['first_name'] = v[0]
            elif kl == 'last-name':
                d['last_name'] = v[0]
            elif kl == 'email-address':
                d['email_address'] = v[0]
        return d
