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


class BTMSketchPoint(object):
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
        'x': 'float',
        'y': 'float',
        'is_user_point': 'bool'
    }

    attribute_map = {
        'x': 'x',
        'y': 'y',
        'is_user_point': 'isUserPoint'
    }

    def __init__(self, x=None, y=None, is_user_point=None):  # noqa: E501
        """BTMSketchPoint - a model defined in OpenAPI"""  # noqa: E501

        self._x = None
        self._y = None
        self._is_user_point = None
        self.discriminator = None

        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if is_user_point is not None:
            self.is_user_point = is_user_point

    @property
    def x(self):
        """Gets the x of this BTMSketchPoint.  # noqa: E501


        :return: The x of this BTMSketchPoint.  # noqa: E501
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this BTMSketchPoint.


        :param x: The x of this BTMSketchPoint.  # noqa: E501
        :type: float
        """

        self._x = x

    @property
    def y(self):
        """Gets the y of this BTMSketchPoint.  # noqa: E501


        :return: The y of this BTMSketchPoint.  # noqa: E501
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this BTMSketchPoint.


        :param y: The y of this BTMSketchPoint.  # noqa: E501
        :type: float
        """

        self._y = y

    @property
    def is_user_point(self):
        """Gets the is_user_point of this BTMSketchPoint.  # noqa: E501


        :return: The is_user_point of this BTMSketchPoint.  # noqa: E501
        :rtype: bool
        """
        return self._is_user_point

    @is_user_point.setter
    def is_user_point(self, is_user_point):
        """Sets the is_user_point of this BTMSketchPoint.


        :param is_user_point: The is_user_point of this BTMSketchPoint.  # noqa: E501
        :type: bool
        """

        self._is_user_point = is_user_point

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
        if not isinstance(other, BTMSketchPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
