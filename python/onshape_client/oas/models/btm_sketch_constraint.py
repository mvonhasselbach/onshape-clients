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


class BTMSketchConstraint(object):
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
        'driven_dimension': 'bool',
        'constraint_type': 'str',
        'has_offset_data1': 'bool',
        'offset_orientation1': 'bool',
        'offset_distance1': 'float',
        'has_offset_data2': 'bool',
        'offset_orientation2': 'bool',
        'offset_distance2': 'float',
        'has_pierce_parameter': 'bool',
        'pierce_parameter': 'float',
        'help_parameters': 'list[float]',
        'parameters': 'list[BTMParameter]',
        'entity_id_and_replace_in_dependent_fields': 'str',
        'node_id': 'str',
        'namespace': 'str',
        'import_microversion': 'str',
        'entity_id': 'str'
    }

    attribute_map = {
        'driven_dimension': 'drivenDimension',
        'constraint_type': 'constraintType',
        'has_offset_data1': 'hasOffsetData1',
        'offset_orientation1': 'offsetOrientation1',
        'offset_distance1': 'offsetDistance1',
        'has_offset_data2': 'hasOffsetData2',
        'offset_orientation2': 'offsetOrientation2',
        'offset_distance2': 'offsetDistance2',
        'has_pierce_parameter': 'hasPierceParameter',
        'pierce_parameter': 'pierceParameter',
        'help_parameters': 'helpParameters',
        'parameters': 'parameters',
        'entity_id_and_replace_in_dependent_fields': 'entityIdAndReplaceInDependentFields',
        'node_id': 'nodeId',
        'namespace': 'namespace',
        'import_microversion': 'importMicroversion',
        'entity_id': 'entityId'
    }

    def __init__(self, driven_dimension=None, constraint_type=None, has_offset_data1=None, offset_orientation1=None, offset_distance1=None, has_offset_data2=None, offset_orientation2=None, offset_distance2=None, has_pierce_parameter=None, pierce_parameter=None, help_parameters=None, parameters=None, entity_id_and_replace_in_dependent_fields=None, node_id=None, namespace=None, import_microversion=None, entity_id=None):  # noqa: E501
        """BTMSketchConstraint - a model defined in OpenAPI"""  # noqa: E501

        self._driven_dimension = None
        self._constraint_type = None
        self._has_offset_data1 = None
        self._offset_orientation1 = None
        self._offset_distance1 = None
        self._has_offset_data2 = None
        self._offset_orientation2 = None
        self._offset_distance2 = None
        self._has_pierce_parameter = None
        self._pierce_parameter = None
        self._help_parameters = None
        self._parameters = None
        self._entity_id_and_replace_in_dependent_fields = None
        self._node_id = None
        self._namespace = None
        self._import_microversion = None
        self._entity_id = None
        self.discriminator = None

        if driven_dimension is not None:
            self.driven_dimension = driven_dimension
        if constraint_type is not None:
            self.constraint_type = constraint_type
        if has_offset_data1 is not None:
            self.has_offset_data1 = has_offset_data1
        if offset_orientation1 is not None:
            self.offset_orientation1 = offset_orientation1
        if offset_distance1 is not None:
            self.offset_distance1 = offset_distance1
        if has_offset_data2 is not None:
            self.has_offset_data2 = has_offset_data2
        if offset_orientation2 is not None:
            self.offset_orientation2 = offset_orientation2
        if offset_distance2 is not None:
            self.offset_distance2 = offset_distance2
        if has_pierce_parameter is not None:
            self.has_pierce_parameter = has_pierce_parameter
        if pierce_parameter is not None:
            self.pierce_parameter = pierce_parameter
        if help_parameters is not None:
            self.help_parameters = help_parameters
        if parameters is not None:
            self.parameters = parameters
        if entity_id_and_replace_in_dependent_fields is not None:
            self.entity_id_and_replace_in_dependent_fields = entity_id_and_replace_in_dependent_fields
        if node_id is not None:
            self.node_id = node_id
        if namespace is not None:
            self.namespace = namespace
        if import_microversion is not None:
            self.import_microversion = import_microversion
        if entity_id is not None:
            self.entity_id = entity_id

    @property
    def driven_dimension(self):
        """Gets the driven_dimension of this BTMSketchConstraint.  # noqa: E501


        :return: The driven_dimension of this BTMSketchConstraint.  # noqa: E501
        :rtype: bool
        """
        return self._driven_dimension

    @driven_dimension.setter
    def driven_dimension(self, driven_dimension):
        """Sets the driven_dimension of this BTMSketchConstraint.


        :param driven_dimension: The driven_dimension of this BTMSketchConstraint.  # noqa: E501
        :type: bool
        """

        self._driven_dimension = driven_dimension

    @property
    def constraint_type(self):
        """Gets the constraint_type of this BTMSketchConstraint.  # noqa: E501


        :return: The constraint_type of this BTMSketchConstraint.  # noqa: E501
        :rtype: str
        """
        return self._constraint_type

    @constraint_type.setter
    def constraint_type(self, constraint_type):
        """Sets the constraint_type of this BTMSketchConstraint.


        :param constraint_type: The constraint_type of this BTMSketchConstraint.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "COINCIDENT", "PARALLEL", "VERTICAL", "HORIZONTAL", "PERPENDICULAR", "CONCENTRIC", "MIRROR", "MIDPOINT", "TANGENT", "EQUAL", "LENGTH", "DISTANCE", "ANGLE", "RADIUS", "NORMAL", "FIX", "PROJECTED", "OFFSET", "CIRCULAR_PATTERN", "PIERCE", "LINEAR_PATTERN", "MAJOR_DIAMETER", "MINOR_DIAMETER", "QUADRANT", "DIAMETER", "SILHOUETTED", "CENTERLINE_DIMENSION", "INTERSECTED", "RHO", "EQUAL_CURVATURE", "UNKNOWN"]  # noqa: E501
        if constraint_type not in allowed_values:
            raise ValueError(
                "Invalid value for `constraint_type` ({0}), must be one of {1}"  # noqa: E501
                .format(constraint_type, allowed_values)
            )

        self._constraint_type = constraint_type

    @property
    def has_offset_data1(self):
        """Gets the has_offset_data1 of this BTMSketchConstraint.  # noqa: E501


        :return: The has_offset_data1 of this BTMSketchConstraint.  # noqa: E501
        :rtype: bool
        """
        return self._has_offset_data1

    @has_offset_data1.setter
    def has_offset_data1(self, has_offset_data1):
        """Sets the has_offset_data1 of this BTMSketchConstraint.


        :param has_offset_data1: The has_offset_data1 of this BTMSketchConstraint.  # noqa: E501
        :type: bool
        """

        self._has_offset_data1 = has_offset_data1

    @property
    def offset_orientation1(self):
        """Gets the offset_orientation1 of this BTMSketchConstraint.  # noqa: E501


        :return: The offset_orientation1 of this BTMSketchConstraint.  # noqa: E501
        :rtype: bool
        """
        return self._offset_orientation1

    @offset_orientation1.setter
    def offset_orientation1(self, offset_orientation1):
        """Sets the offset_orientation1 of this BTMSketchConstraint.


        :param offset_orientation1: The offset_orientation1 of this BTMSketchConstraint.  # noqa: E501
        :type: bool
        """

        self._offset_orientation1 = offset_orientation1

    @property
    def offset_distance1(self):
        """Gets the offset_distance1 of this BTMSketchConstraint.  # noqa: E501


        :return: The offset_distance1 of this BTMSketchConstraint.  # noqa: E501
        :rtype: float
        """
        return self._offset_distance1

    @offset_distance1.setter
    def offset_distance1(self, offset_distance1):
        """Sets the offset_distance1 of this BTMSketchConstraint.


        :param offset_distance1: The offset_distance1 of this BTMSketchConstraint.  # noqa: E501
        :type: float
        """

        self._offset_distance1 = offset_distance1

    @property
    def has_offset_data2(self):
        """Gets the has_offset_data2 of this BTMSketchConstraint.  # noqa: E501


        :return: The has_offset_data2 of this BTMSketchConstraint.  # noqa: E501
        :rtype: bool
        """
        return self._has_offset_data2

    @has_offset_data2.setter
    def has_offset_data2(self, has_offset_data2):
        """Sets the has_offset_data2 of this BTMSketchConstraint.


        :param has_offset_data2: The has_offset_data2 of this BTMSketchConstraint.  # noqa: E501
        :type: bool
        """

        self._has_offset_data2 = has_offset_data2

    @property
    def offset_orientation2(self):
        """Gets the offset_orientation2 of this BTMSketchConstraint.  # noqa: E501


        :return: The offset_orientation2 of this BTMSketchConstraint.  # noqa: E501
        :rtype: bool
        """
        return self._offset_orientation2

    @offset_orientation2.setter
    def offset_orientation2(self, offset_orientation2):
        """Sets the offset_orientation2 of this BTMSketchConstraint.


        :param offset_orientation2: The offset_orientation2 of this BTMSketchConstraint.  # noqa: E501
        :type: bool
        """

        self._offset_orientation2 = offset_orientation2

    @property
    def offset_distance2(self):
        """Gets the offset_distance2 of this BTMSketchConstraint.  # noqa: E501


        :return: The offset_distance2 of this BTMSketchConstraint.  # noqa: E501
        :rtype: float
        """
        return self._offset_distance2

    @offset_distance2.setter
    def offset_distance2(self, offset_distance2):
        """Sets the offset_distance2 of this BTMSketchConstraint.


        :param offset_distance2: The offset_distance2 of this BTMSketchConstraint.  # noqa: E501
        :type: float
        """

        self._offset_distance2 = offset_distance2

    @property
    def has_pierce_parameter(self):
        """Gets the has_pierce_parameter of this BTMSketchConstraint.  # noqa: E501


        :return: The has_pierce_parameter of this BTMSketchConstraint.  # noqa: E501
        :rtype: bool
        """
        return self._has_pierce_parameter

    @has_pierce_parameter.setter
    def has_pierce_parameter(self, has_pierce_parameter):
        """Sets the has_pierce_parameter of this BTMSketchConstraint.


        :param has_pierce_parameter: The has_pierce_parameter of this BTMSketchConstraint.  # noqa: E501
        :type: bool
        """

        self._has_pierce_parameter = has_pierce_parameter

    @property
    def pierce_parameter(self):
        """Gets the pierce_parameter of this BTMSketchConstraint.  # noqa: E501


        :return: The pierce_parameter of this BTMSketchConstraint.  # noqa: E501
        :rtype: float
        """
        return self._pierce_parameter

    @pierce_parameter.setter
    def pierce_parameter(self, pierce_parameter):
        """Sets the pierce_parameter of this BTMSketchConstraint.


        :param pierce_parameter: The pierce_parameter of this BTMSketchConstraint.  # noqa: E501
        :type: float
        """

        self._pierce_parameter = pierce_parameter

    @property
    def help_parameters(self):
        """Gets the help_parameters of this BTMSketchConstraint.  # noqa: E501


        :return: The help_parameters of this BTMSketchConstraint.  # noqa: E501
        :rtype: list[float]
        """
        return self._help_parameters

    @help_parameters.setter
    def help_parameters(self, help_parameters):
        """Sets the help_parameters of this BTMSketchConstraint.


        :param help_parameters: The help_parameters of this BTMSketchConstraint.  # noqa: E501
        :type: list[float]
        """

        self._help_parameters = help_parameters

    @property
    def parameters(self):
        """Gets the parameters of this BTMSketchConstraint.  # noqa: E501


        :return: The parameters of this BTMSketchConstraint.  # noqa: E501
        :rtype: list[BTMParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this BTMSketchConstraint.


        :param parameters: The parameters of this BTMSketchConstraint.  # noqa: E501
        :type: list[BTMParameter]
        """

        self._parameters = parameters

    @property
    def entity_id_and_replace_in_dependent_fields(self):
        """Gets the entity_id_and_replace_in_dependent_fields of this BTMSketchConstraint.  # noqa: E501


        :return: The entity_id_and_replace_in_dependent_fields of this BTMSketchConstraint.  # noqa: E501
        :rtype: str
        """
        return self._entity_id_and_replace_in_dependent_fields

    @entity_id_and_replace_in_dependent_fields.setter
    def entity_id_and_replace_in_dependent_fields(self, entity_id_and_replace_in_dependent_fields):
        """Sets the entity_id_and_replace_in_dependent_fields of this BTMSketchConstraint.


        :param entity_id_and_replace_in_dependent_fields: The entity_id_and_replace_in_dependent_fields of this BTMSketchConstraint.  # noqa: E501
        :type: str
        """

        self._entity_id_and_replace_in_dependent_fields = entity_id_and_replace_in_dependent_fields

    @property
    def node_id(self):
        """Gets the node_id of this BTMSketchConstraint.  # noqa: E501


        :return: The node_id of this BTMSketchConstraint.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this BTMSketchConstraint.


        :param node_id: The node_id of this BTMSketchConstraint.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def namespace(self):
        """Gets the namespace of this BTMSketchConstraint.  # noqa: E501


        :return: The namespace of this BTMSketchConstraint.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this BTMSketchConstraint.


        :param namespace: The namespace of this BTMSketchConstraint.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def import_microversion(self):
        """Gets the import_microversion of this BTMSketchConstraint.  # noqa: E501


        :return: The import_microversion of this BTMSketchConstraint.  # noqa: E501
        :rtype: str
        """
        return self._import_microversion

    @import_microversion.setter
    def import_microversion(self, import_microversion):
        """Sets the import_microversion of this BTMSketchConstraint.


        :param import_microversion: The import_microversion of this BTMSketchConstraint.  # noqa: E501
        :type: str
        """

        self._import_microversion = import_microversion

    @property
    def entity_id(self):
        """Gets the entity_id of this BTMSketchConstraint.  # noqa: E501


        :return: The entity_id of this BTMSketchConstraint.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this BTMSketchConstraint.


        :param entity_id: The entity_id of this BTMSketchConstraint.  # noqa: E501
        :type: str
        """

        self._entity_id = entity_id

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
        if not isinstance(other, BTMSketchConstraint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
