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


class BTMicroversionIdAndConfiguration(object):
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
        'deleted': 'bool',
        'description': 'str',
        'cache_key': 'str',
        'microversion': 'BTMicroversionId',
        'configuration_parameter_id_to_value': 'dict(str, BTFSValue)'
    }

    attribute_map = {
        'deleted': 'deleted',
        'description': 'description',
        'cache_key': 'cacheKey',
        'microversion': 'microversion',
        'configuration_parameter_id_to_value': 'configurationParameterIdToValue'
    }

    def __init__(self, deleted=None, description=None, cache_key=None, microversion=None, configuration_parameter_id_to_value=None):  # noqa: E501
        """BTMicroversionIdAndConfiguration - a model defined in OpenAPI"""  # noqa: E501

        self._deleted = None
        self._description = None
        self._cache_key = None
        self._microversion = None
        self._configuration_parameter_id_to_value = None
        self.discriminator = None

        if deleted is not None:
            self.deleted = deleted
        if description is not None:
            self.description = description
        if cache_key is not None:
            self.cache_key = cache_key
        if microversion is not None:
            self.microversion = microversion
        if configuration_parameter_id_to_value is not None:
            self.configuration_parameter_id_to_value = configuration_parameter_id_to_value

    @property
    def deleted(self):
        """Gets the deleted of this BTMicroversionIdAndConfiguration.  # noqa: E501


        :return: The deleted of this BTMicroversionIdAndConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this BTMicroversionIdAndConfiguration.


        :param deleted: The deleted of this BTMicroversionIdAndConfiguration.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def description(self):
        """Gets the description of this BTMicroversionIdAndConfiguration.  # noqa: E501


        :return: The description of this BTMicroversionIdAndConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTMicroversionIdAndConfiguration.


        :param description: The description of this BTMicroversionIdAndConfiguration.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def cache_key(self):
        """Gets the cache_key of this BTMicroversionIdAndConfiguration.  # noqa: E501


        :return: The cache_key of this BTMicroversionIdAndConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._cache_key

    @cache_key.setter
    def cache_key(self, cache_key):
        """Sets the cache_key of this BTMicroversionIdAndConfiguration.


        :param cache_key: The cache_key of this BTMicroversionIdAndConfiguration.  # noqa: E501
        :type: str
        """

        self._cache_key = cache_key

    @property
    def microversion(self):
        """Gets the microversion of this BTMicroversionIdAndConfiguration.  # noqa: E501


        :return: The microversion of this BTMicroversionIdAndConfiguration.  # noqa: E501
        :rtype: BTMicroversionId
        """
        return self._microversion

    @microversion.setter
    def microversion(self, microversion):
        """Sets the microversion of this BTMicroversionIdAndConfiguration.


        :param microversion: The microversion of this BTMicroversionIdAndConfiguration.  # noqa: E501
        :type: BTMicroversionId
        """

        self._microversion = microversion

    @property
    def configuration_parameter_id_to_value(self):
        """Gets the configuration_parameter_id_to_value of this BTMicroversionIdAndConfiguration.  # noqa: E501


        :return: The configuration_parameter_id_to_value of this BTMicroversionIdAndConfiguration.  # noqa: E501
        :rtype: dict(str, BTFSValue)
        """
        return self._configuration_parameter_id_to_value

    @configuration_parameter_id_to_value.setter
    def configuration_parameter_id_to_value(self, configuration_parameter_id_to_value):
        """Sets the configuration_parameter_id_to_value of this BTMicroversionIdAndConfiguration.


        :param configuration_parameter_id_to_value: The configuration_parameter_id_to_value of this BTMicroversionIdAndConfiguration.  # noqa: E501
        :type: dict(str, BTFSValue)
        """

        self._configuration_parameter_id_to_value = configuration_parameter_id_to_value

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
        if not isinstance(other, BTMicroversionIdAndConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
