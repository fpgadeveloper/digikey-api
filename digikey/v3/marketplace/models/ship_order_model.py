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


class ShipOrderModel(object):
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
        'shipping_tracking': 'list[ShippingTrackingInformationModel]'
    }

    attribute_map = {
        'shipping_tracking': 'shippingTracking'
    }

    def __init__(self, shipping_tracking=None):  # noqa: E501
        """ShipOrderModel - a model defined in Swagger"""  # noqa: E501

        self._shipping_tracking = None
        self.discriminator = None

        if shipping_tracking is not None:
            self.shipping_tracking = shipping_tracking

    @property
    def shipping_tracking(self):
        """Gets the shipping_tracking of this ShipOrderModel.  # noqa: E501


        :return: The shipping_tracking of this ShipOrderModel.  # noqa: E501
        :rtype: list[ShippingTrackingInformationModel]
        """
        return self._shipping_tracking

    @shipping_tracking.setter
    def shipping_tracking(self, shipping_tracking):
        """Sets the shipping_tracking of this ShipOrderModel.


        :param shipping_tracking: The shipping_tracking of this ShipOrderModel.  # noqa: E501
        :type: list[ShippingTrackingInformationModel]
        """

        self._shipping_tracking = shipping_tracking

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
        if issubclass(ShipOrderModel, dict):
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
        if not isinstance(other, ShipOrderModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
