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


class BTElementReference(object):
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
        'external_reference': 'bool',
        'microversion_id_and_configuration': 'BTMicroversionIdAndConfiguration',
        'external_document_with_version_and_element_id': 'BTDocumentWithVersionAndElementId',
        'external_document_with_version': 'BTDocumentWithVersionId',
        'configured': 'bool',
        'element_id': 'str',
        'full_element_id': 'BTFullElementId',
        'node_id': 'str'
    }

    attribute_map = {
        'external_reference': 'externalReference',
        'microversion_id_and_configuration': 'microversionIdAndConfiguration',
        'external_document_with_version_and_element_id': 'externalDocumentWithVersionAndElementId',
        'external_document_with_version': 'externalDocumentWithVersion',
        'configured': 'configured',
        'element_id': 'elementId',
        'full_element_id': 'fullElementId',
        'node_id': 'nodeId'
    }

    discriminator_value_class_map = {
        'BTExternalReference': 'BTExternalReference'
    }

    def __init__(self, external_reference=None, microversion_id_and_configuration=None, external_document_with_version_and_element_id=None, external_document_with_version=None, configured=None, element_id=None, full_element_id=None, node_id=None):  # noqa: E501
        """BTElementReference - a model defined in OpenAPI"""  # noqa: E501

        self._external_reference = None
        self._microversion_id_and_configuration = None
        self._external_document_with_version_and_element_id = None
        self._external_document_with_version = None
        self._configured = None
        self._element_id = None
        self._full_element_id = None
        self._node_id = None
        self.discriminator = 'type'

        if external_reference is not None:
            self.external_reference = external_reference
        if microversion_id_and_configuration is not None:
            self.microversion_id_and_configuration = microversion_id_and_configuration
        if external_document_with_version_and_element_id is not None:
            self.external_document_with_version_and_element_id = external_document_with_version_and_element_id
        if external_document_with_version is not None:
            self.external_document_with_version = external_document_with_version
        if configured is not None:
            self.configured = configured
        if element_id is not None:
            self.element_id = element_id
        if full_element_id is not None:
            self.full_element_id = full_element_id
        if node_id is not None:
            self.node_id = node_id

    @property
    def external_reference(self):
        """Gets the external_reference of this BTElementReference.  # noqa: E501


        :return: The external_reference of this BTElementReference.  # noqa: E501
        :rtype: bool
        """
        return self._external_reference

    @external_reference.setter
    def external_reference(self, external_reference):
        """Sets the external_reference of this BTElementReference.


        :param external_reference: The external_reference of this BTElementReference.  # noqa: E501
        :type: bool
        """

        self._external_reference = external_reference

    @property
    def microversion_id_and_configuration(self):
        """Gets the microversion_id_and_configuration of this BTElementReference.  # noqa: E501


        :return: The microversion_id_and_configuration of this BTElementReference.  # noqa: E501
        :rtype: BTMicroversionIdAndConfiguration
        """
        return self._microversion_id_and_configuration

    @microversion_id_and_configuration.setter
    def microversion_id_and_configuration(self, microversion_id_and_configuration):
        """Sets the microversion_id_and_configuration of this BTElementReference.


        :param microversion_id_and_configuration: The microversion_id_and_configuration of this BTElementReference.  # noqa: E501
        :type: BTMicroversionIdAndConfiguration
        """

        self._microversion_id_and_configuration = microversion_id_and_configuration

    @property
    def external_document_with_version_and_element_id(self):
        """Gets the external_document_with_version_and_element_id of this BTElementReference.  # noqa: E501


        :return: The external_document_with_version_and_element_id of this BTElementReference.  # noqa: E501
        :rtype: BTDocumentWithVersionAndElementId
        """
        return self._external_document_with_version_and_element_id

    @external_document_with_version_and_element_id.setter
    def external_document_with_version_and_element_id(self, external_document_with_version_and_element_id):
        """Sets the external_document_with_version_and_element_id of this BTElementReference.


        :param external_document_with_version_and_element_id: The external_document_with_version_and_element_id of this BTElementReference.  # noqa: E501
        :type: BTDocumentWithVersionAndElementId
        """

        self._external_document_with_version_and_element_id = external_document_with_version_and_element_id

    @property
    def external_document_with_version(self):
        """Gets the external_document_with_version of this BTElementReference.  # noqa: E501


        :return: The external_document_with_version of this BTElementReference.  # noqa: E501
        :rtype: BTDocumentWithVersionId
        """
        return self._external_document_with_version

    @external_document_with_version.setter
    def external_document_with_version(self, external_document_with_version):
        """Sets the external_document_with_version of this BTElementReference.


        :param external_document_with_version: The external_document_with_version of this BTElementReference.  # noqa: E501
        :type: BTDocumentWithVersionId
        """

        self._external_document_with_version = external_document_with_version

    @property
    def configured(self):
        """Gets the configured of this BTElementReference.  # noqa: E501


        :return: The configured of this BTElementReference.  # noqa: E501
        :rtype: bool
        """
        return self._configured

    @configured.setter
    def configured(self, configured):
        """Sets the configured of this BTElementReference.


        :param configured: The configured of this BTElementReference.  # noqa: E501
        :type: bool
        """

        self._configured = configured

    @property
    def element_id(self):
        """Gets the element_id of this BTElementReference.  # noqa: E501


        :return: The element_id of this BTElementReference.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this BTElementReference.


        :param element_id: The element_id of this BTElementReference.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

    @property
    def full_element_id(self):
        """Gets the full_element_id of this BTElementReference.  # noqa: E501


        :return: The full_element_id of this BTElementReference.  # noqa: E501
        :rtype: BTFullElementId
        """
        return self._full_element_id

    @full_element_id.setter
    def full_element_id(self, full_element_id):
        """Sets the full_element_id of this BTElementReference.


        :param full_element_id: The full_element_id of this BTElementReference.  # noqa: E501
        :type: BTFullElementId
        """

        self._full_element_id = full_element_id

    @property
    def node_id(self):
        """Gets the node_id of this BTElementReference.  # noqa: E501


        :return: The node_id of this BTElementReference.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this BTElementReference.


        :param node_id: The node_id of this BTElementReference.  # noqa: E501
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
        if not isinstance(other, BTElementReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
