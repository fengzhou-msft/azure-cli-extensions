# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_acc(cmd, resource_group_name, acc_name, location=None, tags=None):
    raise CLIError('TODO: Implement `acc create`')


def list_acc(cmd, resource_group_name=None):
    raise CLIError('TODO: Implement `acc list`')


def update_acc(cmd, instance, tags=None):
    with cmd.update_context(instance) as c:
        c.set_param('tags', tags)
    return instance