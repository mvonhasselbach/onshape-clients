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


class Server(object):
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
        'url': 'str',
        'description': 'str',
        'variables': 'dict(str, ServerVariable)',
        'extensions': 'dict(str, object)'
    }

    attribute_map = {
        'url': 'url',
        'description': 'description',
        'variables': 'variables',
        'extensions': 'extensions'
    }

    def __init__(self, url=None, description=None, variables=None, extensions=None):  # noqa: E501
        """Server - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._description = None
        self._variables = None
        self._extensions = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if description is not None:
            self.description = description
        if variables is not None:
            self.variables = variables
        if extensions is not None:
            self.extensions = extensions

    @property
    def url(self):
        """Gets the url of this Server.  # noqa: E501


        :return: The url of this Server.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Server.


        :param url: The url of this Server.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def description(self):
        """Gets the description of this Server.  # noqa: E501


        :return: The description of this Server.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Server.


        :param description: The description of this Server.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def variables(self):
        """Gets the variables of this Server.  # noqa: E501


        :return: The variables of this Server.  # noqa: E501
        :rtype: dict(str, ServerVariable)
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this Server.


        :param variables: The variables of this Server.  # noqa: E501
        :type: dict(str, ServerVariable)
        """

        self._variables = variables

    @property
    def extensions(self):
        """Gets the extensions of this Server.  # noqa: E501


        :return: The extensions of this Server.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        """Sets the extensions of this Server.


        :param extensions: The extensions of this Server.  # noqa: E501
        :type: dict(str, object)
        """

        self._extensions = extensions

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
        if not isinstance(other, Server):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
