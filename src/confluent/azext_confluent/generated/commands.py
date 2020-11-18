# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_confluent.generated._client_factory import cf_organization
    confluent_organization = CliCommandType(
        operations_tmpl='azext_confluent.vendored_sdks.confluent.operations._organization_operations#OrganizationOperat'
        'ions.{}',
        client_factory=cf_organization)
    with self.command_group('confluent organization', confluent_organization, client_factory=cf_organization,
                            is_experimental=True) as g:
        g.custom_command('list', 'confluent_organization_list')
        g.custom_show_command('show', 'confluent_organization_show')
        g.custom_command('create', 'confluent_organization_create', supports_no_wait=True)
        g.custom_command('update', 'confluent_organization_update')
        g.custom_command('delete', 'confluent_organization_delete', supports_no_wait=True, confirmation=True)
        g.custom_wait_command('wait', 'confluent_organization_show')
