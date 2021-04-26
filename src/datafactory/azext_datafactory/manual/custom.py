# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from knack.util import CLIError


def datafactory_create(client,
                       resource_group_name,
                       factory_name,
                       if_match=None,
                       location=None,
                       tags=None,
                       factory_vsts_configuration=None,
                       factory_git_hub_configuration=None,
                       global_parameters=None):
    from azext_datafactory.vendored_sdks.datafactory.models import FactoryIdentity
    from azext_datafactory.vendored_sdks.datafactory.models import FactoryIdentityType
    all_repo_configuration = []
    if factory_vsts_configuration is not None:
        all_repo_configuration.append(factory_vsts_configuration)
    if factory_git_hub_configuration is not None:
        all_repo_configuration.append(factory_git_hub_configuration)
    if len(all_repo_configuration) > 1:
        raise CLIError('at most one of  factory_vsts_configuration, factory_git_hub_configuration is needed for '
                       'repo_configuration!')
    repo_configuration = all_repo_configuration[0] if len(all_repo_configuration) == 1 else None
    factory = {}
    factory['location'] = location
    factory['tags'] = tags
    factory['repo_configuration'] = repo_configuration
    factory['global_parameters'] = global_parameters
    factory['encryption'] = {}
    factory['identity'] = FactoryIdentity(type=FactoryIdentityType.SYSTEM_ASSIGNED)
    return client.create_or_update(resource_group_name=resource_group_name,
                                   factory_name=factory_name,
                                   if_match=if_match,
                                   factory=factory)


def datafactory_update(client,
                       resource_group_name,
                       factory_name,
                       tags=None):
    factory_update_parameters = {}
    factory_update_parameters['tags'] = tags
    return client.update(resource_group_name=resource_group_name,
                         factory_name=factory_name,
                         factory_update_parameters=factory_update_parameters)
