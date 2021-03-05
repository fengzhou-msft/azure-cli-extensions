# Azure CLI datashare Extension #
This is the extension for datashare

### How to use ###
Install this extension using the below CLI command
```
az extension add --name datashare
```

### Included Features ###
#### datashare account ####
##### Create #####
```
az datashare account create --location "West US 2" --tags tag1="Red" tag2="White" --name "Account1" \
    --resource-group "SampleResourceGroup" 

az datashare account wait --created --name "{myAccount}" --resource-group "{rg}"
```
##### Show #####
```
az datashare account show --name "Account1" --resource-group "SampleResourceGroup"
```
##### List #####
```
az datashare account list --resource-group "SampleResourceGroup"
```
##### Update #####
```
az datashare account update --name "Account1" --tags tag1="Red" tag2="White" --resource-group "SampleResourceGroup"
```
##### Delete #####
```
az datashare account delete --name "Account1" --resource-group "SampleResourceGroup"
```
#### datashare consumer invitation ####
##### List #####
```
az datashare consumer invitation list
```
##### Show #####
```
az datashare consumer invitation show --invitation-id "dfbbc788-19eb-4607-a5a1-c74181bfff03" --location "East US 2"
```
##### Reject #####
```
az datashare consumer invitation reject --invitation-id "dfbbc788-19eb-4607-a5a1-c74181bfff03" --location "East US 2"
```
#### datashare dataset ####
##### Create #####
```
az datashare dataset create --account-name "Account1" \
    --blob-data-set container-name="C1" file-path="file21" resource-group="SampleResourceGroup" storage-account-name="storage2" subscription-id="433a8dfd-e5d5-4e77-ad86-90acdc75eb1a" \
    --name "Dataset1" --resource-group "SampleResourceGroup" --share-name "Share1" 
```
##### Create #####
```
az datashare dataset create --account-name "Account1" \
    --kusto-cluster-data-set kusto-cluster-resource-id="/subscriptions/433a8dfd-e5d5-4e77-ad86-90acdc75eb1a/resourceGroups/SampleResourceGroup/providers/Microsoft.Kusto/clusters/Cluster1" \
    --name "Dataset1" --resource-group "SampleResourceGroup" --share-name "Share1" 
```
##### Create #####
```
az datashare dataset create --account-name "Account1" \
    --kusto-database-data-set kusto-database-resource-id="/subscriptions/433a8dfd-e5d5-4e77-ad86-90acdc75eb1a/resourceGroups/SampleResourceGroup/providers/Microsoft.Kusto/clusters/Cluster1/databases/Database1" \
    --name "Dataset1" --resource-group "SampleResourceGroup" --share-name "Share1" 
```
##### Create #####
```
az datashare dataset create --account-name "Account1" \
    --sqldb-table-data-set database-name="SqlDB1" schema-name="dbo" sql-server-resource-id="/subscriptions/433a8dfd-e5d5-4e77-ad86-90acdc75eb1a/resourceGroups/SampleResourceGroup/providers/Microsoft.Sql/servers/Server1" table-name="Table1" \
    --name "Dataset1" --resource-group "SampleResourceGroup" --share-name "Share1" 
```
##### Create #####
```
az datashare dataset create --account-name "Account1" \
    --sqldw-table-data-set data-warehouse-name="DataWarehouse1" schema-name="dbo" sql-server-resource-id="/subscriptions/433a8dfd-e5d5-4e77-ad86-90acdc75eb1a/resourceGroups/SampleResourceGroup/providers/Microsoft.Sql/servers/Server1" table-name="Table1" \
    --name "Dataset1" --resource-group "SampleResourceGroup" --share-name "Share1" 
```
##### Show #####
```
az datashare dataset show --account-name "Account1" --name "Dataset1" --resource-group "SampleResourceGroup" \
    --share-name "Share1" 
```
##### List #####
```
az datashare dataset list --account-name "Account1" --resource-group "SampleResourceGroup" --share-name "Share1"
```
##### Delete #####
```
az datashare dataset delete --account-name "Account1" --name "Dataset1" --resource-group "SampleResourceGroup" \
    --share-name "Share1" 
```
#### datashare consumer dataset-mapping ####
##### Create #####
```
az datashare consumer dataset-mapping create --account-name "Account1" \
    --blob-data-set-mapping container-name="C1" data-set-id="a08f184b-0567-4b11-ba22-a1199336d226" file-path="file21" resource-group="SampleResourceGroup" storage-account-name="storage2" subscription-id="433a8dfd-e5d5-4e77-ad86-90acdc75eb1a" \
    --name "DatasetMapping1" --resource-group "SampleResourceGroup" --share-subscription-name "ShareSubscription1" 
```
##### Create #####
```
az datashare consumer dataset-mapping create --account-name "Account1" \
    --sqldb-table-data-set-mapping database-name="Database1" data-set-id="a08f184b-0567-4b11-ba22-a1199336d226" schema-name="dbo" sql-server-resource-id="/subscriptions/433a8dfd-e5d5-4e77-ad86-90acdc75eb1a/resourceGroups/SampleResourceGroup/providers/Microsoft.Sql/servers/Server1" table-name="Table1" \
    --name "DatasetMapping1" --resource-group "SampleResourceGroup" --share-subscription-name "ShareSubscription1" 
```
##### Create #####
```
az datashare consumer dataset-mapping create --account-name "Account1" \
    --adls-gen2-file-data-set-mapping data-set-id="a08f184b-0567-4b11-ba22-a1199336d226" file-path="file21" file-system="fileSystem" output-type="Csv" resource-group="SampleResourceGroup" storage-account-name="storage2" subscription-id="433a8dfd-e5d5-4e77-ad86-90acdc75eb1a" \
    --name "DatasetMapping1" --resource-group "SampleResourceGroup" --share-subscription-name "ShareSubscription1" 
```
##### Create #####
```
az datashare consumer dataset-mapping create --account-name "Account1" \
    --sqldw-table-data-set-mapping data-set-id="a08f184b-0567-4b11-ba22-a1199336d226" data-warehouse-name="DataWarehouse1" schema-name="dbo" sql-server-resource-id="/subscriptions/433a8dfd-e5d5-4e77-ad86-90acdc75eb1a/resourceGroups/SampleResourceGroup/providers/Microsoft.Sql/servers/Server1" table-name="Table1" \
    --name "DatasetMapping1" --resource-group "SampleResourceGroup" --share-subscription-name "ShareSubscription1" 
```
##### List #####
```
az datashare consumer dataset-mapping list --account-name "Account1" --resource-group "SampleResourceGroup" \
    --share-subscription-name "ShareSubscription1" 
```
##### Show #####
```
az datashare consumer dataset-mapping show --account-name "Account1" --name "DatasetMapping1" \
    --resource-group "SampleResourceGroup" --share-subscription-name "ShareSubscription1" 
```
##### Delete #####
```
az datashare consumer dataset-mapping delete --account-name "Account1" --name "DatasetMapping1" \
    --resource-group "SampleResourceGroup" --share-subscription-name "ShareSubscription1" 
```
#### datashare invitation ####
##### Create #####
```
az datashare invitation create --account-name "Account1" --target-email "receiver@microsoft.com" --name "Invitation1" \
    --resource-group "SampleResourceGroup" --share-name "Share1" 
```
##### Show #####
```
az datashare invitation show --account-name "Account1" --name "Invitation1" --resource-group "SampleResourceGroup" \
    --share-name "Share1" 
```
##### List #####
```
az datashare invitation list --account-name "Account1" --resource-group "SampleResourceGroup" --share-name "Share1"
```
##### Delete #####
```
az datashare invitation delete --account-name "Account1" --name "Invitation1" --resource-group "SampleResourceGroup" \
    --share-name "Share1" 
```
#### datashare ####
##### Create #####
```
az datashare create --account-name "Account1" --resource-group "SampleResourceGroup" --description "share description" \
    --share-kind "CopyBased" --terms "Confidential" --name "Share1" 
```
##### Synchronization list #####
```
az datashare synchronization list --account-name "Account1" --resource-group "SampleResourceGroup" --name "Share1"
```
##### Show #####
```
az datashare show --account-name "Account1" --resource-group "SampleResourceGroup" --name "Share1"
```
##### List #####
```
az datashare list --account-name "Account1" --resource-group "SampleResourceGroup"
```
##### Synchronization list-detail #####
```
az datashare synchronization list-detail --account-name "Account1" --resource-group "SampleResourceGroup" \
    --name "Share1" --id "7d0536a6-3fa5-43de-b152-3d07c4f6b2bb" 
```
##### Delete #####
```
az datashare delete --account-name "Account1" --resource-group "SampleResourceGroup" --name "Share1"
```
#### datashare provider-share-subscription ####
##### List #####
```
az datashare provider-share-subscription list --account-name "Account1" --resource-group "SampleResourceGroup" \
    --share-name "Share1" 
```
##### Show #####
```
az datashare provider-share-subscription show --account-name "Account1" \
    --provider-share-subscription-id "4256e2cf-0f82-4865-961b-12f83333f487" --resource-group "SampleResourceGroup" \
    --share-name "Share1" 
```
##### Reinstate #####
```
az datashare provider-share-subscription reinstate --account-name "Account1" \
    --provider-share-subscription-id "4256e2cf-0f82-4865-961b-12f83333f487" --resource-group "SampleResourceGroup" \
    --share-name "Share1" 
```
##### Revoke #####
```
az datashare provider-share-subscription revoke --account-name "Account1" \
    --provider-share-subscription-id "4256e2cf-0f82-4865-961b-12f83333f487" --resource-group "SampleResourceGroup" \
    --share-name "Share1" 
```
#### datashare consumer share-subscription ####
##### Create #####
```
az datashare consumer share-subscription create --account-name "Account1" --resource-group "SampleResourceGroup" \
    --invitation-id "12345678-1234-1234-12345678abd" --source-share-location "eastus2" --name "ShareSubscription1" 
```
##### Synchronization list #####
```
az datashare consumer share-subscription synchronization list --account-name "Account1" \
    --resource-group "SampleResourceGroup" --name "ShareSub1" 
```
##### Show #####
```
az datashare consumer share-subscription show --account-name "Account1" --resource-group "SampleResourceGroup" \
    --name "ShareSubscription1" 
```
##### List #####
```
az datashare consumer share-subscription list --account-name "Account1" --resource-group "SampleResourceGroup"
```
##### List-source-dataset #####
```
az datashare consumer share-subscription list-source-dataset --account-name "Account1" \
    --resource-group "SampleResourceGroup" --name "Share1" 
```
##### List-source-share-synchronization-setting #####
```
az datashare consumer share-subscription list-source-share-synchronization-setting --account-name "Account1" \
    --resource-group "SampleResourceGroup" --name "ShareSub1" 
```
##### Synchronization cancel #####
```
az datashare consumer share-subscription synchronization cancel --account-name "Account1" \
    --resource-group "SampleResourceGroup" --name "ShareSubscription1" --id "7d0536a6-3fa5-43de-b152-3d07c4f6b2bb" 
```
##### Synchronization list-detail #####
```
az datashare consumer share-subscription synchronization list-detail --account-name "Account1" \
    --resource-group "SampleResourceGroup" --name "ShareSub1" --id "7d0536a6-3fa5-43de-b152-3d07c4f6b2bb" 
```
##### Synchronization start #####
```
az datashare consumer share-subscription synchronization start --account-name "Account1" \
    --resource-group "SampleResourceGroup" --name "ShareSubscription1" --mode "Incremental" 
```
##### Delete #####
```
az datashare consumer share-subscription delete --account-name "Account1" --resource-group "SampleResourceGroup" \
    --name "ShareSubscription1" 
```
#### datashare synchronization-setting ####
##### Create #####
```
az datashare synchronization-setting create --account-name "Account1" --resource-group "SampleResourceGroup" \
    --share-name "Share1" \
    --scheduled-synchronization-setting recurrence-interval="Day" synchronization-time="2018-11-14T04:47:52.9614956Z" \
    --name "Dataset1" 
```
##### Show #####
```
az datashare synchronization-setting show --account-name "Account1" --resource-group "SampleResourceGroup" \
    --share-name "Share1" --name "SynchronizationSetting1" 
```
##### List #####
```
az datashare synchronization-setting list --account-name "Account1" --resource-group "SampleResourceGroup" \
    --share-name "Share1" 
```
##### Delete #####
```
az datashare synchronization-setting delete --account-name "Account1" --resource-group "SampleResourceGroup" \
    --share-name "Share1" --name "SynchronizationSetting1" 
```
#### datashare consumer trigger ####
##### Create #####
```
az datashare consumer trigger create --account-name "Account1" --resource-group "SampleResourceGroup" \
    --share-subscription-name "ShareSubscription1" \
    --scheduled-trigger recurrence-interval="Day" synchronization-mode="Incremental" synchronization-time="2018-11-14T04:47:52.9614956Z" \
    --name "Trigger1" 
```
##### Show #####
```
az datashare consumer trigger show --account-name "Account1" --resource-group "SampleResourceGroup" \
    --share-subscription-name "ShareSubscription1" --name "Trigger1" 
```
##### List #####
```
az datashare consumer trigger list --account-name "Account1" --resource-group "SampleResourceGroup" \
    --share-subscription-name "ShareSubscription1" 
```
##### Delete #####
```
az datashare consumer trigger delete --account-name "Account1" --resource-group "SampleResourceGroup" \
    --share-subscription-name "ShareSubscription1" --name "Trigger1" 
```