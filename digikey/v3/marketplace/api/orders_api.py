# coding: utf-8

"""
    Orders

    API operations for managing orders as well as refunds and incidents as they relate to the order  # noqa: E501

    OpenAPI spec version: suppliers-v1
    Contact: MarketplaceAPISupport@digikey.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from digikey.v3.marketplace.api_client import ApiClient


class OrdersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def update_supplier_invoice_number(self, order_id, **kwargs):  # noqa: E501
        """Update Supplier Invoice Number  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_supplier_invoice_number(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id:  (required)
        :param str supplier_invoice_number: 
        :return: Order
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_supplier_invoice_number_with_http_info(order_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_supplier_invoice_number_with_http_info(order_id, **kwargs)  # noqa: E501
            return data

    def update_supplier_invoice_number_with_http_info(self, order_id, **kwargs):  # noqa: E501
        """Update Supplier Invoice Number  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_supplier_invoice_number_with_http_info(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id:  (required)
        :param str supplier_invoice_number: 
        :return: Order
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_id', 'supplier_invoice_number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_supplier_invoice_number" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'order_id' is set
        if ('order_id' not in params or
                params['order_id'] is None):
            raise ValueError("Missing the required parameter `order_id` when calling `update_supplier_invoice_number`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'order_id' in params:
            path_params['orderId'] = params['order_id']  # noqa: E501

        query_params = []
        if 'supplier_invoice_number' in params:
            query_params.append(('supplierInvoiceNumber', params['supplier_invoice_number']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeySecurity', 'oauth2AccessCodeSecurity']  # noqa: E501

        return self.api_client.call_api(
            '/orders/{orderId}/supplierInvoiceNumber', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Order',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
