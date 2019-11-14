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


class BTMIndividualQueryWithOccurrenceBase(object):
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
        'path': 'list[str]',
        'query_string': 'str',
        'deterministic_ids': 'list[str]',
        'deterministic_id_list': 'BTMIndividualQueryBase',
        'query': 'BTMIndividualQueryBase',
        'import_microversion': 'str',
        'node_id': 'str'
    }

    attribute_map = {
        'path': 'path',
        'query_string': 'queryString',
        'deterministic_ids': 'deterministicIds',
        'deterministic_id_list': 'deterministicIdList',
        'query': 'query',
        'import_microversion': 'importMicroversion',
        'node_id': 'nodeId'
    }

    discriminator_value_class_map = {
        'BTMFeatureQueryWithOccurrence': 'BTMFeatureQueryWithOccurrence',
        'BTMIndividualOccurrenceQuery': 'BTMIndividualOccurrenceQuery',
        'BTMIndividualQueryWithOccurrence': 'BTMIndividualQueryWithOccurrence'
    }

    def __init__(self, path=None, query_string=None, deterministic_ids=None, deterministic_id_list=None, query=None, import_microversion=None, node_id=None):  # noqa: E501
        """BTMIndividualQueryWithOccurrenceBase - a model defined in OpenAPI"""  # noqa: E501

        self._path = None
        self._query_string = None
        self._deterministic_ids = None
        self._deterministic_id_list = None
        self._query = None
        self._import_microversion = None
        self._node_id = None
        self.discriminator = 'type'

        if path is not None:
            self.path = path
        if query_string is not None:
            self.query_string = query_string
        if deterministic_ids is not None:
            self.deterministic_ids = deterministic_ids
        if deterministic_id_list is not None:
            self.deterministic_id_list = deterministic_id_list
        if query is not None:
            self.query = query
        if import_microversion is not None:
            self.import_microversion = import_microversion
        if node_id is not None:
            self.node_id = node_id

    @property
    def path(self):
        """Gets the path of this BTMIndividualQueryWithOccurrenceBase.  # noqa: E501


        :return: The path of this BTMIndividualQueryWithOccurrenceBase.  # noqa: E501
        :rtype: list[str]
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this BTMIndividualQueryWithOccurrenceBase.


        :param path: The path of this BTMIndividualQueryWithOccurrenceBase.  # noqa: E501
        :type: list[str]
        """

        self._path = path

    @property
    def query_string(self):
        """Gets the query_string of this BTMIndividualQueryWithOccurrenceBase.  # noqa: E501


        :return: The query_string of this BTMIndividualQueryWithOccurrenceBase.  # noqa: E501
        :rtype: str
        """
        return self._query_string

    @query_string.setter
    def query_string(self, query_string):
        """Sets the query_string of this BTMIndividualQueryWithOccurrenceBase.


        :param query_string: The query_string of this BTMIndividualQueryWithOccurrenceBase.  # noqa: E501
        :type: str
        """

        self._query_string = query_string

    @property
    def deterministic_ids(self):
        """Gets the deterministic_ids of this BTMIndividualQueryWithOccurrenceBase.  # noqa: E501


        :return: The deterministic_ids of this BTMIndividualQueryWithOccurrenceBase.  # noqa: E501
        :rtype: list[str]
        """
        return self._deterministic_ids

    @deterministic_ids.setter
    def deterministic_ids(self, deterministic_ids):
        """Sets the deterministic_ids of this BTMIndividualQueryWithOccurrenceBase.


        :param deterministic_ids: The deterministic_ids of this BTMIndividualQueryWithOccurrenceBase.  # noqa: E501
        :type: list[str]
        """

        self._deterministic_ids = deterministic_ids

    @property
    def deterministic_id_list(self):
        """Gets the deterministic_id_list of this BTMIndividualQueryWithOccurrenceBase.  # noqa: E501


        :return: The deterministic_id_list of this BTMIndividualQueryWithOccurrenceBase.  # noqa: E501
        :rtype: BTMIndividualQueryBase
        """
        return self._deterministic_id_list

    @deterministic_id_list.setter
    def deterministic_id_list(self, deterministic_id_list):
        """Sets the deterministic_id_list of this BTMIndividualQueryWithOccurrenceBase.


        :param deterministic_id_list: The deterministic_id_list of this BTMIndividualQueryWithOccurrenceBase.  # noqa: E501
        :type: BTMIndividualQueryBase
        """

        self._deterministic_id_list = deterministic_id_list

    @property
    def query(self):
        """Gets the query of this BTMIndividualQueryWithOccurrenceBase.  # noqa: E501


        :return: The query of this BTMIndividualQueryWithOccurrenceBase.  # noqa: E501
        :rtype: BTMIndividualQueryBase
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this BTMIndividualQueryWithOccurrenceBase.


        :param query: The query of this BTMIndividualQueryWithOccurrenceBase.  # noqa: E501
        :type: BTMIndividualQueryBase
        """

        self._query = query

    @property
    def import_microversion(self):
        """Gets the import_microversion of this BTMIndividualQueryWithOccurrenceBase.  # noqa: E501


        :return: The import_microversion of this BTMIndividualQueryWithOccurrenceBase.  # noqa: E501
        :rtype: str
        """
        return self._import_microversion

    @import_microversion.setter
    def import_microversion(self, import_microversion):
        """Sets the import_microversion of this BTMIndividualQueryWithOccurrenceBase.


        :param import_microversion: The import_microversion of this BTMIndividualQueryWithOccurrenceBase.  # noqa: E501
        :type: str
        """

        self._import_microversion = import_microversion

    @property
    def node_id(self):
        """Gets the node_id of this BTMIndividualQueryWithOccurrenceBase.  # noqa: E501


        :return: The node_id of this BTMIndividualQueryWithOccurrenceBase.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this BTMIndividualQueryWithOccurrenceBase.


        :param node_id: The node_id of this BTMIndividualQueryWithOccurrenceBase.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, BTMIndividualQueryWithOccurrenceBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
