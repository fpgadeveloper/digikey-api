# coding: utf-8

"""
    Orders

    API operations for managing orders as well as refunds and incidents as they relate to the order  # noqa: E501

    OpenAPI spec version: suppliers-v1
    Contact: MarketplaceAPISupport@digikey.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Customer(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'customer_id': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'customer_email': 'str',
        'billing_address': 'ContactInfo',
        'shipping_address': 'ContactInfo'
    }

    attribute_map = {
        'customer_id': 'customerId',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'customer_email': 'customerEmail',
        'billing_address': 'billingAddress',
        'shipping_address': 'shippingAddress'
    }

    def __init__(self, customer_id=None, first_name=None, last_name=None, customer_email=None, billing_address=None, shipping_address=None):  # noqa: E501
        """Customer - a model defined in Swagger"""  # noqa: E501

        self._customer_id = None
        self._first_name = None
        self._last_name = None
        self._customer_email = None
        self._billing_address = None
        self._shipping_address = None
        self.discriminator = None

        if customer_id is not None:
            self.customer_id = customer_id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if customer_email is not None:
            self.customer_email = customer_email
        if billing_address is not None:
            self.billing_address = billing_address
        if shipping_address is not None:
            self.shipping_address = shipping_address

    @property
    def customer_id(self):
        """Gets the customer_id of this Customer.  # noqa: E501


        :return: The customer_id of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this Customer.


        :param customer_id: The customer_id of this Customer.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def first_name(self):
        """Gets the first_name of this Customer.  # noqa: E501


        :return: The first_name of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Customer.


        :param first_name: The first_name of this Customer.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this Customer.  # noqa: E501


        :return: The last_name of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Customer.


        :param last_name: The last_name of this Customer.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def customer_email(self):
        """Gets the customer_email of this Customer.  # noqa: E501


        :return: The customer_email of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._customer_email

    @customer_email.setter
    def customer_email(self, customer_email):
        """Sets the customer_email of this Customer.


        :param customer_email: The customer_email of this Customer.  # noqa: E501
        :type: str
        """

        self._customer_email = customer_email

    @property
    def billing_address(self):
        """Gets the billing_address of this Customer.  # noqa: E501


        :return: The billing_address of this Customer.  # noqa: E501
        :rtype: ContactInfo
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this Customer.


        :param billing_address: The billing_address of this Customer.  # noqa: E501
        :type: ContactInfo
        """

        self._billing_address = billing_address

    @property
    def shipping_address(self):
        """Gets the shipping_address of this Customer.  # noqa: E501


        :return: The shipping_address of this Customer.  # noqa: E501
        :rtype: ContactInfo
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """Sets the shipping_address of this Customer.


        :param shipping_address: The shipping_address of this Customer.  # noqa: E501
        :type: ContactInfo
        """

        self._shipping_address = shipping_address

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Customer, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Customer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
