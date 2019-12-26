# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    tags_type,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)


def load_arguments(self, _):

    with self.argument_context('blueprint create') as c:
        c.argument('scope', id_part=None, help='The scope of the resource. Valid scopes are: management group (format: \'/providers/Microsoft.Management/managementGroups/{managementGroup}\'), subscription (format: \'/subscriptions/{subscriptionId}\'). For blueprint assignments management group scope is reserved for future use.')
        c.argument('name', id_part=None, help='Name of the blueprint definition.')
        c.argument('display_name', id_part=None, help='One-liner string explain this resource.')
        c.argument('description', id_part=None, help='Multi-line explain this resource.')
        c.argument('target_scope', arg_type=get_enum_type(['subscription', 'managementGroup']), id_part=None, help='The scope where this blueprint definition can be assigned.')
        c.argument('parameters', id_part=None, help='Parameters required by this blueprint definition.')
        c.argument('resource_groups', id_part=None, help='Resource group placeholders defined by this blueprint definition.')
        c.argument('versions', id_part=None, help='Published versions of this blueprint definition.')
        c.argument('layout', id_part=None, help='Layout view of the blueprint definition for UI reference.')

    with self.argument_context('blueprint update') as c:
        c.argument('scope', id_part=None, help='The scope of the resource. Valid scopes are: management group (format: \'/providers/Microsoft.Management/managementGroups/{managementGroup}\'), subscription (format: \'/subscriptions/{subscriptionId}\'). For blueprint assignments management group scope is reserved for future use.')
        c.argument('name', id_part=None, help='Name of the blueprint definition.')
        c.argument('display_name', id_part=None, help='One-liner string explain this resource.')
        c.argument('description', id_part=None, help='Multi-line explain this resource.')
        c.argument('target_scope', arg_type=get_enum_type(['subscription', 'managementGroup']), id_part=None, help='The scope where this blueprint definition can be assigned.')
        c.argument('parameters', id_part=None, help='Parameters required by this blueprint definition.')
        c.argument('resource_groups', id_part=None, help='Resource group placeholders defined by this blueprint definition.')
        c.argument('versions', id_part=None, help='Published versions of this blueprint definition.')
        c.argument('layout', id_part=None, help='Layout view of the blueprint definition for UI reference.')

    with self.argument_context('blueprint delete') as c:
        c.argument('scope', id_part=None, help='The scope of the resource. Valid scopes are: management group (format: \'/providers/Microsoft.Management/managementGroups/{managementGroup}\'), subscription (format: \'/subscriptions/{subscriptionId}\'). For blueprint assignments management group scope is reserved for future use.')
        c.argument('name', id_part=None, help='Name of the blueprint definition.')

    with self.argument_context('blueprint show') as c:
        c.argument('scope', id_part=None, help='The scope of the resource. Valid scopes are: management group (format: \'/providers/Microsoft.Management/managementGroups/{managementGroup}\'), subscription (format: \'/subscriptions/{subscriptionId}\'). For blueprint assignments management group scope is reserved for future use.')
        c.argument('name', id_part=None, help='Name of the blueprint definition.')

    with self.argument_context('blueprint list') as c:
        c.argument('scope', id_part=None, help='The scope of the resource. Valid scopes are: management group (format: \'/providers/Microsoft.Management/managementGroups/{managementGroup}\'), subscription (format: \'/subscriptions/{subscriptionId}\'). For blueprint assignments management group scope is reserved for future use.')

    with self.argument_context('blueprint artifact create') as c:
        c.argument('scope', id_part=None, help='The scope of the resource. Valid scopes are: management group (format: \'/providers/Microsoft.Management/managementGroups/{managementGroup}\'), subscription (format: \'/subscriptions/{subscriptionId}\'). For blueprint assignments management group scope is reserved for future use.')
        c.argument('blueprint_name', id_part=None, help='Name of the blueprint definition.')
        c.argument('name', id_part=None, help='Name of the blueprint artifact.')

    with self.argument_context('blueprint artifact update') as c:
        c.argument('scope', id_part=None, help='The scope of the resource. Valid scopes are: management group (format: \'/providers/Microsoft.Management/managementGroups/{managementGroup}\'), subscription (format: \'/subscriptions/{subscriptionId}\'). For blueprint assignments management group scope is reserved for future use.')
        c.argument('blueprint_name', id_part=None, help='Name of the blueprint definition.')
        c.argument('name', id_part=None, help='Name of the blueprint artifact.')

    with self.argument_context('blueprint artifact delete') as c:
        c.argument('scope', id_part=None, help='The scope of the resource. Valid scopes are: management group (format: \'/providers/Microsoft.Management/managementGroups/{managementGroup}\'), subscription (format: \'/subscriptions/{subscriptionId}\'). For blueprint assignments management group scope is reserved for future use.')
        c.argument('blueprint_name', id_part=None, help='Name of the blueprint definition.')
        c.argument('name', id_part=None, help='Name of the blueprint artifact.')

    with self.argument_context('blueprint artifact show') as c:
        c.argument('scope', id_part=None, help='The scope of the resource. Valid scopes are: management group (format: \'/providers/Microsoft.Management/managementGroups/{managementGroup}\'), subscription (format: \'/subscriptions/{subscriptionId}\'). For blueprint assignments management group scope is reserved for future use.')
        c.argument('blueprint_name', id_part=None, help='Name of the blueprint definition.')
        c.argument('name', id_part=None, help='Name of the blueprint artifact.')

    with self.argument_context('blueprint artifact list') as c:
        c.argument('scope', id_part=None, help='The scope of the resource. Valid scopes are: management group (format: \'/providers/Microsoft.Management/managementGroups/{managementGroup}\'), subscription (format: \'/subscriptions/{subscriptionId}\'). For blueprint assignments management group scope is reserved for future use.')
        c.argument('blueprint_name', id_part=None, help='Name of the blueprint definition.')

    with self.argument_context('blueprint published create') as c:
        c.argument('scope', id_part=None, help='The scope of the resource. Valid scopes are: management group (format: \'/providers/Microsoft.Management/managementGroups/{managementGroup}\'), subscription (format: \'/subscriptions/{subscriptionId}\'). For blueprint assignments management group scope is reserved for future use.')
        c.argument('name', id_part=None, help='Name of the blueprint definition.')
        c.argument('version_id', id_part=None, help='Version of the published blueprint definition.')
        c.argument('display_name', id_part=None, help='One-liner string explain this resource.')
        c.argument('description', id_part=None, help='Multi-line explain this resource.')
        c.argument('target_scope', arg_type=get_enum_type(['subscription', 'managementGroup']), id_part=None, help='The scope where this blueprint definition can be assigned.')
        c.argument('parameters', id_part=None, help='Parameters required by this blueprint definition.')
        c.argument('resource_groups', id_part=None, help='Resource group placeholders defined by this blueprint definition.')
        c.argument('blueprint_name', id_part=None, help='Name of the published blueprint definition.')
        c.argument('change_notes', id_part=None, help='Version-specific change notes.')

    with self.argument_context('blueprint published delete') as c:
        c.argument('scope', id_part=None, help='The scope of the resource. Valid scopes are: management group (format: \'/providers/Microsoft.Management/managementGroups/{managementGroup}\'), subscription (format: \'/subscriptions/{subscriptionId}\'). For blueprint assignments management group scope is reserved for future use.')
        c.argument('name', id_part=None, help='Name of the blueprint definition.')
        c.argument('version_id', id_part=None, help='Version of the published blueprint definition.')

    with self.argument_context('blueprint published show') as c:
        c.argument('scope', id_part=None, help='The scope of the resource. Valid scopes are: management group (format: \'/providers/Microsoft.Management/managementGroups/{managementGroup}\'), subscription (format: \'/subscriptions/{subscriptionId}\'). For blueprint assignments management group scope is reserved for future use.')
        c.argument('name', id_part=None, help='Name of the blueprint definition.')
        c.argument('version_id', id_part=None, help='Version of the published blueprint definition.')

    with self.argument_context('blueprint published list') as c:
        c.argument('scope', id_part=None, help='The scope of the resource. Valid scopes are: management group (format: \'/providers/Microsoft.Management/managementGroups/{managementGroup}\'), subscription (format: \'/subscriptions/{subscriptionId}\'). For blueprint assignments management group scope is reserved for future use.')
        c.argument('name', id_part=None, help='Name of the blueprint definition.')

    with self.argument_context('blueprint published artifact get') as c:
        c.argument('scope', id_part=None, help='The scope of the resource. Valid scopes are: management group (format: \'/providers/Microsoft.Management/managementGroups/{managementGroup}\'), subscription (format: \'/subscriptions/{subscriptionId}\'). For blueprint assignments management group scope is reserved for future use.')
        c.argument('blueprint_name', id_part=None, help='Name of the blueprint definition.')
        c.argument('version_id', id_part=None, help='Version of the published blueprint definition.')
        c.argument('name', id_part=None, help='Name of the blueprint artifact.')

    with self.argument_context('blueprint published artifact list') as c:
        c.argument('scope', id_part=None, help='The scope of the resource. Valid scopes are: management group (format: \'/providers/Microsoft.Management/managementGroups/{managementGroup}\'), subscription (format: \'/subscriptions/{subscriptionId}\'). For blueprint assignments management group scope is reserved for future use.')
        c.argument('blueprint_name', id_part=None, help='Name of the blueprint definition.')
        c.argument('version_id', id_part=None, help='Version of the published blueprint definition.')

    with self.argument_context('blueprint assignment create') as c:
        c.argument('scope', id_part=None, help='The scope of the resource. Valid scopes are: management group (format: \'/providers/Microsoft.Management/managementGroups/{managementGroup}\'), subscription (format: \'/subscriptions/{subscriptionId}\'). For blueprint assignments management group scope is reserved for future use.')
        c.argument('name', id_part=None, help='Name of the blueprint assignment.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('identity_type', arg_type=get_enum_type(['None', 'SystemAssigned', 'UserAssigned']), id_part=None, help='Type of the managed identity.')
        c.argument('identity_principal_id', id_part=None, help='Azure Active Directory principal ID associated with this Identity.')
        c.argument('identity_tenant_id', id_part=None, help='ID of the Azure Active Directory.')
        c.argument('identity_user_assigned_identities', id_part=None, help='The list of user-assigned managed identities associated with the resource. Key is the Azure resource Id of the managed identity.')
        c.argument('display_name', id_part=None, help='One-liner string explain this resource.')
        c.argument('description', id_part=None, help='Multi-line explain this resource.')
        c.argument('blueprint_id', id_part=None, help='ID of the published version of a blueprint definition.')
        c.argument('parameters', id_part=None, help='Blueprint assignment parameter values.')
        c.argument('resource_groups', id_part=None, help='Names and locations of resource group placeholders.')
        c.argument('locks_mode', arg_type=get_enum_type(['None', 'AllResourcesReadOnly', 'AllResourcesDoNotDelete']), id_part=None, help='Lock mode.')
        c.argument('locks_excluded_principals', id_part=None, help='List of AAD principals excluded from blueprint locks. Up to 5 principals are permitted.', nargs='+')

    with self.argument_context('blueprint assignment update') as c:
        c.argument('scope', id_part=None, help='The scope of the resource. Valid scopes are: management group (format: \'/providers/Microsoft.Management/managementGroups/{managementGroup}\'), subscription (format: \'/subscriptions/{subscriptionId}\'). For blueprint assignments management group scope is reserved for future use.')
        c.argument('name', id_part=None, help='Name of the blueprint assignment.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('identity_type', arg_type=get_enum_type(['None', 'SystemAssigned', 'UserAssigned']), id_part=None, help='Type of the managed identity.')
        c.argument('identity_principal_id', id_part=None, help='Azure Active Directory principal ID associated with this Identity.')
        c.argument('identity_tenant_id', id_part=None, help='ID of the Azure Active Directory.')
        c.argument('identity_user_assigned_identities', id_part=None, help='The list of user-assigned managed identities associated with the resource. Key is the Azure resource Id of the managed identity.')
        c.argument('display_name', id_part=None, help='One-liner string explain this resource.')
        c.argument('description', id_part=None, help='Multi-line explain this resource.')
        c.argument('blueprint_id', id_part=None, help='ID of the published version of a blueprint definition.')
        c.argument('parameters', id_part=None, help='Blueprint assignment parameter values.')
        c.argument('resource_groups', id_part=None, help='Names and locations of resource group placeholders.')
        c.argument('locks_mode', arg_type=get_enum_type(['None', 'AllResourcesReadOnly', 'AllResourcesDoNotDelete']), id_part=None, help='Lock mode.')
        c.argument('locks_excluded_principals', id_part=None, help='List of AAD principals excluded from blueprint locks. Up to 5 principals are permitted.', nargs='+')

    with self.argument_context('blueprint assignment delete') as c:
        c.argument('scope', id_part=None, help='The scope of the resource. Valid scopes are: management group (format: \'/providers/Microsoft.Management/managementGroups/{managementGroup}\'), subscription (format: \'/subscriptions/{subscriptionId}\'). For blueprint assignments management group scope is reserved for future use.')
        c.argument('name', id_part=None, help='Name of the blueprint assignment.')

    with self.argument_context('blueprint assignment show') as c:
        c.argument('scope', id_part=None, help='The scope of the resource. Valid scopes are: management group (format: \'/providers/Microsoft.Management/managementGroups/{managementGroup}\'), subscription (format: \'/subscriptions/{subscriptionId}\'). For blueprint assignments management group scope is reserved for future use.')
        c.argument('name', id_part=None, help='Name of the blueprint assignment.')

    with self.argument_context('blueprint assignment list') as c:
        c.argument('scope', id_part=None, help='The scope of the resource. Valid scopes are: management group (format: \'/providers/Microsoft.Management/managementGroups/{managementGroup}\'), subscription (format: \'/subscriptions/{subscriptionId}\'). For blueprint assignments management group scope is reserved for future use.')

    with self.argument_context('blueprint assignment who_is_blueprint') as c:
        c.argument('scope', id_part=None, help='The scope of the resource. Valid scopes are: management group (format: \'/providers/Microsoft.Management/managementGroups/{managementGroup}\'), subscription (format: \'/subscriptions/{subscriptionId}\'). For blueprint assignments management group scope is reserved for future use.')
        c.argument('name', id_part=None, help='Name of the blueprint assignment.')
