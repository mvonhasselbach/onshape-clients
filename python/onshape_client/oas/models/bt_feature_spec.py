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


class BTFeatureSpec(object):
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
        'full_feature_type': 'str',
        'all_parameters': 'list[BTParameterSpec]',
        'localized_name': 'str',
        'localizable_name': 'str',
        'additional_localized_strings': 'int',
        'location_infos': 'list[BTLocationInfo]',
        'namespace_the_source': 'bool',
        'namespace_including_enums': 'str',
        'signature': 'str',
        'strings_to_localize': 'list[str]',
        'source_microversion_id': 'str',
        'feature_type_name': 'str',
        'feature_type': 'str',
        'groups': 'list[BTParameterGroupSpec]',
        'ui_hints': 'list[str]',
        'source_location': 'BTLocationInfo',
        'icon_uri': 'str',
        'language_version': 'int',
        'linked_location_name': 'str',
        'feature_name_template': 'str',
        'manipulator_change_function': 'str',
        'filter_selectors': 'list[str]',
        'editing_logic': 'BTEditingLogic',
        'parameters': 'list[BTParameterSpec]',
        'namespace': 'str'
    }

    attribute_map = {
        'full_feature_type': 'fullFeatureType',
        'all_parameters': 'allParameters',
        'localized_name': 'localizedName',
        'localizable_name': 'localizableName',
        'additional_localized_strings': 'additionalLocalizedStrings',
        'location_infos': 'locationInfos',
        'namespace_the_source': 'namespaceTheSource',
        'namespace_including_enums': 'namespaceIncludingEnums',
        'signature': 'signature',
        'strings_to_localize': 'stringsToLocalize',
        'source_microversion_id': 'sourceMicroversionId',
        'feature_type_name': 'featureTypeName',
        'feature_type': 'featureType',
        'groups': 'groups',
        'ui_hints': 'uiHints',
        'source_location': 'sourceLocation',
        'icon_uri': 'iconUri',
        'language_version': 'languageVersion',
        'linked_location_name': 'linkedLocationName',
        'feature_name_template': 'featureNameTemplate',
        'manipulator_change_function': 'manipulatorChangeFunction',
        'filter_selectors': 'filterSelectors',
        'editing_logic': 'editingLogic',
        'parameters': 'parameters',
        'namespace': 'namespace'
    }

    def __init__(self, full_feature_type=None, all_parameters=None, localized_name=None, localizable_name=None, additional_localized_strings=None, location_infos=None, namespace_the_source=None, namespace_including_enums=None, signature=None, strings_to_localize=None, source_microversion_id=None, feature_type_name=None, feature_type=None, groups=None, ui_hints=None, source_location=None, icon_uri=None, language_version=None, linked_location_name=None, feature_name_template=None, manipulator_change_function=None, filter_selectors=None, editing_logic=None, parameters=None, namespace=None):  # noqa: E501
        """BTFeatureSpec - a model defined in OpenAPI"""  # noqa: E501

        self._full_feature_type = None
        self._all_parameters = None
        self._localized_name = None
        self._localizable_name = None
        self._additional_localized_strings = None
        self._location_infos = None
        self._namespace_the_source = None
        self._namespace_including_enums = None
        self._signature = None
        self._strings_to_localize = None
        self._source_microversion_id = None
        self._feature_type_name = None
        self._feature_type = None
        self._groups = None
        self._ui_hints = None
        self._source_location = None
        self._icon_uri = None
        self._language_version = None
        self._linked_location_name = None
        self._feature_name_template = None
        self._manipulator_change_function = None
        self._filter_selectors = None
        self._editing_logic = None
        self._parameters = None
        self._namespace = None
        self.discriminator = None

        if full_feature_type is not None:
            self.full_feature_type = full_feature_type
        if all_parameters is not None:
            self.all_parameters = all_parameters
        if localized_name is not None:
            self.localized_name = localized_name
        if localizable_name is not None:
            self.localizable_name = localizable_name
        if additional_localized_strings is not None:
            self.additional_localized_strings = additional_localized_strings
        if location_infos is not None:
            self.location_infos = location_infos
        if namespace_the_source is not None:
            self.namespace_the_source = namespace_the_source
        if namespace_including_enums is not None:
            self.namespace_including_enums = namespace_including_enums
        if signature is not None:
            self.signature = signature
        if strings_to_localize is not None:
            self.strings_to_localize = strings_to_localize
        if source_microversion_id is not None:
            self.source_microversion_id = source_microversion_id
        if feature_type_name is not None:
            self.feature_type_name = feature_type_name
        if feature_type is not None:
            self.feature_type = feature_type
        if groups is not None:
            self.groups = groups
        if ui_hints is not None:
            self.ui_hints = ui_hints
        if source_location is not None:
            self.source_location = source_location
        if icon_uri is not None:
            self.icon_uri = icon_uri
        if language_version is not None:
            self.language_version = language_version
        if linked_location_name is not None:
            self.linked_location_name = linked_location_name
        if feature_name_template is not None:
            self.feature_name_template = feature_name_template
        if manipulator_change_function is not None:
            self.manipulator_change_function = manipulator_change_function
        if filter_selectors is not None:
            self.filter_selectors = filter_selectors
        if editing_logic is not None:
            self.editing_logic = editing_logic
        if parameters is not None:
            self.parameters = parameters
        if namespace is not None:
            self.namespace = namespace

    @property
    def full_feature_type(self):
        """Gets the full_feature_type of this BTFeatureSpec.  # noqa: E501


        :return: The full_feature_type of this BTFeatureSpec.  # noqa: E501
        :rtype: str
        """
        return self._full_feature_type

    @full_feature_type.setter
    def full_feature_type(self, full_feature_type):
        """Sets the full_feature_type of this BTFeatureSpec.


        :param full_feature_type: The full_feature_type of this BTFeatureSpec.  # noqa: E501
        :type: str
        """

        self._full_feature_type = full_feature_type

    @property
    def all_parameters(self):
        """Gets the all_parameters of this BTFeatureSpec.  # noqa: E501


        :return: The all_parameters of this BTFeatureSpec.  # noqa: E501
        :rtype: list[BTParameterSpec]
        """
        return self._all_parameters

    @all_parameters.setter
    def all_parameters(self, all_parameters):
        """Sets the all_parameters of this BTFeatureSpec.


        :param all_parameters: The all_parameters of this BTFeatureSpec.  # noqa: E501
        :type: list[BTParameterSpec]
        """

        self._all_parameters = all_parameters

    @property
    def localized_name(self):
        """Gets the localized_name of this BTFeatureSpec.  # noqa: E501


        :return: The localized_name of this BTFeatureSpec.  # noqa: E501
        :rtype: str
        """
        return self._localized_name

    @localized_name.setter
    def localized_name(self, localized_name):
        """Sets the localized_name of this BTFeatureSpec.


        :param localized_name: The localized_name of this BTFeatureSpec.  # noqa: E501
        :type: str
        """

        self._localized_name = localized_name

    @property
    def localizable_name(self):
        """Gets the localizable_name of this BTFeatureSpec.  # noqa: E501


        :return: The localizable_name of this BTFeatureSpec.  # noqa: E501
        :rtype: str
        """
        return self._localizable_name

    @localizable_name.setter
    def localizable_name(self, localizable_name):
        """Sets the localizable_name of this BTFeatureSpec.


        :param localizable_name: The localizable_name of this BTFeatureSpec.  # noqa: E501
        :type: str
        """

        self._localizable_name = localizable_name

    @property
    def additional_localized_strings(self):
        """Gets the additional_localized_strings of this BTFeatureSpec.  # noqa: E501


        :return: The additional_localized_strings of this BTFeatureSpec.  # noqa: E501
        :rtype: int
        """
        return self._additional_localized_strings

    @additional_localized_strings.setter
    def additional_localized_strings(self, additional_localized_strings):
        """Sets the additional_localized_strings of this BTFeatureSpec.


        :param additional_localized_strings: The additional_localized_strings of this BTFeatureSpec.  # noqa: E501
        :type: int
        """

        self._additional_localized_strings = additional_localized_strings

    @property
    def location_infos(self):
        """Gets the location_infos of this BTFeatureSpec.  # noqa: E501


        :return: The location_infos of this BTFeatureSpec.  # noqa: E501
        :rtype: list[BTLocationInfo]
        """
        return self._location_infos

    @location_infos.setter
    def location_infos(self, location_infos):
        """Sets the location_infos of this BTFeatureSpec.


        :param location_infos: The location_infos of this BTFeatureSpec.  # noqa: E501
        :type: list[BTLocationInfo]
        """

        self._location_infos = location_infos

    @property
    def namespace_the_source(self):
        """Gets the namespace_the_source of this BTFeatureSpec.  # noqa: E501


        :return: The namespace_the_source of this BTFeatureSpec.  # noqa: E501
        :rtype: bool
        """
        return self._namespace_the_source

    @namespace_the_source.setter
    def namespace_the_source(self, namespace_the_source):
        """Sets the namespace_the_source of this BTFeatureSpec.


        :param namespace_the_source: The namespace_the_source of this BTFeatureSpec.  # noqa: E501
        :type: bool
        """

        self._namespace_the_source = namespace_the_source

    @property
    def namespace_including_enums(self):
        """Gets the namespace_including_enums of this BTFeatureSpec.  # noqa: E501


        :return: The namespace_including_enums of this BTFeatureSpec.  # noqa: E501
        :rtype: str
        """
        return self._namespace_including_enums

    @namespace_including_enums.setter
    def namespace_including_enums(self, namespace_including_enums):
        """Sets the namespace_including_enums of this BTFeatureSpec.


        :param namespace_including_enums: The namespace_including_enums of this BTFeatureSpec.  # noqa: E501
        :type: str
        """

        self._namespace_including_enums = namespace_including_enums

    @property
    def signature(self):
        """Gets the signature of this BTFeatureSpec.  # noqa: E501


        :return: The signature of this BTFeatureSpec.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this BTFeatureSpec.


        :param signature: The signature of this BTFeatureSpec.  # noqa: E501
        :type: str
        """

        self._signature = signature

    @property
    def strings_to_localize(self):
        """Gets the strings_to_localize of this BTFeatureSpec.  # noqa: E501


        :return: The strings_to_localize of this BTFeatureSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._strings_to_localize

    @strings_to_localize.setter
    def strings_to_localize(self, strings_to_localize):
        """Sets the strings_to_localize of this BTFeatureSpec.


        :param strings_to_localize: The strings_to_localize of this BTFeatureSpec.  # noqa: E501
        :type: list[str]
        """

        self._strings_to_localize = strings_to_localize

    @property
    def source_microversion_id(self):
        """Gets the source_microversion_id of this BTFeatureSpec.  # noqa: E501


        :return: The source_microversion_id of this BTFeatureSpec.  # noqa: E501
        :rtype: str
        """
        return self._source_microversion_id

    @source_microversion_id.setter
    def source_microversion_id(self, source_microversion_id):
        """Sets the source_microversion_id of this BTFeatureSpec.


        :param source_microversion_id: The source_microversion_id of this BTFeatureSpec.  # noqa: E501
        :type: str
        """

        self._source_microversion_id = source_microversion_id

    @property
    def feature_type_name(self):
        """Gets the feature_type_name of this BTFeatureSpec.  # noqa: E501


        :return: The feature_type_name of this BTFeatureSpec.  # noqa: E501
        :rtype: str
        """
        return self._feature_type_name

    @feature_type_name.setter
    def feature_type_name(self, feature_type_name):
        """Sets the feature_type_name of this BTFeatureSpec.


        :param feature_type_name: The feature_type_name of this BTFeatureSpec.  # noqa: E501
        :type: str
        """

        self._feature_type_name = feature_type_name

    @property
    def feature_type(self):
        """Gets the feature_type of this BTFeatureSpec.  # noqa: E501


        :return: The feature_type of this BTFeatureSpec.  # noqa: E501
        :rtype: str
        """
        return self._feature_type

    @feature_type.setter
    def feature_type(self, feature_type):
        """Sets the feature_type of this BTFeatureSpec.


        :param feature_type: The feature_type of this BTFeatureSpec.  # noqa: E501
        :type: str
        """

        self._feature_type = feature_type

    @property
    def groups(self):
        """Gets the groups of this BTFeatureSpec.  # noqa: E501


        :return: The groups of this BTFeatureSpec.  # noqa: E501
        :rtype: list[BTParameterGroupSpec]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this BTFeatureSpec.


        :param groups: The groups of this BTFeatureSpec.  # noqa: E501
        :type: list[BTParameterGroupSpec]
        """

        self._groups = groups

    @property
    def ui_hints(self):
        """Gets the ui_hints of this BTFeatureSpec.  # noqa: E501


        :return: The ui_hints of this BTFeatureSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._ui_hints

    @ui_hints.setter
    def ui_hints(self, ui_hints):
        """Sets the ui_hints of this BTFeatureSpec.


        :param ui_hints: The ui_hints of this BTFeatureSpec.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["OPPOSITE_DIRECTION", "ALWAYS_HIDDEN", "SHOW_CREATE_SELECTION", "CONTROL_VISIBILITY", "NO_PREVIEW_PROVIDED", "REMEMBER_PREVIOUS_VALUE", "DISPLAY_SHORT", "ALLOW_FEATURE_SELECTION", "MATE_CONNECTOR_AXIS_TYPE", "PRIMARY_AXIS", "SHOW_EXPRESSION", "OPPOSITE_DIRECTION_CIRCULAR", "SHOW_LABEL", "HORIZONTAL_ENUM", "UNCONFIGURABLE", "MATCH_LAST_ARRAY_ITEM", "COLLAPSE_ARRAY_ITEMS", "INITIAL_FOCUS_ON_EDIT", "INITIAL_FOCUS", "DISPLAY_CURRENT_VALUE_ONLY", "READ_ONLY", "PREVENT_CREATING_NEW_MATE_CONNECTORS", "FIRST_IN_ROW", "ALLOW_QUERY_ORDER", "PREVENT_ARRAY_REORDER", "UNKNOWN"]  # noqa: E501
        if not set(ui_hints).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `ui_hints` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(ui_hints) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._ui_hints = ui_hints

    @property
    def source_location(self):
        """Gets the source_location of this BTFeatureSpec.  # noqa: E501


        :return: The source_location of this BTFeatureSpec.  # noqa: E501
        :rtype: BTLocationInfo
        """
        return self._source_location

    @source_location.setter
    def source_location(self, source_location):
        """Sets the source_location of this BTFeatureSpec.


        :param source_location: The source_location of this BTFeatureSpec.  # noqa: E501
        :type: BTLocationInfo
        """

        self._source_location = source_location

    @property
    def icon_uri(self):
        """Gets the icon_uri of this BTFeatureSpec.  # noqa: E501


        :return: The icon_uri of this BTFeatureSpec.  # noqa: E501
        :rtype: str
        """
        return self._icon_uri

    @icon_uri.setter
    def icon_uri(self, icon_uri):
        """Sets the icon_uri of this BTFeatureSpec.


        :param icon_uri: The icon_uri of this BTFeatureSpec.  # noqa: E501
        :type: str
        """

        self._icon_uri = icon_uri

    @property
    def language_version(self):
        """Gets the language_version of this BTFeatureSpec.  # noqa: E501


        :return: The language_version of this BTFeatureSpec.  # noqa: E501
        :rtype: int
        """
        return self._language_version

    @language_version.setter
    def language_version(self, language_version):
        """Sets the language_version of this BTFeatureSpec.


        :param language_version: The language_version of this BTFeatureSpec.  # noqa: E501
        :type: int
        """

        self._language_version = language_version

    @property
    def linked_location_name(self):
        """Gets the linked_location_name of this BTFeatureSpec.  # noqa: E501


        :return: The linked_location_name of this BTFeatureSpec.  # noqa: E501
        :rtype: str
        """
        return self._linked_location_name

    @linked_location_name.setter
    def linked_location_name(self, linked_location_name):
        """Sets the linked_location_name of this BTFeatureSpec.


        :param linked_location_name: The linked_location_name of this BTFeatureSpec.  # noqa: E501
        :type: str
        """

        self._linked_location_name = linked_location_name

    @property
    def feature_name_template(self):
        """Gets the feature_name_template of this BTFeatureSpec.  # noqa: E501


        :return: The feature_name_template of this BTFeatureSpec.  # noqa: E501
        :rtype: str
        """
        return self._feature_name_template

    @feature_name_template.setter
    def feature_name_template(self, feature_name_template):
        """Sets the feature_name_template of this BTFeatureSpec.


        :param feature_name_template: The feature_name_template of this BTFeatureSpec.  # noqa: E501
        :type: str
        """

        self._feature_name_template = feature_name_template

    @property
    def manipulator_change_function(self):
        """Gets the manipulator_change_function of this BTFeatureSpec.  # noqa: E501


        :return: The manipulator_change_function of this BTFeatureSpec.  # noqa: E501
        :rtype: str
        """
        return self._manipulator_change_function

    @manipulator_change_function.setter
    def manipulator_change_function(self, manipulator_change_function):
        """Sets the manipulator_change_function of this BTFeatureSpec.


        :param manipulator_change_function: The manipulator_change_function of this BTFeatureSpec.  # noqa: E501
        :type: str
        """

        self._manipulator_change_function = manipulator_change_function

    @property
    def filter_selectors(self):
        """Gets the filter_selectors of this BTFeatureSpec.  # noqa: E501


        :return: The filter_selectors of this BTFeatureSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._filter_selectors

    @filter_selectors.setter
    def filter_selectors(self, filter_selectors):
        """Sets the filter_selectors of this BTFeatureSpec.


        :param filter_selectors: The filter_selectors of this BTFeatureSpec.  # noqa: E501
        :type: list[str]
        """

        self._filter_selectors = filter_selectors

    @property
    def editing_logic(self):
        """Gets the editing_logic of this BTFeatureSpec.  # noqa: E501


        :return: The editing_logic of this BTFeatureSpec.  # noqa: E501
        :rtype: BTEditingLogic
        """
        return self._editing_logic

    @editing_logic.setter
    def editing_logic(self, editing_logic):
        """Sets the editing_logic of this BTFeatureSpec.


        :param editing_logic: The editing_logic of this BTFeatureSpec.  # noqa: E501
        :type: BTEditingLogic
        """

        self._editing_logic = editing_logic

    @property
    def parameters(self):
        """Gets the parameters of this BTFeatureSpec.  # noqa: E501


        :return: The parameters of this BTFeatureSpec.  # noqa: E501
        :rtype: list[BTParameterSpec]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this BTFeatureSpec.


        :param parameters: The parameters of this BTFeatureSpec.  # noqa: E501
        :type: list[BTParameterSpec]
        """

        self._parameters = parameters

    @property
    def namespace(self):
        """Gets the namespace of this BTFeatureSpec.  # noqa: E501


        :return: The namespace of this BTFeatureSpec.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this BTFeatureSpec.


        :param namespace: The namespace of this BTFeatureSpec.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

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
        if not isinstance(other, BTFeatureSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
