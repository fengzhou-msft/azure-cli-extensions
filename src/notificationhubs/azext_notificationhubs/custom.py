# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-statements
# pylint: disable=too-many-lines
# pylint: disable=too-many-locals
# pylint: disable=unused-argument


def list_notificationhubs(cmd, client):
    return client.list()


def create_notificationhubs(cmd, client,
                            resource_group,
                            namespace_name,
                            location=None,
                            tags=None,
                            sku=None,
                            is_availiable=None,
                            rights=None,
                            policy_key=None):
    body = {}
    body['location'] = location  # str
    body['tags'] = tags  # dictionary
    body['sku'] = json.loads(sku) if isinstance(sku, str) else sku
    body['is_availiable'] = is_availiable  # boolean
    body['rights'] = None if rights is None else rights.split(',')
    body['policy_key'] = policy_key  # str
    return client.create_or_update(resource_group_name=resource_group, namespace_name=namespace_name, parameters=body)


def update_notificationhubs(cmd, client,
                            resource_group,
                            namespace_name,
                            name=None,
                            location=None,
                            tags=None,
                            sku=None,
                            is_availiable=None,
                            rights=None,
                            policy_key=None):
    body = client.get(resource_group_name=resource_group, namespace_name=namespace_name).as_dict()
    if name is not None:
        body['name'] = name  # str
    if location is not None:
        body['location'] = location  # str
    if tags is not None:
        body['tags'] = tags  # dictionary
    if sku is not None:
        body['sku'] = json.loads(sku) if isinstance(sku, str) else sku
    if is_availiable is not None:
        body['is_availiable'] = is_availiable  # boolean
    if rights is not None:
        body['rights'] = None if rights is None else rights.split(',')
    if policy_key is not None:
        body['policy_key'] = policy_key  # str
    return client.create_or_update(resource_group_name=resource_group, namespace_name=namespace_name, parameters=body)


def delete_notificationhubs(cmd, client,
                            resource_group,
                            namespace_name):
    return client.delete(resource_group_name=resource_group, namespace_name=namespace_name)


def get_notificationhubs(cmd, client,
                         resource_group,
                         namespace_name):
    return client.get(resource_group_name=resource_group, namespace_name=namespace_name)


def list_notificationhubs(cmd, client,
                          resource_group):
    if resource_group is not None:
        return client.list(resource_group_name=resource_group)
    return client.list_all()


def check_availability_notificationhubs(cmd, client):
    body = {}
    return client.check_availability(parameters=body)


def list_keys_notificationhubs(cmd, client,
                               resource_group,
                               namespace_name,
                               name):
    return client.list_keys(resource_group_name=resource_group, namespace_name=namespace_name, authorization_rule_name=name)


def regenerate_keys_notificationhubs(cmd, client,
                                     resource_group,
                                     namespace_name,
                                     name):
    body = {}
    return client.regenerate_keys(resource_group_name=resource_group, namespace_name=namespace_name, authorization_rule_name=name, parameters=body)


def get_authorization_rule_notificationhubs(cmd, client,
                                            resource_group,
                                            namespace_name,
                                            name):
    return client.get_authorization_rule(resource_group_name=resource_group, namespace_name=namespace_name, authorization_rule_name=name)


def list_authorization_rules_notificationhubs(cmd, client,
                                              resource_group,
                                              namespace_name):
    return client.list_authorization_rules(resource_group_name=resource_group, namespace_name=namespace_name)


def create_or_update_authorization_rule_notificationhubs(cmd, client,
                                                         resource_group,
                                                         namespace_name,
                                                         name):
    body = {}
    return client.create_or_update_authorization_rule(resource_group_name=resource_group, namespace_name=namespace_name, authorization_rule_name=name, parameters=body)


def delete_authorization_rule_notificationhubs(cmd, client,
                                               resource_group,
                                               namespace_name,
                                               name):
    return client.delete_authorization_rule(resource_group_name=resource_group, namespace_name=namespace_name, authorization_rule_name=name)


