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

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class DataSetMappingOperations:
    """DataSetMappingOperations async operations.

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
        share_subscription_name: str,
        data_set_mapping_name: str,
        **kwargs
    ) -> "models.DataSetMapping":
        """Get a DataSetMapping in a shareSubscription.

        Get DataSetMapping in a shareSubscription.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param account_name: The name of the share account.
        :type account_name: str
        :param share_subscription_name: The name of the shareSubscription.
        :type share_subscription_name: str
        :param data_set_mapping_name: The name of the dataSetMapping.
        :type data_set_mapping_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DataSetMapping or the result of cls(response)
        :rtype: ~data_share_management_client.models.DataSetMapping
        :raises: ~data_share_management_client.models.DataShareErrorException:
        """
        cls: ClsType["models.DataSetMapping"] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-11-01"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'shareSubscriptionName': self._serialize.url("share_subscription_name", share_subscription_name, 'str'),
            'dataSetMappingName': self._serialize.url("data_set_mapping_name", data_set_mapping_name, 'str'),
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

        deserialized = self._deserialize('DataSetMapping', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/dataSetMappings/{dataSetMappingName}'}

    async def create(
        self,
        resource_group_name: str,
        account_name: str,
        share_subscription_name: str,
        data_set_mapping_name: str,
        kind: Union[str, "models.Kind"],
        **kwargs
    ) -> "models.DataSetMapping":
        """Create a DataSetMapping.

        Maps a source data set in the source share to a sink data set in the share subscription.
        Enables copying the data set from source to destination.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param account_name: The name of the share account.
        :type account_name: str
        :param share_subscription_name: The name of the shareSubscription.
        :type share_subscription_name: str
        :param data_set_mapping_name: The name of the dataSetMapping.
        :type data_set_mapping_name: str
        :param kind: Kind of data set.
        :type kind: str or ~data_share_management_client.models.Kind
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DataSetMapping or DataSetMapping or the result of cls(response)
        :rtype: ~data_share_management_client.models.DataSetMapping or ~data_share_management_client.models.DataSetMapping
        :raises: ~data_share_management_client.models.DataShareErrorException:
        """
        cls: ClsType["models.DataSetMapping"] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})

        data_set_mapping = models.DataSetMapping(kind=kind)
        api_version = "2019-11-01"

        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'shareSubscriptionName': self._serialize.url("share_subscription_name", share_subscription_name, 'str'),
            'dataSetMappingName': self._serialize.url("data_set_mapping_name", data_set_mapping_name, 'str'),
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
        body_content = self._serialize.body(data_set_mapping, 'DataSetMapping')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.DataShareErrorException.from_response(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('DataSetMapping', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('DataSetMapping', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    create.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/dataSetMappings/{dataSetMappingName}'}

    async def delete(
        self,
        resource_group_name: str,
        account_name: str,
        share_subscription_name: str,
        data_set_mapping_name: str,
        **kwargs
    ) -> None:
        """Delete a DataSetMapping in a shareSubscription.

        Delete DataSetMapping in a shareSubscription.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param account_name: The name of the share account.
        :type account_name: str
        :param share_subscription_name: The name of the shareSubscription.
        :type share_subscription_name: str
        :param data_set_mapping_name: The name of the dataSetMapping.
        :type data_set_mapping_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~data_share_management_client.models.DataShareErrorException:
        """
        cls: ClsType[None] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-11-01"

        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'shareSubscriptionName': self._serialize.url("share_subscription_name", share_subscription_name, 'str'),
            'dataSetMappingName': self._serialize.url("data_set_mapping_name", data_set_mapping_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters: Dict[str, Any] = {}

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.DataShareErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/dataSetMappings/{dataSetMappingName}'}

    def list_by_share_subscription(
        self,
        resource_group_name: str,
        account_name: str,
        share_subscription_name: str,
        skip_token: Optional[str] = None,
        **kwargs
    ) -> "models.DataSetMappingList":
        """List DataSetMappings in a share subscription.

        List DataSetMappings in a share subscription.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param account_name: The name of the share account.
        :type account_name: str
        :param share_subscription_name: The name of the shareSubscription.
        :type share_subscription_name: str
        :param skip_token: Continuation token.
        :type skip_token: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DataSetMappingList or the result of cls(response)
        :rtype: ~data_share_management_client.models.DataSetMappingList
        :raises: ~data_share_management_client.models.DataShareErrorException:
        """
        cls: ClsType["models.DataSetMappingList"] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-11-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_share_subscription.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'accountName': self._serialize.url("account_name", account_name, 'str'),
                    'shareSubscriptionName': self._serialize.url("share_subscription_name", share_subscription_name, 'str'),
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
            deserialized = self._deserialize('DataSetMappingList', pipeline_response)
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
    list_by_share_subscription.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/dataSetMappings'}
