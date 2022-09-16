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


class UpdateOrderAdditionalFieldsCommandBody(object):
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
        'additional_fields': 'list[AdditionalField]'
    }

    attribute_map = {
        'additional_fields': 'additionalFields'
    }

    def __init__(self, additional_fields=None):  # noqa: E501
        """UpdateOrderAdditionalFieldsCommandBody - a model defined in Swagger"""  # noqa: E501

        self._additional_fields = None
        self.discriminator = None

        self.additional_fields = additional_fields

    @property
    def additional_fields(self):
        """Gets the additional_fields of this UpdateOrderAdditionalFieldsCommandBody.  # noqa: E501


        :return: The additional_fields of this UpdateOrderAdditionalFieldsCommandBody.  # noqa: E501
        :rtype: list[AdditionalField]
        """
        return self._additional_fields

    @additional_fields.setter
    def additional_fields(self, additional_fields):
        """Sets the additional_fields of this UpdateOrderAdditionalFieldsCommandBody.


        :param additional_fields: The additional_fields of this UpdateOrderAdditionalFieldsCommandBody.  # noqa: E501
        :type: list[AdditionalField]
        """
        if additional_fields is None:
            raise ValueError("Invalid value for `additional_fields`, must not be `None`")  # noqa: E501

        self._additional_fields = additional_fields

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
        if issubclass(UpdateOrderAdditionalFieldsCommandBody, dict):
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
        if not isinstance(other, UpdateOrderAdditionalFieldsCommandBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other