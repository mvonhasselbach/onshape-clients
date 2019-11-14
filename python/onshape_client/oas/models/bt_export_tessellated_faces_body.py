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


class BTExportTessellatedFacesBody(object):
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
        'faces': 'list[BTExportTessellatedFacesFace]',
        'body_type': 'str',
        'appearance': 'BTGraphicsAppearance',
        'facet_points': 'list[BTVector3d]',
        'id': 'str'
    }

    attribute_map = {
        'faces': 'faces',
        'body_type': 'bodyType',
        'appearance': 'appearance',
        'facet_points': 'facetPoints',
        'id': 'id'
    }

    def __init__(self, faces=None, body_type=None, appearance=None, facet_points=None, id=None):  # noqa: E501
        """BTExportTessellatedFacesBody - a model defined in OpenAPI"""  # noqa: E501

        self._faces = None
        self._body_type = None
        self._appearance = None
        self._facet_points = None
        self._id = None
        self.discriminator = None

        if faces is not None:
            self.faces = faces
        if body_type is not None:
            self.body_type = body_type
        if appearance is not None:
            self.appearance = appearance
        if facet_points is not None:
            self.facet_points = facet_points
        if id is not None:
            self.id = id

    @property
    def faces(self):
        """Gets the faces of this BTExportTessellatedFacesBody.  # noqa: E501


        :return: The faces of this BTExportTessellatedFacesBody.  # noqa: E501
        :rtype: list[BTExportTessellatedFacesFace]
        """
        return self._faces

    @faces.setter
    def faces(self, faces):
        """Sets the faces of this BTExportTessellatedFacesBody.


        :param faces: The faces of this BTExportTessellatedFacesBody.  # noqa: E501
        :type: list[BTExportTessellatedFacesFace]
        """

        self._faces = faces

    @property
    def body_type(self):
        """Gets the body_type of this BTExportTessellatedFacesBody.  # noqa: E501


        :return: The body_type of this BTExportTessellatedFacesBody.  # noqa: E501
        :rtype: str
        """
        return self._body_type

    @body_type.setter
    def body_type(self, body_type):
        """Sets the body_type of this BTExportTessellatedFacesBody.


        :param body_type: The body_type of this BTExportTessellatedFacesBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["SOLID", "SURFACE", "UNKNOWN"]  # noqa: E501
        if body_type not in allowed_values:
            raise ValueError(
                "Invalid value for `body_type` ({0}), must be one of {1}"  # noqa: E501
                .format(body_type, allowed_values)
            )

        self._body_type = body_type

    @property
    def appearance(self):
        """Gets the appearance of this BTExportTessellatedFacesBody.  # noqa: E501


        :return: The appearance of this BTExportTessellatedFacesBody.  # noqa: E501
        :rtype: BTGraphicsAppearance
        """
        return self._appearance

    @appearance.setter
    def appearance(self, appearance):
        """Sets the appearance of this BTExportTessellatedFacesBody.


        :param appearance: The appearance of this BTExportTessellatedFacesBody.  # noqa: E501
        :type: BTGraphicsAppearance
        """

        self._appearance = appearance

    @property
    def facet_points(self):
        """Gets the facet_points of this BTExportTessellatedFacesBody.  # noqa: E501


        :return: The facet_points of this BTExportTessellatedFacesBody.  # noqa: E501
        :rtype: list[BTVector3d]
        """
        return self._facet_points

    @facet_points.setter
    def facet_points(self, facet_points):
        """Sets the facet_points of this BTExportTessellatedFacesBody.


        :param facet_points: The facet_points of this BTExportTessellatedFacesBody.  # noqa: E501
        :type: list[BTVector3d]
        """

        self._facet_points = facet_points

    @property
    def id(self):
        """Gets the id of this BTExportTessellatedFacesBody.  # noqa: E501


        :return: The id of this BTExportTessellatedFacesBody.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTExportTessellatedFacesBody.


        :param id: The id of this BTExportTessellatedFacesBody.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, BTExportTessellatedFacesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
