# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AgentPool
    from ._models_py3 import AgentPoolAvailableVersions
    from ._models_py3 import AgentPoolAvailableVersionsPropertiesAgentPoolVersionsItem
    from ._models_py3 import AgentPoolUpgradeProfile
    from ._models_py3 import AgentPoolUpgradeProfilePropertiesUpgradesItem
    from ._models_py3 import AgentPoolUpgradeSettings
    from ._models_py3 import ContainerServiceDiagnosticsProfile
    from ._models_py3 import ContainerServiceLinuxProfile
    from ._models_py3 import ContainerServiceMasterProfile
    from ._models_py3 import ContainerServiceNetworkProfile
    from ._models_py3 import ContainerServiceSshConfiguration
    from ._models_py3 import ContainerServiceSshPublicKey
    from ._models_py3 import ContainerServiceVMDiagnostics
    from ._models_py3 import CredentialResult
    from ._models_py3 import CredentialResults
    from ._models_py3 import ManagedCluster
    from ._models_py3 import ManagedClusterAADProfile
    from ._models_py3 import ManagedClusterAccessProfile
    from ._models_py3 import ManagedClusterAddonProfile
    from ._models_py3 import ManagedClusterAddonProfileIdentity
    from ._models_py3 import ManagedClusterAgentPoolProfile
    from ._models_py3 import ManagedClusterAgentPoolProfileProperties
    from ._models_py3 import ManagedClusterAPIServerAccessProfile
    from ._models_py3 import ManagedClusterIdentity
    from ._models_py3 import ManagedClusterLoadBalancerProfile
    from ._models_py3 import ManagedClusterLoadBalancerProfileManagedOutboundIPs
    from ._models_py3 import ManagedClusterLoadBalancerProfileOutboundIPPrefixes
    from ._models_py3 import ManagedClusterLoadBalancerProfileOutboundIPs
    from ._models_py3 import ManagedClusterPoolUpgradeProfile
    from ._models_py3 import ManagedClusterPoolUpgradeProfileUpgradesItem
    from ._models_py3 import ManagedClusterPropertiesAutoScalerProfile
    from ._models_py3 import ManagedClusterPropertiesIdentityProfileValue
    from ._models_py3 import ManagedClusterServicePrincipalProfile
    from ._models_py3 import ManagedClusterSKU
    from ._models_py3 import ManagedClusterUpgradeProfile
    from ._models_py3 import ManagedClusterWindowsProfile
    from ._models_py3 import OperationValue
    from ._models_py3 import Resource
    from ._models_py3 import ResourceReference
    from ._models_py3 import SubResource
    from ._models_py3 import TagsObject
    from ._models_py3 import UserAssignedIdentity
except (SyntaxError, ImportError):
    from ._models import AgentPool
    from ._models import AgentPoolAvailableVersions
    from ._models import AgentPoolAvailableVersionsPropertiesAgentPoolVersionsItem
    from ._models import AgentPoolUpgradeProfile
    from ._models import AgentPoolUpgradeProfilePropertiesUpgradesItem
    from ._models import AgentPoolUpgradeSettings
    from ._models import ContainerServiceDiagnosticsProfile
    from ._models import ContainerServiceLinuxProfile
    from ._models import ContainerServiceMasterProfile
    from ._models import ContainerServiceNetworkProfile
    from ._models import ContainerServiceSshConfiguration
    from ._models import ContainerServiceSshPublicKey
    from ._models import ContainerServiceVMDiagnostics
    from ._models import CredentialResult
    from ._models import CredentialResults
    from ._models import ManagedCluster
    from ._models import ManagedClusterAADProfile
    from ._models import ManagedClusterAccessProfile
    from ._models import ManagedClusterAddonProfile
    from ._models import ManagedClusterAddonProfileIdentity
    from ._models import ManagedClusterAgentPoolProfile
    from ._models import ManagedClusterAgentPoolProfileProperties
    from ._models import ManagedClusterAPIServerAccessProfile
    from ._models import ManagedClusterIdentity
    from ._models import ManagedClusterLoadBalancerProfile
    from ._models import ManagedClusterLoadBalancerProfileManagedOutboundIPs
    from ._models import ManagedClusterLoadBalancerProfileOutboundIPPrefixes
    from ._models import ManagedClusterLoadBalancerProfileOutboundIPs
    from ._models import ManagedClusterPoolUpgradeProfile
    from ._models import ManagedClusterPoolUpgradeProfileUpgradesItem
    from ._models import ManagedClusterPropertiesAutoScalerProfile
    from ._models import ManagedClusterPropertiesIdentityProfileValue
    from ._models import ManagedClusterServicePrincipalProfile
    from ._models import ManagedClusterSKU
    from ._models import ManagedClusterUpgradeProfile
    from ._models import ManagedClusterWindowsProfile
    from ._models import OperationValue
    from ._models import Resource
    from ._models import ResourceReference
    from ._models import SubResource
    from ._models import TagsObject
    from ._models import UserAssignedIdentity
