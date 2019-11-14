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


class BTFSValueNumber(object):
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
        'value_object': 'float',
        'value': 'float'
    }

    attribute_map = {
        'value_object': 'valueObject',
        'value': 'value'
    }

    def __init__(self, value_object=None, value=None):  # noqa: E501
        """BTFSValueNumber - a model defined in OpenAPI"""  # noqa: E501

        self._value_object = None
        self._value = None
        self.discriminator = None

        if value_object is not None:
            self.value_object = value_object
        if value is not None:
            self.value = value

    @property
    def value_object(self):
        """Gets the value_object of this BTFSValueNumber.  # noqa: E501


        :return: The value_object of this BTFSValueNumber.  # noqa: E501
        :rtype: float
        """
        return self._value_object

    @value_object.setter
    def value_object(self, value_object):
        """Sets the value_object of this BTFSValueNumber.


        :param value_object: The value_object of this BTFSValueNumber.  # noqa: E501
        :type: float
        """

        self._value_object = value_object

    @property
    def value(self):
        """Gets the value of this BTFSValueNumber.  # noqa: E501


        :return: The value of this BTFSValueNumber.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this BTFSValueNumber.


        :param value: The value of this BTFSValueNumber.  # noqa: E501
        :type: float
        """

        self._value = value

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
        if not isinstance(other, BTFSValueNumber):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
