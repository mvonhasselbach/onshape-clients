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


class BTCopyElementParams(object):
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
        'document_id_source': 'str',
        'workspace_id_source': 'str',
        'element_id_source': 'str',
        'anchor_element_id': 'str',
        'is_group_anchor': 'bool'
    }

    attribute_map = {
        'document_id_source': 'documentIdSource',
        'workspace_id_source': 'workspaceIdSource',
        'element_id_source': 'elementIdSource',
        'anchor_element_id': 'anchorElementId',
        'is_group_anchor': 'isGroupAnchor'
    }

    def __init__(self, document_id_source=None, workspace_id_source=None, element_id_source=None, anchor_element_id=None, is_group_anchor=None):  # noqa: E501
        """BTCopyElementParams - a model defined in OpenAPI"""  # noqa: E501

        self._document_id_source = None
        self._workspace_id_source = None
        self._element_id_source = None
        self._anchor_element_id = None
        self._is_group_anchor = None
        self.discriminator = None

        if document_id_source is not None:
            self.document_id_source = document_id_source
        if workspace_id_source is not None:
            self.workspace_id_source = workspace_id_source
        if element_id_source is not None:
            self.element_id_source = element_id_source
        if anchor_element_id is not None:
            self.anchor_element_id = anchor_element_id
        if is_group_anchor is not None:
            self.is_group_anchor = is_group_anchor

    @property
    def document_id_source(self):
        """Gets the document_id_source of this BTCopyElementParams.  # noqa: E501


        :return: The document_id_source of this BTCopyElementParams.  # noqa: E501
        :rtype: str
        """
        return self._document_id_source

    @document_id_source.setter
    def document_id_source(self, document_id_source):
        """Sets the document_id_source of this BTCopyElementParams.


        :param document_id_source: The document_id_source of this BTCopyElementParams.  # noqa: E501
        :type: str
        """

        self._document_id_source = document_id_source

    @property
    def workspace_id_source(self):
        """Gets the workspace_id_source of this BTCopyElementParams.  # noqa: E501


        :return: The workspace_id_source of this BTCopyElementParams.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id_source

    @workspace_id_source.setter
    def workspace_id_source(self, workspace_id_source):
        """Sets the workspace_id_source of this BTCopyElementParams.


        :param workspace_id_source: The workspace_id_source of this BTCopyElementParams.  # noqa: E501
        :type: str
        """

        self._workspace_id_source = workspace_id_source

    @property
    def element_id_source(self):
        """Gets the element_id_source of this BTCopyElementParams.  # noqa: E501


        :return: The element_id_source of this BTCopyElementParams.  # noqa: E501
        :rtype: str
        """
        return self._element_id_source

    @element_id_source.setter
    def element_id_source(self, element_id_source):
        """Sets the element_id_source of this BTCopyElementParams.


        :param element_id_source: The element_id_source of this BTCopyElementParams.  # noqa: E501
        :type: str
        """

        self._element_id_source = element_id_source

    @property
    def anchor_element_id(self):
        """Gets the anchor_element_id of this BTCopyElementParams.  # noqa: E501


        :return: The anchor_element_id of this BTCopyElementParams.  # noqa: E501
        :rtype: str
        """
        return self._anchor_element_id

    @anchor_element_id.setter
    def anchor_element_id(self, anchor_element_id):
        """Sets the anchor_element_id of this BTCopyElementParams.


        :param anchor_element_id: The anchor_element_id of this BTCopyElementParams.  # noqa: E501
        :type: str
        """

        self._anchor_element_id = anchor_element_id

    @property
    def is_group_anchor(self):
        """Gets the is_group_anchor of this BTCopyElementParams.  # noqa: E501


        :return: The is_group_anchor of this BTCopyElementParams.  # noqa: E501
        :rtype: bool
        """
        return self._is_group_anchor

    @is_group_anchor.setter
    def is_group_anchor(self, is_group_anchor):
        """Sets the is_group_anchor of this BTCopyElementParams.


        :param is_group_anchor: The is_group_anchor of this BTCopyElementParams.  # noqa: E501
        :type: bool
        """

        self._is_group_anchor = is_group_anchor

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
        if not isinstance(other, BTCopyElementParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
