# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

import json


def databricks_workspace_list(cmd, client,
                              resource_group_name=None):
    if resource_group_name is not None:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list_by_subscription()


def databricks_workspace_show(cmd, client,
                              resource_group_name,
                              workspace_name):
    return client.get(resource_group_name=resource_group_name,
                      workspace_name=workspace_name)


def databricks_workspace_create(cmd, client,
                                resource_group_name,
                                workspace_name,
                                location,
                                managed_resource_group_id,
                                tags=None,
                                sku=None,
                                parameters=None,
                                ui_definition_uri=None,
                                authorizations=None,
                                created_by=None,
                                updated_by=None,
                                storage_account_identity=None):
    if isinstance(parameters, str):
        parameters = json.loads(parameters)
    return client.begin_create_or_update(resource_group_name=resource_group_name,
                                         workspace_name=workspace_name,
                                         tags=tags,
                                         location=location,
                                         sku=sku,
                                         managed_resource_group_id=managed_resource_group_id,
                                         parameters=parameters,
                                         ui_definition_uri=ui_definition_uri,
                                         authorizations=authorizations,
                                         created_by=created_by,
                                         updated_by=updated_by,
                                         storage_account_identity=storage_account_identity)


def databricks_workspace_update(cmd, client,
                                resource_group_name,
                                workspace_name,
                                tags=None):
    return client.begin_update(resource_group_name=resource_group_name,
                               workspace_name=workspace_name,
                               tags=tags)


def databricks_workspace_delete(cmd, client,
                                resource_group_name,
                                workspace_name):
    return client.begin_delete(resource_group_name=resource_group_name,
                               workspace_name=workspace_name)
