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


class BTSetFeatureRollbackResponseAllOf(object):
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
        'microversion_id': 'BTMicroversionId',
        'rollback_index': 'int'
    }

    attribute_map = {
        'microversion_id': 'microversionId',
        'rollback_index': 'rollbackIndex'
    }

    def __init__(self, microversion_id=None, rollback_index=None):  # noqa: E501
        """BTSetFeatureRollbackResponseAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._microversion_id = None
        self._rollback_index = None
        self.discriminator = None

        if microversion_id is not None:
            self.microversion_id = microversion_id
        if rollback_index is not None:
            self.rollback_index = rollback_index

    @property
    def microversion_id(self):
        """Gets the microversion_id of this BTSetFeatureRollbackResponseAllOf.  # noqa: E501


        :return: The microversion_id of this BTSetFeatureRollbackResponseAllOf.  # noqa: E501
        :rtype: BTMicroversionId
        """
        return self._microversion_id

    @microversion_id.setter
    def microversion_id(self, microversion_id):
        """Sets the microversion_id of this BTSetFeatureRollbackResponseAllOf.


        :param microversion_id: The microversion_id of this BTSetFeatureRollbackResponseAllOf.  # noqa: E501
        :type: BTMicroversionId
        """

        self._microversion_id = microversion_id

    @property
    def rollback_index(self):
        """Gets the rollback_index of this BTSetFeatureRollbackResponseAllOf.  # noqa: E501


        :return: The rollback_index of this BTSetFeatureRollbackResponseAllOf.  # noqa: E501
        :rtype: int
        """
        return self._rollback_index

    @rollback_index.setter
    def rollback_index(self, rollback_index):
        """Sets the rollback_index of this BTSetFeatureRollbackResponseAllOf.


        :param rollback_index: The rollback_index of this BTSetFeatureRollbackResponseAllOf.  # noqa: E501
        :type: int
        """

        self._rollback_index = rollback_index

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
        if not isinstance(other, BTSetFeatureRollbackResponseAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
