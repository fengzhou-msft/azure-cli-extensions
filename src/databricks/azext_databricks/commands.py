# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals
from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from ._client_factory import cf_workspaces
    databricks_workspaces = CliCommandType(
        operations_tmpl='azext_databricks.vendored_sdks.databricks.operations._workspaces_operations#WorkspacesOperations.{}',
        client_factory=cf_workspaces)
    with self.command_group('databricks workspace', databricks_workspaces, client_factory=cf_workspaces) as g:
        g.custom_command('create', 'create_databricks_workspace')
        g.custom_command('update', 'update_databricks_workspace')
        g.custom_command('delete', 'delete_databricks_workspace')
        g.custom_show_command('show', 'get_databricks_workspace')
        g.custom_command('list', 'list_databricks_workspace')

    from ._client_factory import cf_operations
    databricks_operations = CliCommandType(
        operations_tmpl='azext_databricks.vendored_sdks.databricks.operations._operations_operations#OperationsOperations.{}',
        client_factory=cf_operations)
    with self.command_group('databricks operation', databricks_operations, client_factory=cf_operations) as g:
        g.custom_command('list', 'list_databricks_operation')
