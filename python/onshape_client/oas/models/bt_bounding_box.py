# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    The version of the OpenAPI document: 1.106
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BTBoundingBox(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'valid': 'bool',
        'min_corner': 'BTVector3d',
        'max_corner': 'BTVector3d'
    }

    attribute_map = {
        'valid': 'valid',
        'min_corner': 'minCorner',
        'max_corner': 'maxCorner'
    }

    def __init__(self, valid=None, min_corner=None, max_corner=None):  # noqa: E501
        """BTBoundingBox - a model defined in OpenAPI"""  # noqa: E501

        self._valid = None
        self._min_corner = None
        self._max_corner = None
        self.discriminator = None

        if valid is not None:
            self.valid = valid
        if min_corner is not None:
            self.min_corner = min_corner
        if max_corner is not None:
            self.max_corner = max_corner

    @property
    def valid(self):
        """Gets the valid of this BTBoundingBox.  # noqa: E501


        :return: The valid of this BTBoundingBox.  # noqa: E501
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """Sets the valid of this BTBoundingBox.


        :param valid: The valid of this BTBoundingBox.  # noqa: E501
        :type: bool
        """

        self._valid = valid

    @property
    def min_corner(self):
        """Gets the min_corner of this BTBoundingBox.  # noqa: E501


        :return: The min_corner of this BTBoundingBox.  # noqa: E501
        :rtype: BTVector3d
        """
        return self._min_corner

    @min_corner.setter
    def min_corner(self, min_corner):
        """Sets the min_corner of this BTBoundingBox.


        :param min_corner: The min_corner of this BTBoundingBox.  # noqa: E501
        :type: BTVector3d
        """

        self._min_corner = min_corner

    @property
    def max_corner(self):
        """Gets the max_corner of this BTBoundingBox.  # noqa: E501


        :return: The max_corner of this BTBoundingBox.  # noqa: E501
        :rtype: BTVector3d
        """
        return self._max_corner

    @max_corner.setter
    def max_corner(self, max_corner):
        """Sets the max_corner of this BTBoundingBox.


        :param max_corner: The max_corner of this BTBoundingBox.  # noqa: E501
        :type: BTVector3d
        """

        self._max_corner = max_corner

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BTBoundingBox):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
