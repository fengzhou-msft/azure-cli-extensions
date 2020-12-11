def step_organization_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az confluent organization create '
             '--location westus2 '
             '--offer-detail id="confluent-cloud-azure-prod" plan-id="confluent-cloud-azure-payg-prod" plan-name="Confluent Cloud - Pay as you go" publisher-id="confluentinc" term-unit="P1M" '
             '--user-detail email-address="feng.zhou@microsoft.com" first-name="feng" last-name="zhou" '
             '--tags Environment="Dev" '
             '--name "{myOrganization}" '
             '--resource-group "{rg}"',
             checks=checks)
    test.cmd('az confluent organization wait --created '
             '--name "{myOrganization}" '
             '--resource-group "{rg}"',
             checks=[])
