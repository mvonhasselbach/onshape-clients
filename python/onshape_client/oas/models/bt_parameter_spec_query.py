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


class BTParameterSpecQuery(object):
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
        'max_number_of_picks': 'int',
        'filter': 'object',
        'additional_box_select_filter': 'object'
    }

    attribute_map = {
        'max_number_of_picks': 'maxNumberOfPicks',
        'filter': 'filter',
        'additional_box_select_filter': 'additionalBoxSelectFilter'
    }

    def __init__(self, max_number_of_picks=None, filter=None, additional_box_select_filter=None):  # noqa: E501
        """BTParameterSpecQuery - a model defined in OpenAPI"""  # noqa: E501

        self._max_number_of_picks = None
        self._filter = None
        self._additional_box_select_filter = None
        self.discriminator = None

        if max_number_of_picks is not None:
            self.max_number_of_picks = max_number_of_picks
        if filter is not None:
            self.filter = filter
        if additional_box_select_filter is not None:
            self.additional_box_select_filter = additional_box_select_filter

    @property
    def max_number_of_picks(self):
        """Gets the max_number_of_picks of this BTParameterSpecQuery.  # noqa: E501


        :return: The max_number_of_picks of this BTParameterSpecQuery.  # noqa: E501
        :rtype: int
        """
        return self._max_number_of_picks

    @max_number_of_picks.setter
    def max_number_of_picks(self, max_number_of_picks):
        """Sets the max_number_of_picks of this BTParameterSpecQuery.


        :param max_number_of_picks: The max_number_of_picks of this BTParameterSpecQuery.  # noqa: E501
        :type: int
        """

        self._max_number_of_picks = max_number_of_picks

    @property
    def filter(self):
        """Gets the filter of this BTParameterSpecQuery.  # noqa: E501


        :return: The filter of this BTParameterSpecQuery.  # noqa: E501
        :rtype: object
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this BTParameterSpecQuery.


        :param filter: The filter of this BTParameterSpecQuery.  # noqa: E501
        :type: object
        """

        self._filter = filter

    @property
    def additional_box_select_filter(self):
        """Gets the additional_box_select_filter of this BTParameterSpecQuery.  # noqa: E501


        :return: The additional_box_select_filter of this BTParameterSpecQuery.  # noqa: E501
        :rtype: object
        """
        return self._additional_box_select_filter

    @additional_box_select_filter.setter
    def additional_box_select_filter(self, additional_box_select_filter):
        """Sets the additional_box_select_filter of this BTParameterSpecQuery.


        :param additional_box_select_filter: The additional_box_select_filter of this BTParameterSpecQuery.  # noqa: E501
        :type: object
        """

        self._additional_box_select_filter = additional_box_select_filter

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
        if not isinstance(other, BTParameterSpecQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
