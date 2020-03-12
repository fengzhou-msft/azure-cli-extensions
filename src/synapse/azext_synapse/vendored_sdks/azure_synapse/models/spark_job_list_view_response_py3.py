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


class SparkJobListViewResponse(Model):
    """SparkJobListViewResponse.

    :param n_jobs:
    :type n_jobs: int
    :param spark_jobs:
    :type spark_jobs: list[~azure.synapse.models.SparkJob]
    """

    _attribute_map = {
        'n_jobs': {'key': 'nJobs', 'type': 'int'},
        'spark_jobs': {'key': 'sparkJobs', 'type': '[SparkJob]'},
    }

    def __init__(self, *, n_jobs: int=None, spark_jobs=None, **kwargs) -> None:
        super(SparkJobListViewResponse, self).__init__(**kwargs)
        self.n_jobs = n_jobs
        self.spark_jobs = spark_jobs
