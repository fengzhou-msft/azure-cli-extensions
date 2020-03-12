# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ExtendedLivyListSessionResponse(Model):
    """ExtendedLivyListSessionResponse.

    :param from_property:
    :type from_property: int
    :param total:
    :type total: int
    :param sessions:
    :type sessions: list[~azure.synapse.models.ExtendedLivySessionResponse]
    """

    _attribute_map = {
        'from_property': {'key': 'from', 'type': 'int'},
        'total': {'key': 'total', 'type': 'int'},
        'sessions': {'key': 'sessions', 'type': '[ExtendedLivySessionResponse]'},
    }

    def __init__(self, **kwargs):
        super(ExtendedLivyListSessionResponse, self).__init__(**kwargs)
        self.from_property = kwargs.get('from_property', None)
        self.total = kwargs.get('total', None)
        self.sessions = kwargs.get('sessions', None)
