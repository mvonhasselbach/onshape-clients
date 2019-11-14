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


class BTDocumentElementInfo(object):
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
        'data_type': 'str',
        'thumbnails': 'str',
        'microversion_id': 'str',
        'element_type': 'str',
        'foreign_data_id': 'str',
        'unupdatable': 'bool',
        'specified_unit': 'str',
        'filename': 'str',
        'thumbnail_info': 'BTThumbnailInfo',
        'length_units': 'str',
        'angle_units': 'str',
        'mass_units': 'str',
        'name': 'str',
        'id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'data_type': 'dataType',
        'thumbnails': 'thumbnails',
        'microversion_id': 'microversionId',
        'element_type': 'elementType',
        'foreign_data_id': 'foreignDataId',
        'unupdatable': 'unupdatable',
        'specified_unit': 'specifiedUnit',
        'filename': 'filename',
        'thumbnail_info': 'thumbnailInfo',
        'length_units': 'lengthUnits',
        'angle_units': 'angleUnits',
        'mass_units': 'massUnits',
        'name': 'name',
        'id': 'id',
        'type': 'type'
    }

    def __init__(self, data_type=None, thumbnails=None, microversion_id=None, element_type=None, foreign_data_id=None, unupdatable=None, specified_unit=None, filename=None, thumbnail_info=None, length_units=None, angle_units=None, mass_units=None, name=None, id=None, type=None):  # noqa: E501
        """BTDocumentElementInfo - a model defined in OpenAPI"""  # noqa: E501

        self._data_type = None
        self._thumbnails = None
        self._microversion_id = None
        self._element_type = None
        self._foreign_data_id = None
        self._unupdatable = None
        self._specified_unit = None
        self._filename = None
        self._thumbnail_info = None
        self._length_units = None
        self._angle_units = None
        self._mass_units = None
        self._name = None
        self._id = None
        self._type = None
        self.discriminator = None

        if data_type is not None:
            self.data_type = data_type
        if thumbnails is not None:
            self.thumbnails = thumbnails
        if microversion_id is not None:
            self.microversion_id = microversion_id
        if element_type is not None:
            self.element_type = element_type
        if foreign_data_id is not None:
            self.foreign_data_id = foreign_data_id
        if unupdatable is not None:
            self.unupdatable = unupdatable
        if specified_unit is not None:
            self.specified_unit = specified_unit
        if filename is not None:
            self.filename = filename
        if thumbnail_info is not None:
            self.thumbnail_info = thumbnail_info
        if length_units is not None:
            self.length_units = length_units
        if angle_units is not None:
            self.angle_units = angle_units
        if mass_units is not None:
            self.mass_units = mass_units
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type

    @property
    def data_type(self):
        """Gets the data_type of this BTDocumentElementInfo.  # noqa: E501


        :return: The data_type of this BTDocumentElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this BTDocumentElementInfo.


        :param data_type: The data_type of this BTDocumentElementInfo.  # noqa: E501
        :type: str
        """

        self._data_type = data_type

    @property
    def thumbnails(self):
        """Gets the thumbnails of this BTDocumentElementInfo.  # noqa: E501


        :return: The thumbnails of this BTDocumentElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._thumbnails

    @thumbnails.setter
    def thumbnails(self, thumbnails):
        """Sets the thumbnails of this BTDocumentElementInfo.


        :param thumbnails: The thumbnails of this BTDocumentElementInfo.  # noqa: E501
        :type: str
        """

        self._thumbnails = thumbnails

    @property
    def microversion_id(self):
        """Gets the microversion_id of this BTDocumentElementInfo.  # noqa: E501


        :return: The microversion_id of this BTDocumentElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._microversion_id

    @microversion_id.setter
    def microversion_id(self, microversion_id):
        """Sets the microversion_id of this BTDocumentElementInfo.


        :param microversion_id: The microversion_id of this BTDocumentElementInfo.  # noqa: E501
        :type: str
        """

        self._microversion_id = microversion_id

    @property
    def element_type(self):
        """Gets the element_type of this BTDocumentElementInfo.  # noqa: E501


        :return: The element_type of this BTDocumentElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._element_type

    @element_type.setter
    def element_type(self, element_type):
        """Sets the element_type of this BTDocumentElementInfo.


        :param element_type: The element_type of this BTDocumentElementInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["PARTSTUDIO", "ASSEMBLY", "DRAWING", "FEATURESTUDIO", "BLOB", "APPLICATION", "TABLE", "BILLOFMATERIALS", "UNKNOWN"]  # noqa: E501
        if element_type not in allowed_values:
            raise ValueError(
                "Invalid value for `element_type` ({0}), must be one of {1}"  # noqa: E501
                .format(element_type, allowed_values)
            )

        self._element_type = element_type

    @property
    def foreign_data_id(self):
        """Gets the foreign_data_id of this BTDocumentElementInfo.  # noqa: E501


        :return: The foreign_data_id of this BTDocumentElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._foreign_data_id

    @foreign_data_id.setter
    def foreign_data_id(self, foreign_data_id):
        """Sets the foreign_data_id of this BTDocumentElementInfo.


        :param foreign_data_id: The foreign_data_id of this BTDocumentElementInfo.  # noqa: E501
        :type: str
        """

        self._foreign_data_id = foreign_data_id

    @property
    def unupdatable(self):
        """Gets the unupdatable of this BTDocumentElementInfo.  # noqa: E501


        :return: The unupdatable of this BTDocumentElementInfo.  # noqa: E501
        :rtype: bool
        """
        return self._unupdatable

    @unupdatable.setter
    def unupdatable(self, unupdatable):
        """Sets the unupdatable of this BTDocumentElementInfo.


        :param unupdatable: The unupdatable of this BTDocumentElementInfo.  # noqa: E501
        :type: bool
        """

        self._unupdatable = unupdatable

    @property
    def specified_unit(self):
        """Gets the specified_unit of this BTDocumentElementInfo.  # noqa: E501


        :return: The specified_unit of this BTDocumentElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._specified_unit

    @specified_unit.setter
    def specified_unit(self, specified_unit):
        """Sets the specified_unit of this BTDocumentElementInfo.


        :param specified_unit: The specified_unit of this BTDocumentElementInfo.  # noqa: E501
        :type: str
        """

        self._specified_unit = specified_unit

    @property
    def filename(self):
        """Gets the filename of this BTDocumentElementInfo.  # noqa: E501


        :return: The filename of this BTDocumentElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this BTDocumentElementInfo.


        :param filename: The filename of this BTDocumentElementInfo.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def thumbnail_info(self):
        """Gets the thumbnail_info of this BTDocumentElementInfo.  # noqa: E501


        :return: The thumbnail_info of this BTDocumentElementInfo.  # noqa: E501
        :rtype: BTThumbnailInfo
        """
        return self._thumbnail_info

    @thumbnail_info.setter
    def thumbnail_info(self, thumbnail_info):
        """Sets the thumbnail_info of this BTDocumentElementInfo.


        :param thumbnail_info: The thumbnail_info of this BTDocumentElementInfo.  # noqa: E501
        :type: BTThumbnailInfo
        """

        self._thumbnail_info = thumbnail_info

    @property
    def length_units(self):
        """Gets the length_units of this BTDocumentElementInfo.  # noqa: E501


        :return: The length_units of this BTDocumentElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._length_units

    @length_units.setter
    def length_units(self, length_units):
        """Sets the length_units of this BTDocumentElementInfo.


        :param length_units: The length_units of this BTDocumentElementInfo.  # noqa: E501
        :type: str
        """

        self._length_units = length_units

    @property
    def angle_units(self):
        """Gets the angle_units of this BTDocumentElementInfo.  # noqa: E501


        :return: The angle_units of this BTDocumentElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._angle_units

    @angle_units.setter
    def angle_units(self, angle_units):
        """Sets the angle_units of this BTDocumentElementInfo.


        :param angle_units: The angle_units of this BTDocumentElementInfo.  # noqa: E501
        :type: str
        """

        self._angle_units = angle_units

    @property
    def mass_units(self):
        """Gets the mass_units of this BTDocumentElementInfo.  # noqa: E501


        :return: The mass_units of this BTDocumentElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._mass_units

    @mass_units.setter
    def mass_units(self, mass_units):
        """Sets the mass_units of this BTDocumentElementInfo.


        :param mass_units: The mass_units of this BTDocumentElementInfo.  # noqa: E501
        :type: str
        """

        self._mass_units = mass_units

    @property
    def name(self):
        """Gets the name of this BTDocumentElementInfo.  # noqa: E501


        :return: The name of this BTDocumentElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTDocumentElementInfo.


        :param name: The name of this BTDocumentElementInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this BTDocumentElementInfo.  # noqa: E501


        :return: The id of this BTDocumentElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTDocumentElementInfo.


        :param id: The id of this BTDocumentElementInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this BTDocumentElementInfo.  # noqa: E501


        :return: The type of this BTDocumentElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BTDocumentElementInfo.


        :param type: The type of this BTDocumentElementInfo.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, BTDocumentElementInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
