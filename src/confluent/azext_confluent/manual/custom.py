# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.cli.core.util import sdk_no_wait, user_confirmation


def confluent_organization_create(cmd,
                                  client,
                                  resource_group_name,
                                  organization_name,
                                  plan_id,
                                  plan_name,
                                  term_unit,
                                  tags=None,
                                  location=None,
                                  publisher_id=None,
                                  offer_id=None,
                                  no_wait=False):
    import jwt
    from azure.cli.core._profile import Profile
    from azure.cli.core.azclierror import UnauthorizedError
    from azure.cli.command_modules.role.custom import list_role_assignments

    token_info = Profile(cli_ctx=cmd.cli_ctx).get_raw_token()[0][2]
    decode = jwt.decode(token_info['accessToken'], verify=False, algorithms=['RS256'])
    body = {}
    body['user_detail'] = {}
    try:
        body['user_detail']['first_name'] = decode['given_name']
        body['user_detail']['last_name'] = decode['family_name']
        body['user_detail']['email_address'] = decode['email'] if 'email' in decode else decode['unique_name']
    except KeyError as ex:
        raise UnauthorizedError(f'Cannot create the organization as CLI cannot get the right value for {str(ex)} from access '
                        'token.') from ex

    # Check owner or contributor role of subscription
    user_object_id = decode['oid']
    role_assignments = list_role_assignments(cmd, assignee=user_object_id, role='Owner') + \
        list_role_assignments(cmd, assignee=user_object_id, role='Contributor')
    if not role_assignments:
        raise UnauthorizedError('You must have Owner or Contributor role of the subscription to create an organization.')

    body['tags'] = tags
    body['location'] = location
    body['offer_detail'] = {}
    body['offer_detail']['publisher_id'] = publisher_id
    body['offer_detail']['id'] = offer_id
    body['offer_detail']['plan_id'] = plan_id
    body['offer_detail']['plan_name'] = plan_name
    body['offer_detail']['term_unit'] = term_unit

    return sdk_no_wait(no_wait,
                       client.begin_create,
                       resource_group_name=resource_group_name,
                       organization_name=organization_name,
                       body=body)


def confluent_organization_delete(client,
                                  resource_group_name,
                                  organization_name,
                                  no_wait=False,
                                  yes=None):
    if not yes:
        org = client.get(resource_group_name=resource_group_name,
                         organization_name=organization_name)
        default_msg = '- This action cannot be undone.\n' \
                      f'- This will permanently delete \'{organization_name}\' and its Azure subscription.\n' \
                      '- Stop billing for the selected Confluent organization through Azure Marketplace.\n' \
                      'Do you want to proceed'

        if org.offer_detail.plan_id in ['confluent-cloud-azure-payg-prod', 'confluent-cloud-azure-payg-stag']:
            user_confirmation(default_msg)
        else:
            user_confirmation('- The action cannot be undone and will permanently delete this resource.\n'
                              '- Resource deletion is a permanent action. All the resources, contract purchased '
                              'and its Azure integration will be permanently deleted and will unsubscribe you '
                              'from this service.\n'
                              '- If you delete the resource, you will not be able to restore the commit contract '
                              'and create Confluent cloud resource once again with this contract.\n'
                              '- If you are deleting the Confluent cloud resource after 14 days into the contract '
                              'term, you will not get a refund for this service.\n'
                              '- The resource is also associated with other non-dependent resources like clusters'
                              ', environments, topics etc. Such associated resources on Confluent cloud will be '
                              'scheduled for deletion. For more information on the Confluent Cloud cluster '
                              'deletion process and timeline, please contact Confluent Support: '
                              'https://support.confluent.io/\n'
                              'Do you want to proceed')

    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       organization_name=organization_name)


def confluent_offer_detail_show(cmd, publisher_id=None, offer_id=None):
    from azure.cli.core.util import send_raw_request
    from azure.cli.core.azclierror import ArgumentUsageError
    url = f"https://management.azure.com/providers/Microsoft.Marketplace/offers/{publisher_id}.{offer_id}?" \
        "excludePublic=true&api-version=2018-08-01-beta"
    response = send_raw_request(cmd.cli_ctx, 'get', url)
    try:
        plans = response.json()['plans']
        plans = [{'planId': plan['planId'],
                  'planName': plan['displayName'],
                  'offerId': offer_id,
                  'publisherId': publisher_id,
                  'termUnits':[{
                      'price': item['price'],
                      'termDescription': item['termDescription'],
                      'termUnits': item['termUnits']
                  } for a in plan['availabilities'] for item in a['terms']]
                  } for plan in plans]
    except KeyError as ex:
        raise ArgumentUsageError('Not able to get offer details for the provided publisher id and offer id.') from ex

    for plan in plans:
        for term in plan['termUnits']:
            if term['termUnits'] not in ['P1M', 'P1Y']:
                del term['termUnits']

    return plans
