# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from knack.help_files import helps


helps['confluent'] = """
    type: group
    short-summary: Manage confluent resources
"""

helps['confluent organization show'] = """
    type: command
    short-summary: "Get the properties of a specific Organization resource."
    examples:
      - name: Show organization
        text: |-
               az confluent organization show --name "myOrganization" --resource-group "myResourceGroup"
      - name: Show organization using IDs
        text: |-
               az confluent organization show --ids "/subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/Microsoft.Confluent/organizations/{myOrganization}"
"""

helps['confluent organization delete'] = """
    type: command
    short-summary: "Delete Organization resource."
    examples:
      - name: Delete organization
        text: |-
               az confluent organization delete --name "myOrganization" --resource-group "myResourceGroup"
      - name: Delete organization using IDs
        text: |-
               az confluent organization delete --ids "/subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/Microsoft.Confluent/organizations/{myOrganization}"
"""

helps['confluent offer-detail'] = """
    type: group
    short-summary: Manage confluent offer details
"""

helps['confluent offer-detail show'] = """
    type: command
    short-summary: "Get the offer details for available offers."
    examples:
      - name: Show default offer details
        text: |-
               az confluent offer-detail show
"""
