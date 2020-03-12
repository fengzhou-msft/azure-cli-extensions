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


class HistoryServerDataResponse(Model):
    """HistoryServerDataResponse.

    :param data:
    :type data: ~azure.synapse.models.Data
    """

    _attribute_map = {
        'data': {'key': 'data', 'type': 'Data'},
    }

    def __init__(self, *, data=None, **kwargs) -> None:
        super(HistoryServerDataResponse, self).__init__(**kwargs)
        self.data = data
