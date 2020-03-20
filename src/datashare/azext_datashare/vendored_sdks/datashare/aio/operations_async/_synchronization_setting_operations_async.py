# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.polling import AsyncNoPolling, AsyncPollingMethod, async_poller
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class SynchronizationSettingOperations:
    """SynchronizationSettingOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~data_share_management_client.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def get(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        synchronization_setting_name: str,
        **kwargs
    ) -> "models.SynchronizationSetting":
        """Get a synchronizationSetting in a share.

        Get synchronizationSetting in a share.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param account_name: The name of the share account.
        :type account_name: str
        :param share_name: The name of the share.
        :type share_name: str
        :param synchronization_setting_name: The name of the synchronizationSetting.
        :type synchronization_setting_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SynchronizationSetting or the result of cls(response)
        :rtype: ~data_share_management_client.models.SynchronizationSetting
        :raises: ~data_share_management_client.models.DataShareErrorException:
        """
        cls: ClsType["models.SynchronizationSetting"] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-11-01"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'shareName': self._serialize.url("share_name", share_name, 'str'),
            'synchronizationSettingName': self._serialize.url("synchronization_setting_name", synchronization_setting_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.DataShareErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('SynchronizationSetting', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/synchronizationSettings/{synchronizationSettingName}'}

    async def create(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        synchronization_setting_name: str,
        kind: Union[str, "models.Kind"],
        **kwargs
    ) -> "models.SynchronizationSetting":
        """Create or update a synchronizationSetting.

        Adds a new synchronization setting to an existing share.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param account_name: The name of the share account.
        :type account_name: str
        :param share_name: The name of the share.
        :type share_name: str
        :param synchronization_setting_name: The name of the synchronizationSetting.
        :type synchronization_setting_name: str
        :param kind: Kind of data set.
        :type kind: str or ~data_share_management_client.models.Kind
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SynchronizationSetting or SynchronizationSetting or the result of cls(response)
        :rtype: ~data_share_management_client.models.SynchronizationSetting or ~data_share_management_client.models.SynchronizationSetting
        :raises: ~data_share_management_client.models.DataShareErrorException:
        """
        cls: ClsType["models.SynchronizationSetting"] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})

        synchronization_setting = models.SynchronizationSetting(kind=kind)
        api_version = "2019-11-01"

        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'shareName': self._serialize.url("share_name", share_name, 'str'),
            'synchronizationSettingName': self._serialize.url("synchronization_setting_name", synchronization_setting_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(synchronization_setting, 'SynchronizationSetting')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.DataShareErrorException.from_response(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('SynchronizationSetting', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('SynchronizationSetting', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    create.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/synchronizationSettings/{synchronizationSettingName}'}

    async def _delete_initial(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        synchronization_setting_name: str,
        **kwargs
    ) -> "models.OperationResponse":
        cls: ClsType["models.OperationResponse"] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-11-01"

        # Construct URL
        url = self._delete_initial.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'shareName': self._serialize.url("share_name", share_name, 'str'),
            'synchronizationSettingName': self._serialize.url("synchronization_setting_name", synchronization_setting_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.DataShareErrorException.from_response(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('OperationResponse', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    _delete_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/synchronizationSettings/{synchronizationSettingName}'}

    async def delete(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        synchronization_setting_name: str,
        **kwargs
    ) -> "models.OperationResponse":
        """Delete a synchronizationSetting in a share.

        Delete synchronizationSetting in a share.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param account_name: The name of the share account.
        :type account_name: str
        :param share_name: The name of the share.
        :type share_name: str
        :param synchronization_setting_name: The name of the synchronizationSetting.
        :type synchronization_setting_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :return: An instance of LROPoller that returns OperationResponse
        :rtype: ~azure.core.polling.LROPoller[~data_share_management_client.models.OperationResponse]

        :raises ~data_share_management_client.models.DataShareErrorException:
        """
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop('polling', True)
        cls: ClsType["models.OperationResponse"] = kwargs.pop('cls', None )
        raw_result = await self._delete_initial(
            resource_group_name=resource_group_name,
            account_name=account_name,
            share_name=share_name,
            synchronization_setting_name=synchronization_setting_name,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('OperationResponse', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = AsyncARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/synchronizationSettings/{synchronizationSettingName}'}

    def list_by_share(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        skip_token: Optional[str] = None,
        **kwargs
    ) -> "models.SynchronizationSettingList":
        """List synchronizationSettings in a share.

        List synchronizationSettings in a share.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param account_name: The name of the share account.
        :type account_name: str
        :param share_name: The name of the share.
        :type share_name: str
        :param skip_token: Continuation token.
        :type skip_token: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SynchronizationSettingList or the result of cls(response)
        :rtype: ~data_share_management_client.models.SynchronizationSettingList
        :raises: ~data_share_management_client.models.DataShareErrorException:
        """
        cls: ClsType["models.SynchronizationSettingList"] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-11-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_share.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'accountName': self._serialize.url("account_name", account_name, 'str'),
                    'shareName': self._serialize.url("share_name", share_name, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters: Dict[str, Any] = {}
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
            if skip_token is not None:
                query_parameters['$skipToken'] = self._serialize.query("skip_token", skip_token, 'str')

            # Construct headers
            header_parameters: Dict[str, Any] = {}
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('SynchronizationSettingList', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise models.DataShareErrorException.from_response(response, self._deserialize)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_share.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/synchronizationSettings'}
