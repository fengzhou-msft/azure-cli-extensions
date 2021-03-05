# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_datashare_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_datashare.vendored_sdks.datashare import DataShareManagementClient
    return get_mgmt_service_client(cli_ctx,
                                   DataShareManagementClient)


def cf_account(cli_ctx, *_):
    return cf_datashare_cl(cli_ctx).accounts


def cf_consumer_invitation(cli_ctx, *_):
    return cf_datashare_cl(cli_ctx).consumer_invitations


def cf_data_set(cli_ctx, *_):
    return cf_datashare_cl(cli_ctx).data_sets


def cf_data_set_mapping(cli_ctx, *_):
    return cf_datashare_cl(cli_ctx).data_set_mappings


def cf_invitation(cli_ctx, *_):
    return cf_datashare_cl(cli_ctx).invitations


def cf_share(cli_ctx, *_):
    return cf_datashare_cl(cli_ctx).shares


def cf_provider_share_subscription(cli_ctx, *_):
    return cf_datashare_cl(cli_ctx).provider_share_subscriptions


def cf_share_subscription(cli_ctx, *_):
    return cf_datashare_cl(cli_ctx).share_subscriptions


def cf_synchronization_setting(cli_ctx, *_):
    return cf_datashare_cl(cli_ctx).synchronization_settings


def cf_trigger(cli_ctx, *_):
    return cf_datashare_cl(cli_ctx).triggers
