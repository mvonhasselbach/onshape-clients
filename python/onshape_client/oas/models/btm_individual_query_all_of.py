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


class BTMIndividualQueryAllOf(object):
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
        'persistent_query': 'BTPStatement',
        'variable_name': 'BTMIndividualQuery',
        'query_statement': 'BTPStatement'
    }

    attribute_map = {
        'persistent_query': 'persistentQuery',
        'variable_name': 'variableName',
        'query_statement': 'queryStatement'
    }

    def __init__(self, persistent_query=None, variable_name=None, query_statement=None):  # noqa: E501
        """BTMIndividualQueryAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._persistent_query = None
        self._variable_name = None
        self._query_statement = None
        self.discriminator = None

        if persistent_query is not None:
            self.persistent_query = persistent_query
        if variable_name is not None:
            self.variable_name = variable_name
        if query_statement is not None:
            self.query_statement = query_statement

    @property
    def persistent_query(self):
        """Gets the persistent_query of this BTMIndividualQueryAllOf.  # noqa: E501


        :return: The persistent_query of this BTMIndividualQueryAllOf.  # noqa: E501
        :rtype: BTPStatement
        """
        return self._persistent_query

    @persistent_query.setter
    def persistent_query(self, persistent_query):
        """Sets the persistent_query of this BTMIndividualQueryAllOf.


        :param persistent_query: The persistent_query of this BTMIndividualQueryAllOf.  # noqa: E501
        :type: BTPStatement
        """

        self._persistent_query = persistent_query

    @property
    def variable_name(self):
        """Gets the variable_name of this BTMIndividualQueryAllOf.  # noqa: E501


        :return: The variable_name of this BTMIndividualQueryAllOf.  # noqa: E501
        :rtype: BTMIndividualQuery
        """
        return self._variable_name

    @variable_name.setter
    def variable_name(self, variable_name):
        """Sets the variable_name of this BTMIndividualQueryAllOf.


        :param variable_name: The variable_name of this BTMIndividualQueryAllOf.  # noqa: E501
        :type: BTMIndividualQuery
        """

        self._variable_name = variable_name

    @property
    def query_statement(self):
        """Gets the query_statement of this BTMIndividualQueryAllOf.  # noqa: E501


        :return: The query_statement of this BTMIndividualQueryAllOf.  # noqa: E501
        :rtype: BTPStatement
        """
        return self._query_statement

    @query_statement.setter
    def query_statement(self, query_statement):
        """Sets the query_statement of this BTMIndividualQueryAllOf.


        :param query_statement: The query_statement of this BTMIndividualQueryAllOf.  # noqa: E501
        :type: BTPStatement
        """

        self._query_statement = query_statement

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
        if not isinstance(other, BTMIndividualQueryAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
