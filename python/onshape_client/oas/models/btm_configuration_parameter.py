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


class BTMConfigurationParameter(object):
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
        'parameter_type': 'str',
        'generated_parameter_id': 'BTTreeNode',
        'valid': 'bool',
        'parameter_id': 'str',
        'parameter_name': 'str',
        'import_microversion': 'str',
        'node_id': 'str'
    }

    attribute_map = {
        'parameter_type': 'parameterType',
        'generated_parameter_id': 'generatedParameterId',
        'valid': 'valid',
        'parameter_id': 'parameterId',
        'parameter_name': 'parameterName',
        'import_microversion': 'importMicroversion',
        'node_id': 'nodeId'
    }

    discriminator_value_class_map = {
        'BTMConfigurationParameterBoolean': 'BTMConfigurationParameterBoolean',
        'BTMConfigurationParameterEnum': 'BTMConfigurationParameterEnum',
        'BTMConfigurationParameterString': 'BTMConfigurationParameterString',
        'BTMConfigurationParameterQuantity': 'BTMConfigurationParameterQuantity'
    }

    def __init__(self, parameter_type=None, generated_parameter_id=None, valid=None, parameter_id=None, parameter_name=None, import_microversion=None, node_id=None):  # noqa: E501
        """BTMConfigurationParameter - a model defined in OpenAPI"""  # noqa: E501

        self._parameter_type = None
        self._generated_parameter_id = None
        self._valid = None
        self._parameter_id = None
        self._parameter_name = None
        self._import_microversion = None
        self._node_id = None
        self.discriminator = 'type'

        if parameter_type is not None:
            self.parameter_type = parameter_type
        if generated_parameter_id is not None:
            self.generated_parameter_id = generated_parameter_id
        if valid is not None:
            self.valid = valid
        if parameter_id is not None:
            self.parameter_id = parameter_id
        if parameter_name is not None:
            self.parameter_name = parameter_name
        if import_microversion is not None:
            self.import_microversion = import_microversion
        if node_id is not None:
            self.node_id = node_id

    @property
    def parameter_type(self):
        """Gets the parameter_type of this BTMConfigurationParameter.  # noqa: E501


        :return: The parameter_type of this BTMConfigurationParameter.  # noqa: E501
        :rtype: str
        """
        return self._parameter_type

    @parameter_type.setter
    def parameter_type(self, parameter_type):
        """Sets the parameter_type of this BTMConfigurationParameter.


        :param parameter_type: The parameter_type of this BTMConfigurationParameter.  # noqa: E501
        :type: str
        """
        allowed_values = ["ENUM", "BOOLEAN", "STRING", "QUANTITY"]  # noqa: E501
        if parameter_type not in allowed_values:
            raise ValueError(
                "Invalid value for `parameter_type` ({0}), must be one of {1}"  # noqa: E501
                .format(parameter_type, allowed_values)
            )

        self._parameter_type = parameter_type

    @property
    def generated_parameter_id(self):
        """Gets the generated_parameter_id of this BTMConfigurationParameter.  # noqa: E501


        :return: The generated_parameter_id of this BTMConfigurationParameter.  # noqa: E501
        :rtype: BTTreeNode
        """
        return self._generated_parameter_id

    @generated_parameter_id.setter
    def generated_parameter_id(self, generated_parameter_id):
        """Sets the generated_parameter_id of this BTMConfigurationParameter.


        :param generated_parameter_id: The generated_parameter_id of this BTMConfigurationParameter.  # noqa: E501
        :type: BTTreeNode
        """

        self._generated_parameter_id = generated_parameter_id

    @property
    def valid(self):
        """Gets the valid of this BTMConfigurationParameter.  # noqa: E501


        :return: The valid of this BTMConfigurationParameter.  # noqa: E501
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """Sets the valid of this BTMConfigurationParameter.


        :param valid: The valid of this BTMConfigurationParameter.  # noqa: E501
        :type: bool
        """

        self._valid = valid

    @property
    def parameter_id(self):
        """Gets the parameter_id of this BTMConfigurationParameter.  # noqa: E501


        :return: The parameter_id of this BTMConfigurationParameter.  # noqa: E501
        :rtype: str
        """
        return self._parameter_id

    @parameter_id.setter
    def parameter_id(self, parameter_id):
        """Sets the parameter_id of this BTMConfigurationParameter.


        :param parameter_id: The parameter_id of this BTMConfigurationParameter.  # noqa: E501
        :type: str
        """

        self._parameter_id = parameter_id

    @property
    def parameter_name(self):
        """Gets the parameter_name of this BTMConfigurationParameter.  # noqa: E501


        :return: The parameter_name of this BTMConfigurationParameter.  # noqa: E501
        :rtype: str
        """
        return self._parameter_name

    @parameter_name.setter
    def parameter_name(self, parameter_name):
        """Sets the parameter_name of this BTMConfigurationParameter.


        :param parameter_name: The parameter_name of this BTMConfigurationParameter.  # noqa: E501
        :type: str
        """

        self._parameter_name = parameter_name

    @property
    def import_microversion(self):
        """Gets the import_microversion of this BTMConfigurationParameter.  # noqa: E501


        :return: The import_microversion of this BTMConfigurationParameter.  # noqa: E501
        :rtype: str
        """
        return self._import_microversion

    @import_microversion.setter
    def import_microversion(self, import_microversion):
        """Sets the import_microversion of this BTMConfigurationParameter.


        :param import_microversion: The import_microversion of this BTMConfigurationParameter.  # noqa: E501
        :type: str
        """

        self._import_microversion = import_microversion

    @property
    def node_id(self):
        """Gets the node_id of this BTMConfigurationParameter.  # noqa: E501


        :return: The node_id of this BTMConfigurationParameter.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this BTMConfigurationParameter.


        :param node_id: The node_id of this BTMConfigurationParameter.  # noqa: E501
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
        if not isinstance(other, BTMConfigurationParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
