# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    OpenAPI spec version: 1.94
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BTPurchaseUserInfo(object):
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
        'purchase': 'BTPurchaseInfo',
        'user': 'BTUserBasicSummaryInfo',
        'consumed_quantity': 'int',
        'purchase_state': 'int',
        'name': 'str',
        'id': 'str',
        'href': 'str',
        'view_ref': 'str'
    }

    attribute_map = {
        'purchase': 'purchase',
        'user': 'user',
        'consumed_quantity': 'consumedQuantity',
        'purchase_state': 'purchaseState',
        'name': 'name',
        'id': 'id',
        'href': 'href',
        'view_ref': 'viewRef'
    }

    def __init__(self, purchase=None, user=None, consumed_quantity=None, purchase_state=None, name=None, id=None, href=None, view_ref=None):  # noqa: E501
        """BTPurchaseUserInfo - a model defined in OpenAPI"""  # noqa: E501

        self._purchase = None
        self._user = None
        self._consumed_quantity = None
        self._purchase_state = None
        self._name = None
        self._id = None
        self._href = None
        self._view_ref = None
        self.discriminator = None

        if purchase is not None:
            self.purchase = purchase
        if user is not None:
            self.user = user
        if consumed_quantity is not None:
            self.consumed_quantity = consumed_quantity
        if purchase_state is not None:
            self.purchase_state = purchase_state
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if view_ref is not None:
            self.view_ref = view_ref

    @property
    def purchase(self):
        """Gets the purchase of this BTPurchaseUserInfo.  # noqa: E501


        :return: The purchase of this BTPurchaseUserInfo.  # noqa: E501
        :rtype: BTPurchaseInfo
        """
        return self._purchase

    @purchase.setter
    def purchase(self, purchase):
        """Sets the purchase of this BTPurchaseUserInfo.


        :param purchase: The purchase of this BTPurchaseUserInfo.  # noqa: E501
        :type: BTPurchaseInfo
        """

        self._purchase = purchase

    @property
    def user(self):
        """Gets the user of this BTPurchaseUserInfo.  # noqa: E501


        :return: The user of this BTPurchaseUserInfo.  # noqa: E501
        :rtype: BTUserBasicSummaryInfo
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this BTPurchaseUserInfo.


        :param user: The user of this BTPurchaseUserInfo.  # noqa: E501
        :type: BTUserBasicSummaryInfo
        """

        self._user = user

    @property
    def consumed_quantity(self):
        """Gets the consumed_quantity of this BTPurchaseUserInfo.  # noqa: E501


        :return: The consumed_quantity of this BTPurchaseUserInfo.  # noqa: E501
        :rtype: int
        """
        return self._consumed_quantity

    @consumed_quantity.setter
    def consumed_quantity(self, consumed_quantity):
        """Sets the consumed_quantity of this BTPurchaseUserInfo.


        :param consumed_quantity: The consumed_quantity of this BTPurchaseUserInfo.  # noqa: E501
        :type: int
        """

        self._consumed_quantity = consumed_quantity

    @property
    def purchase_state(self):
        """Gets the purchase_state of this BTPurchaseUserInfo.  # noqa: E501


        :return: The purchase_state of this BTPurchaseUserInfo.  # noqa: E501
        :rtype: int
        """
        return self._purchase_state

    @purchase_state.setter
    def purchase_state(self, purchase_state):
        """Sets the purchase_state of this BTPurchaseUserInfo.


        :param purchase_state: The purchase_state of this BTPurchaseUserInfo.  # noqa: E501
        :type: int
        """

        self._purchase_state = purchase_state

    @property
    def name(self):
        """Gets the name of this BTPurchaseUserInfo.  # noqa: E501


        :return: The name of this BTPurchaseUserInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTPurchaseUserInfo.


        :param name: The name of this BTPurchaseUserInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this BTPurchaseUserInfo.  # noqa: E501


        :return: The id of this BTPurchaseUserInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTPurchaseUserInfo.


        :param id: The id of this BTPurchaseUserInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this BTPurchaseUserInfo.  # noqa: E501


        :return: The href of this BTPurchaseUserInfo.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BTPurchaseUserInfo.


        :param href: The href of this BTPurchaseUserInfo.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def view_ref(self):
        """Gets the view_ref of this BTPurchaseUserInfo.  # noqa: E501


        :return: The view_ref of this BTPurchaseUserInfo.  # noqa: E501
        :rtype: str
        """
        return self._view_ref

    @view_ref.setter
    def view_ref(self, view_ref):
        """Sets the view_ref of this BTPurchaseUserInfo.


        :param view_ref: The view_ref of this BTPurchaseUserInfo.  # noqa: E501
        :type: str
        """

        self._view_ref = view_ref

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
        if not isinstance(other, BTPurchaseUserInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other