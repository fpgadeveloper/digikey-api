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


class AcceptOrderDetailErrorsPage(object):
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
        'errors': 'list[AcceptOrderDetailErrorResult]',
        'error_count': 'int'
    }

    attribute_map = {
        'errors': 'errors',
        'error_count': 'errorCount'
    }

    def __init__(self, errors=None, error_count=None):  # noqa: E501
        """AcceptOrderDetailErrorsPage - a model defined in Swagger"""  # noqa: E501

        self._errors = None
        self._error_count = None
        self.discriminator = None

        if errors is not None:
            self.errors = errors
        if error_count is not None:
            self.error_count = error_count

    @property
    def errors(self):
        """Gets the errors of this AcceptOrderDetailErrorsPage.  # noqa: E501


        :return: The errors of this AcceptOrderDetailErrorsPage.  # noqa: E501
        :rtype: list[AcceptOrderDetailErrorResult]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this AcceptOrderDetailErrorsPage.


        :param errors: The errors of this AcceptOrderDetailErrorsPage.  # noqa: E501
        :type: list[AcceptOrderDetailErrorResult]
        """

        self._errors = errors

    @property
    def error_count(self):
        """Gets the error_count of this AcceptOrderDetailErrorsPage.  # noqa: E501


        :return: The error_count of this AcceptOrderDetailErrorsPage.  # noqa: E501
        :rtype: int
        """
        return self._error_count

    @error_count.setter
    def error_count(self, error_count):
        """Sets the error_count of this AcceptOrderDetailErrorsPage.


        :param error_count: The error_count of this AcceptOrderDetailErrorsPage.  # noqa: E501
        :type: int
        """

        self._error_count = error_count

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
        if issubclass(AcceptOrderDetailErrorsPage, dict):
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
        if not isinstance(other, AcceptOrderDetailErrorsPage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
