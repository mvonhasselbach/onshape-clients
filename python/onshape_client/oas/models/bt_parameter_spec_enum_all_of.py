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


class BTParameterSpecEnumAllOf(object):
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
        'enum_name': 'str',
        'option_names': 'list[str]',
        'options': 'list[str]',
        'namespace': 'str'
    }

    attribute_map = {
        'enum_name': 'enumName',
        'option_names': 'optionNames',
        'options': 'options',
        'namespace': 'namespace'
    }

    def __init__(self, enum_name=None, option_names=None, options=None, namespace=None):  # noqa: E501
        """BTParameterSpecEnumAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._enum_name = None
        self._option_names = None
        self._options = None
        self._namespace = None
        self.discriminator = None

        if enum_name is not None:
            self.enum_name = enum_name
        if option_names is not None:
            self.option_names = option_names
        if options is not None:
            self.options = options
        if namespace is not None:
            self.namespace = namespace

    @property
    def enum_name(self):
        """Gets the enum_name of this BTParameterSpecEnumAllOf.  # noqa: E501


        :return: The enum_name of this BTParameterSpecEnumAllOf.  # noqa: E501
        :rtype: str
        """
        return self._enum_name

    @enum_name.setter
    def enum_name(self, enum_name):
        """Sets the enum_name of this BTParameterSpecEnumAllOf.


        :param enum_name: The enum_name of this BTParameterSpecEnumAllOf.  # noqa: E501
        :type: str
        """

        self._enum_name = enum_name

    @property
    def option_names(self):
        """Gets the option_names of this BTParameterSpecEnumAllOf.  # noqa: E501


        :return: The option_names of this BTParameterSpecEnumAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._option_names

    @option_names.setter
    def option_names(self, option_names):
        """Sets the option_names of this BTParameterSpecEnumAllOf.


        :param option_names: The option_names of this BTParameterSpecEnumAllOf.  # noqa: E501
        :type: list[str]
        """

        self._option_names = option_names

    @property
    def options(self):
        """Gets the options of this BTParameterSpecEnumAllOf.  # noqa: E501


        :return: The options of this BTParameterSpecEnumAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this BTParameterSpecEnumAllOf.


        :param options: The options of this BTParameterSpecEnumAllOf.  # noqa: E501
        :type: list[str]
        """

        self._options = options

    @property
    def namespace(self):
        """Gets the namespace of this BTParameterSpecEnumAllOf.  # noqa: E501


        :return: The namespace of this BTParameterSpecEnumAllOf.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this BTParameterSpecEnumAllOf.


        :param namespace: The namespace of this BTParameterSpecEnumAllOf.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

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
        if not isinstance(other, BTParameterSpecEnumAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
