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

from knack.help_files import helps


helps['confluent organization'] = """
    type: group
    short-summary: Manage organization with confluent
"""

helps['confluent organization list'] = """
    type: command
    short-summary: "List all Organizations under the specified resource group. And List all organizations under the \
specified subscription."
    examples:
      - name: Organization_ListByResourceGroup
        text: |-
               az confluent organization list --resource-group "myResourceGroup"
      - name: Organization_ListBySubscription
        text: |-
               az confluent organization list
"""

helps['confluent organization show'] = """
    type: command
    short-summary: "Get the properties of a specific Organization resource."
    examples:
      - name: Organization_Get
        text: |-
               az confluent organization show --name "myOrganization" --resource-group "myResourceGroup"
"""

helps['confluent organization create'] = """
    type: command
    short-summary: "Create Organization resource."
    parameters:
      - name: --offer-detail
        short-summary: "Confluent offer detail"
        long-summary: |
            Usage: --offer-detail publisher-id=XX id=XX plan-id=XX plan-name=XX term-unit=XX status=XX

            publisher-id: Publisher Id
            id: Offer Id
            plan-id: Offer Plan Id
            plan-name: Offer Plan Name
            term-unit: Offer Plan Term unit
            status: SaaS Offer Status
      - name: --user-detail
        short-summary: "Subscriber detail"
        long-summary: |
            Usage: --user-detail first-name=XX last-name=XX email-address=XX

            first-name: First name
            last-name: Last name
            email-address: Email address
    examples:
      - name: Organization_Create
        text: |-
               az confluent organization create --location "West US" --offer-detail id="string" plan-id="string" \
plan-name="string" publisher-id="string" term-unit="string" --user-detail email-address="contoso@microsoft.com" \
first-name="string" last-name="string" --tags Environment="Dev" --name "myOrganization" --resource-group \
"myResourceGroup"
"""

helps['confluent organization update'] = """
    type: command
    short-summary: "Update Organization resource."
    examples:
      - name: Confluent_Update
        text: |-
               az confluent organization update --tags client="dev-client" env="dev" --name "myOrganization" \
--resource-group "myResourceGroup"
"""

helps['confluent organization delete'] = """
    type: command
    short-summary: "Delete Organization resource."
    examples:
      - name: Confluent_Delete
        text: |-
               az confluent organization delete --name "myOrganization" --resource-group "myResourceGroup"
"""

helps['confluent organization wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the confluent organization is met.
    examples:
      - name: Pause executing next line of CLI script until the confluent organization is successfully created.
        text: |-
               az confluent organization wait --name "myOrganization" --resource-group "myResourceGroup" --created
      - name: Pause executing next line of CLI script until the confluent organization is successfully deleted.
        text: |-
               az confluent organization wait --name "myOrganization" --resource-group "myResourceGroup" --deleted
"""
