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


class Operation(object):
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
        'tags': 'list[str]',
        'summary': 'str',
        'description': 'str',
        'external_docs': 'ExternalDocumentation',
        'operation_id': 'str',
        'parameters': 'list[Parameter]',
        'request_body': 'RequestBody',
        'responses': 'dict(str, ApiResponse)',
        'callbacks': 'dict(str, Callback)',
        'deprecated': 'bool',
        'security': 'list[SecurityRequirement]',
        'servers': 'list[Server]',
        'extensions': 'dict(str, object)'
    }

    attribute_map = {
        'tags': 'tags',
        'summary': 'summary',
        'description': 'description',
        'external_docs': 'externalDocs',
        'operation_id': 'operationId',
        'parameters': 'parameters',
        'request_body': 'requestBody',
        'responses': 'responses',
        'callbacks': 'callbacks',
        'deprecated': 'deprecated',
        'security': 'security',
        'servers': 'servers',
        'extensions': 'extensions'
    }

    def __init__(self, tags=None, summary=None, description=None, external_docs=None, operation_id=None, parameters=None, request_body=None, responses=None, callbacks=None, deprecated=None, security=None, servers=None, extensions=None):  # noqa: E501
        """Operation - a model defined in OpenAPI"""  # noqa: E501

        self._tags = None
        self._summary = None
        self._description = None
        self._external_docs = None
        self._operation_id = None
        self._parameters = None
        self._request_body = None
        self._responses = None
        self._callbacks = None
        self._deprecated = None
        self._security = None
        self._servers = None
        self._extensions = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if summary is not None:
            self.summary = summary
        if description is not None:
            self.description = description
        if external_docs is not None:
            self.external_docs = external_docs
        if operation_id is not None:
            self.operation_id = operation_id
        if parameters is not None:
            self.parameters = parameters
        if request_body is not None:
            self.request_body = request_body
        if responses is not None:
            self.responses = responses
        if callbacks is not None:
            self.callbacks = callbacks
        if deprecated is not None:
            self.deprecated = deprecated
        if security is not None:
            self.security = security
        if servers is not None:
            self.servers = servers
        if extensions is not None:
            self.extensions = extensions

    @property
    def tags(self):
        """Gets the tags of this Operation.  # noqa: E501


        :return: The tags of this Operation.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Operation.


        :param tags: The tags of this Operation.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def summary(self):
        """Gets the summary of this Operation.  # noqa: E501


        :return: The summary of this Operation.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this Operation.


        :param summary: The summary of this Operation.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def description(self):
        """Gets the description of this Operation.  # noqa: E501


        :return: The description of this Operation.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Operation.


        :param description: The description of this Operation.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def external_docs(self):
        """Gets the external_docs of this Operation.  # noqa: E501


        :return: The external_docs of this Operation.  # noqa: E501
        :rtype: ExternalDocumentation
        """
        return self._external_docs

    @external_docs.setter
    def external_docs(self, external_docs):
        """Sets the external_docs of this Operation.


        :param external_docs: The external_docs of this Operation.  # noqa: E501
        :type: ExternalDocumentation
        """

        self._external_docs = external_docs

    @property
    def operation_id(self):
        """Gets the operation_id of this Operation.  # noqa: E501


        :return: The operation_id of this Operation.  # noqa: E501
        :rtype: str
        """
        return self._operation_id

    @operation_id.setter
    def operation_id(self, operation_id):
        """Sets the operation_id of this Operation.


        :param operation_id: The operation_id of this Operation.  # noqa: E501
        :type: str
        """

        self._operation_id = operation_id

    @property
    def parameters(self):
        """Gets the parameters of this Operation.  # noqa: E501


        :return: The parameters of this Operation.  # noqa: E501
        :rtype: list[Parameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this Operation.


        :param parameters: The parameters of this Operation.  # noqa: E501
        :type: list[Parameter]
        """

        self._parameters = parameters

    @property
    def request_body(self):
        """Gets the request_body of this Operation.  # noqa: E501


        :return: The request_body of this Operation.  # noqa: E501
        :rtype: RequestBody
        """
        return self._request_body

    @request_body.setter
    def request_body(self, request_body):
        """Sets the request_body of this Operation.


        :param request_body: The request_body of this Operation.  # noqa: E501
        :type: RequestBody
        """

        self._request_body = request_body

    @property
    def responses(self):
        """Gets the responses of this Operation.  # noqa: E501


        :return: The responses of this Operation.  # noqa: E501
        :rtype: dict(str, ApiResponse)
        """
        return self._responses

    @responses.setter
    def responses(self, responses):
        """Sets the responses of this Operation.


        :param responses: The responses of this Operation.  # noqa: E501
        :type: dict(str, ApiResponse)
        """

        self._responses = responses

    @property
    def callbacks(self):
        """Gets the callbacks of this Operation.  # noqa: E501


        :return: The callbacks of this Operation.  # noqa: E501
        :rtype: dict(str, Callback)
        """
        return self._callbacks

    @callbacks.setter
    def callbacks(self, callbacks):
        """Sets the callbacks of this Operation.


        :param callbacks: The callbacks of this Operation.  # noqa: E501
        :type: dict(str, Callback)
        """

        self._callbacks = callbacks

    @property
    def deprecated(self):
        """Gets the deprecated of this Operation.  # noqa: E501


        :return: The deprecated of this Operation.  # noqa: E501
        :rtype: bool
        """
        return self._deprecated

    @deprecated.setter
    def deprecated(self, deprecated):
        """Sets the deprecated of this Operation.


        :param deprecated: The deprecated of this Operation.  # noqa: E501
        :type: bool
        """

        self._deprecated = deprecated

    @property
    def security(self):
        """Gets the security of this Operation.  # noqa: E501


        :return: The security of this Operation.  # noqa: E501
        :rtype: list[SecurityRequirement]
        """
        return self._security

    @security.setter
    def security(self, security):
        """Sets the security of this Operation.


        :param security: The security of this Operation.  # noqa: E501
        :type: list[SecurityRequirement]
        """

        self._security = security

    @property
    def servers(self):
        """Gets the servers of this Operation.  # noqa: E501


        :return: The servers of this Operation.  # noqa: E501
        :rtype: list[Server]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this Operation.


        :param servers: The servers of this Operation.  # noqa: E501
        :type: list[Server]
        """

        self._servers = servers

    @property
    def extensions(self):
        """Gets the extensions of this Operation.  # noqa: E501


        :return: The extensions of this Operation.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        """Sets the extensions of this Operation.


        :param extensions: The extensions of this Operation.  # noqa: E501
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
        if not isinstance(other, Operation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