def create_notificationhubs_notification_hub(cmd, client,
                                             resource_group,
                                             namespace_name,
                                             notification_hub_name,
                                             location=None,
                                             tags=None,
                                             sku=None,
                                             is_availiable=None,
                                             rights=None,
                                             policy_key=None):
    body = {}
    body['location'] = location  # str
    body['tags'] = tags  # dictionary
    body['sku'] = json.loads(sku) if isinstance(sku, str) else sku
    body['is_availiable'] = is_availiable  # boolean
    body['rights'] = None if rights is None else rights.split(',')
    body['policy_key'] = policy_key  # str
    return client.create_or_update(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name, parameters=body)


def update_notificationhubs_notification_hub(cmd, client,
                                             resource_group,
                                             namespace_name,
                                             notification_hub_name,
                                             name=None,
                                             location=None,
                                             tags=None,
                                             sku=None,
                                             is_availiable=None,
                                             rights=None,
                                             policy_key=None):
    body = client.get(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name).as_dict()
    if name is not None:
        body['name'] = name  # str
    if location is not None:
        body['location'] = location  # str
    if tags is not None:
        body['tags'] = tags  # dictionary
    if sku is not None:
        body['sku'] = json.loads(sku) if isinstance(sku, str) else sku
    if is_availiable is not None:
        body['is_availiable'] = is_availiable  # boolean
    if rights is not None:
        body['rights'] = None if rights is None else rights.split(',')
    if policy_key is not None:
        body['policy_key'] = policy_key  # str
    return client.create_or_update(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name, parameters=body)


def delete_notificationhubs_notification_hub(cmd, client,
                                             resource_group,
                                             namespace_name,
                                             notification_hub_name):
    return client.delete(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name)


def get_notificationhubs_notification_hub(cmd, client,
                                          resource_group,
                                          namespace_name,
                                          notification_hub_name):
    return client.get(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name)


def list_notificationhubs_notification_hub(cmd, client,
                                           resource_group,
                                           namespace_name):
    return client.list(resource_group_name=resource_group, namespace_name=namespace_name)


def check_notification_hub_availability_notificationhubs_notification_hub(cmd, client,
                                                                          resource_group,
                                                                          namespace_name):
    body = {}
    return client.check_notification_hub_availability(resource_group_name=resource_group, namespace_name=namespace_name, parameters=body)


def regenerate_keys_notificationhubs_notification_hub(cmd, client,
                                                      resource_group,
                                                      namespace_name,
                                                      notification_hub_name,
                                                      name):
    body = {}
    return client.regenerate_keys(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name, authorization_rule_name=name, parameters=body)


def get_pns_credentials_notificationhubs_notification_hub(cmd, client,
                                                          resource_group,
                                                          namespace_name,
                                                          notification_hub_name):
    return client.get_pns_credentials(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name)


def list_keys_notificationhubs_notification_hub(cmd, client,
                                                resource_group,
                                                namespace_name,
                                                notification_hub_name,
                                                name):
    return client.list_keys(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name, authorization_rule_name=name)


def debug_send_notificationhubs_notification_hub(cmd, client,
                                                 resource_group,
                                                 namespace_name,
                                                 notification_hub_name):
    body = {}
    return client.debug_send(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name, parameters=body)


def list_authorization_rules_notificationhubs_notification_hub(cmd, client,
                                                               resource_group,
                                                               namespace_name,
                                                               notification_hub_name):
    return client.list_authorization_rules(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name)


def get_authorization_rule_notificationhubs_notification_hub(cmd, client,
                                                             resource_group,
                                                             namespace_name,
                                                             notification_hub_name,
                                                             name):
    return client.get_authorization_rule(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name, authorization_rule_name=name)


def create_or_update_authorization_rule_notificationhubs_notification_hub(cmd, client,
                                                                          resource_group,
                                                                          namespace_name,
                                                                          notification_hub_name,
                                                                          name):
    body = {}
    return client.create_or_update_authorization_rule(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name, authorization_rule_name=name, parameters=body)


def delete_authorization_rule_notificationhubs_notification_hub(cmd, client,
                                                                resource_group,
                                                                namespace_name,
                                                                notification_hub_name,
                                                                name):
    return client.delete_authorization_rule(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name, authorization_rule_name=name)
