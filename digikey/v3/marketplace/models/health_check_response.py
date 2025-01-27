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


class HealthCheckResponse(object):
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
        'healthy': 'bool',
        'timestamp_utc': 'datetime'
    }

    attribute_map = {
        'healthy': 'healthy',
        'timestamp_utc': 'timestampUtc'
    }

    def __init__(self, healthy=None, timestamp_utc=None):  # noqa: E501
        """HealthCheckResponse - a model defined in Swagger"""  # noqa: E501

        self._healthy = None
        self._timestamp_utc = None
        self.discriminator = None

        if healthy is not None:
            self.healthy = healthy
        if timestamp_utc is not None:
            self.timestamp_utc = timestamp_utc

    @property
    def healthy(self):
        """Gets the healthy of this HealthCheckResponse.  # noqa: E501


        :return: The healthy of this HealthCheckResponse.  # noqa: E501
        :rtype: bool
        """
        return self._healthy

    @healthy.setter
    def healthy(self, healthy):
        """Sets the healthy of this HealthCheckResponse.


        :param healthy: The healthy of this HealthCheckResponse.  # noqa: E501
        :type: bool
        """

        self._healthy = healthy

    @property
    def timestamp_utc(self):
        """Gets the timestamp_utc of this HealthCheckResponse.  # noqa: E501


        :return: The timestamp_utc of this HealthCheckResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp_utc

    @timestamp_utc.setter
    def timestamp_utc(self, timestamp_utc):
        """Sets the timestamp_utc of this HealthCheckResponse.


        :param timestamp_utc: The timestamp_utc of this HealthCheckResponse.  # noqa: E501
        :type: datetime
        """

        self._timestamp_utc = timestamp_utc

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
        if issubclass(HealthCheckResponse, dict):
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
        if not isinstance(other, HealthCheckResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
