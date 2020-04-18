# Azure CLI Module Creation Report

### databricks workspace create

create a databricks workspace.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--location**|string|The geo-location where the resource lives|location|
|**--managed-resource-group-id**|string|The managed resource group Id.|managed_resource_group_id|
|**--tags**|dictionary|Resource tags.|tags|
|**--sku**|object|The SKU of the resource.|sku|
|**--parameters**|object|The workspace's custom parameters.|parameters|
|**--ui-definition-uri**|string|The blob URI where the UI definition file is located.|ui_definition_uri|
|**--authorizations**|array|The workspace provider authorizations.|authorizations|
|**--created-by**|object|Indicates the Object ID, PUID and Application ID of entity that created the workspace.|created_by|
|**--updated-by**|object|Indicates the Object ID, PUID and Application ID of entity that last updated the workspace.|updated_by|
|**--storage-account-identity**|object|The details of Managed Identity of Storage Account|storage_account_identity|
### databricks workspace delete

delete a databricks workspace.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
### databricks workspace list

list a databricks workspace.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|
### databricks workspace show

show a databricks workspace.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
### databricks workspace update

update a databricks workspace.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|
|**--workspace-name**|string|The name of the workspace.|workspace_name|
|**--tags**|dictionary|Resource tags.|tags|