# Azure CLI Module Creation Report

### account alias create

create a account alias.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|account alias|Alias|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create|Create|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--alias-name**|string|Alias Name|alias_name|aliasName|
|**--display-name**|string|The friendly name of the subscription.|properties_display_name|displayName|
|**--workload**|choice|The workload type of the subscription. It can be either Production or DevTest.|properties_workload|workload|
|**--billing-scope**|string|Determines whether subscription is fieldLed, partnerLed or LegacyEA|properties_billing_scope|billingScope|
|**--subscription-id**|string|This parameter can be used to create alias for existing subscription Id|properties_subscription_id|subscriptionId|

### account alias delete

delete a account alias.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|account alias|Alias|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|Delete|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--alias-name**|string|Alias Name|alias_name|aliasName|

### account alias list

list a account alias.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|account alias|Alias|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list|List|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### account alias show

show a account alias.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|account alias|Alias|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|show|Get|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--alias-name**|string|Alias Name|alias_name|aliasName|

### account subscription cancel

cancel a account subscription.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|account subscription|Subscriptions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel|Cancel|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscription-id**|string|Subscription Id.|subscription_id|subscriptionId|

### account subscription enable

enable a account subscription.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|account subscription|Subscriptions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|enable|Enable|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscription-id**|string|Subscription Id.|subscription_id|subscriptionId|

### account subscription list

list a account subscription.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|account subscription|Subscriptions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list|List|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### account subscription list-location

list-location a account subscription.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|account subscription|Subscriptions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-location|ListLocations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscription-id**|string|The ID of the target subscription.|subscription_id|subscriptionId|

### account subscription rename

rename a account subscription.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|account subscription|Subscriptions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|rename|Rename|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscription-id**|string|Subscription Id.|subscription_id|subscriptionId|
|**--subscription-name**|string|New subscription name|subscription_name|subscriptionName|

### account subscription show

show a account subscription.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|account subscription|Subscriptions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|show|Get|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscription-id**|string|The ID of the target subscription.|subscription_id|subscriptionId|

### account tenant list

list a account tenant.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|account tenant|Tenants|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list|List|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
