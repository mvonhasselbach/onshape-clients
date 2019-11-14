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


class BTOrFilter(object):
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
        'operand1': 'object',
        'operand2': 'object'
    }

    attribute_map = {
        'operand1': 'operand1',
        'operand2': 'operand2'
    }

    def __init__(self, operand1=None, operand2=None):  # noqa: E501
        """BTOrFilter - a model defined in OpenAPI"""  # noqa: E501

        self._operand1 = None
        self._operand2 = None
        self.discriminator = None

        if operand1 is not None:
            self.operand1 = operand1
        if operand2 is not None:
            self.operand2 = operand2

    @property
    def operand1(self):
        """Gets the operand1 of this BTOrFilter.  # noqa: E501


        :return: The operand1 of this BTOrFilter.  # noqa: E501
        :rtype: object
        """
        return self._operand1

    @operand1.setter
    def operand1(self, operand1):
        """Sets the operand1 of this BTOrFilter.


        :param operand1: The operand1 of this BTOrFilter.  # noqa: E501
        :type: object
        """

        self._operand1 = operand1

    @property
    def operand2(self):
        """Gets the operand2 of this BTOrFilter.  # noqa: E501


        :return: The operand2 of this BTOrFilter.  # noqa: E501
        :rtype: object
        """
        return self._operand2

    @operand2.setter
    def operand2(self, operand2):
        """Sets the operand2 of this BTOrFilter.


        :param operand2: The operand2 of this BTOrFilter.  # noqa: E501
        :type: object
        """

        self._operand2 = operand2

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
        if not isinstance(other, BTOrFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