from ._paged_models import AgentPoolPaged
from ._paged_models import ManagedClusterPaged
from ._paged_models import OperationValuePaged
from ._container_service_client_enums import (
    ContainerServiceStorageProfileTypes,
    ContainerServiceVMSizeTypes,
    OSType,
    AgentPoolType,
    AgentPoolMode,
    ScaleSetPriority,
    ScaleSetEvictionPolicy,
    NetworkPlugin,
    NetworkPolicy,
    NetworkMode,
    OutboundType,
    LoadBalancerSku,
    ResourceIdentityType,
    ManagedClusterSKUName,
    ManagedClusterSKUTier,
)

__all__ = [
    'AgentPool',
    'AgentPoolAvailableVersions',
    'AgentPoolAvailableVersionsPropertiesAgentPoolVersionsItem',
    'AgentPoolUpgradeProfile',
    'AgentPoolUpgradeProfilePropertiesUpgradesItem',
    'AgentPoolUpgradeSettings',
    'ContainerServiceDiagnosticsProfile',
    'ContainerServiceLinuxProfile',
    'ContainerServiceMasterProfile',
    'ContainerServiceNetworkProfile',
    'ContainerServiceSshConfiguration',
    'ContainerServiceSshPublicKey',
    'ContainerServiceVMDiagnostics',
    'CredentialResult',
    'CredentialResults',
    'ManagedCluster',
    'ManagedClusterAADProfile',
    'ManagedClusterAccessProfile',
    'ManagedClusterAddonProfile',
    'ManagedClusterAddonProfileIdentity',
    'ManagedClusterAgentPoolProfile',
    'ManagedClusterAgentPoolProfileProperties',
    'ManagedClusterAPIServerAccessProfile',
    'ManagedClusterIdentity',
    'ManagedClusterLoadBalancerProfile',
    'ManagedClusterLoadBalancerProfileManagedOutboundIPs',
    'ManagedClusterLoadBalancerProfileOutboundIPPrefixes',
    'ManagedClusterLoadBalancerProfileOutboundIPs',
    'ManagedClusterPoolUpgradeProfile',
    'ManagedClusterPoolUpgradeProfileUpgradesItem',
    'ManagedClusterPropertiesAutoScalerProfile',
    'ManagedClusterPropertiesIdentityProfileValue',
    'ManagedClusterServicePrincipalProfile',
    'ManagedClusterSKU',
    'ManagedClusterUpgradeProfile',
    'ManagedClusterWindowsProfile',
    'OperationValue',
    'Resource',
    'ResourceReference',
    'SubResource',
    'TagsObject',
    'UserAssignedIdentity',
    'OperationValuePaged',
    'ManagedClusterPaged',
    'AgentPoolPaged',
    'ContainerServiceStorageProfileTypes',
    'ContainerServiceVMSizeTypes',
    'OSType',
    'AgentPoolType',
    'AgentPoolMode',
    'ScaleSetPriority',
    'ScaleSetEvictionPolicy',
    'NetworkPlugin',
    'NetworkPolicy',
    'NetworkMode',
    'OutboundType',
    'LoadBalancerSku',
    'ResourceIdentityType',
    'ManagedClusterSKUName',
    'ManagedClusterSKUTier',
]
