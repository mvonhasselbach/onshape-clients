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


class Card(object):
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
        'id': 'str',
        'object': 'str',
        'account': 'str',
        'customer': 'str',
        'metadata': 'dict(str, str)',
        'address_city': 'str',
        'address_country': 'str',
        'address_line1': 'str',
        'address_line1_check': 'str',
        'address_line2': 'str',
        'address_state': 'str',
        'address_zip': 'str',
        'address_zip_check': 'str',
        'available_payout_methods': 'list[str]',
        'brand': 'str',
        'country': 'str',
        'currency': 'str',
        'cvc_check': 'str',
        'default_for_currency': 'bool',
        'dynamic_last4': 'str',
        'exp_month': 'int',
        'exp_year': 'int',
        'fingerprint': 'str',
        'funding': 'str',
        'last4': 'str',
        'name': 'str',
        'recipient': 'str',
        'status': 'str',
        'three_d_secure': 'ThreeDSecure',
        'tokenization_method': 'str',
        'description': 'str',
        'iin': 'str',
        'issuer': 'str',
        'type': 'str',
        'instance_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'object': 'object',
        'account': 'account',
        'customer': 'customer',
        'metadata': 'metadata',
        'address_city': 'addressCity',
        'address_country': 'addressCountry',
        'address_line1': 'addressLine1',
        'address_line1_check': 'addressLine1Check',
        'address_line2': 'addressLine2',
        'address_state': 'addressState',
        'address_zip': 'addressZip',
        'address_zip_check': 'addressZipCheck',
        'available_payout_methods': 'availablePayoutMethods',
        'brand': 'brand',
        'country': 'country',
        'currency': 'currency',
        'cvc_check': 'cvcCheck',
        'default_for_currency': 'defaultForCurrency',
        'dynamic_last4': 'dynamicLast4',
        'exp_month': 'expMonth',
        'exp_year': 'expYear',
        'fingerprint': 'fingerprint',
        'funding': 'funding',
        'last4': 'last4',
        'name': 'name',
        'recipient': 'recipient',
        'status': 'status',
        'three_d_secure': 'threeDSecure',
        'tokenization_method': 'tokenizationMethod',
        'description': 'description',
        'iin': 'iin',
        'issuer': 'issuer',
        'type': 'type',
        'instance_url': 'instanceURL'
    }

    def __init__(self, id=None, object=None, account=None, customer=None, metadata=None, address_city=None, address_country=None, address_line1=None, address_line1_check=None, address_line2=None, address_state=None, address_zip=None, address_zip_check=None, available_payout_methods=None, brand=None, country=None, currency=None, cvc_check=None, default_for_currency=None, dynamic_last4=None, exp_month=None, exp_year=None, fingerprint=None, funding=None, last4=None, name=None, recipient=None, status=None, three_d_secure=None, tokenization_method=None, description=None, iin=None, issuer=None, type=None, instance_url=None):  # noqa: E501
        """Card - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._object = None
        self._account = None
        self._customer = None
        self._metadata = None
        self._address_city = None
        self._address_country = None
        self._address_line1 = None
        self._address_line1_check = None
        self._address_line2 = None
        self._address_state = None
        self._address_zip = None
        self._address_zip_check = None
        self._available_payout_methods = None
        self._brand = None
        self._country = None
        self._currency = None
        self._cvc_check = None
        self._default_for_currency = None
        self._dynamic_last4 = None
        self._exp_month = None
        self._exp_year = None
        self._fingerprint = None
        self._funding = None
        self._last4 = None
        self._name = None
        self._recipient = None
        self._status = None
        self._three_d_secure = None
        self._tokenization_method = None
        self._description = None
        self._iin = None
        self._issuer = None
        self._type = None
        self._instance_url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if object is not None:
            self.object = object
        if account is not None:
            self.account = account
        if customer is not None:
            self.customer = customer
        if metadata is not None:
            self.metadata = metadata
        if address_city is not None:
            self.address_city = address_city
        if address_country is not None:
            self.address_country = address_country
        if address_line1 is not None:
            self.address_line1 = address_line1
        if address_line1_check is not None:
            self.address_line1_check = address_line1_check
        if address_line2 is not None:
            self.address_line2 = address_line2
        if address_state is not None:
            self.address_state = address_state
        if address_zip is not None:
            self.address_zip = address_zip
        if address_zip_check is not None:
            self.address_zip_check = address_zip_check
        if available_payout_methods is not None:
            self.available_payout_methods = available_payout_methods
        if brand is not None:
            self.brand = brand
        if country is not None:
            self.country = country
        if currency is not None:
            self.currency = currency
        if cvc_check is not None:
            self.cvc_check = cvc_check
        if default_for_currency is not None:
            self.default_for_currency = default_for_currency
        if dynamic_last4 is not None:
            self.dynamic_last4 = dynamic_last4
        if exp_month is not None:
            self.exp_month = exp_month
        if exp_year is not None:
            self.exp_year = exp_year
        if fingerprint is not None:
            self.fingerprint = fingerprint
        if funding is not None:
            self.funding = funding
        if last4 is not None:
            self.last4 = last4
        if name is not None:
            self.name = name
        if recipient is not None:
            self.recipient = recipient
        if status is not None:
            self.status = status
        if three_d_secure is not None:
            self.three_d_secure = three_d_secure
        if tokenization_method is not None:
            self.tokenization_method = tokenization_method
        if description is not None:
            self.description = description
        if iin is not None:
            self.iin = iin
        if issuer is not None:
            self.issuer = issuer
        if type is not None:
            self.type = type
        if instance_url is not None:
            self.instance_url = instance_url

    @property
    def id(self):
        """Gets the id of this Card.  # noqa: E501


        :return: The id of this Card.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Card.


        :param id: The id of this Card.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def object(self):
        """Gets the object of this Card.  # noqa: E501


        :return: The object of this Card.  # noqa: E501
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this Card.


        :param object: The object of this Card.  # noqa: E501
        :type: str
        """

        self._object = object

    @property
    def account(self):
        """Gets the account of this Card.  # noqa: E501


        :return: The account of this Card.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this Card.


        :param account: The account of this Card.  # noqa: E501
        :type: str
        """

        self._account = account

    @property
    def customer(self):
        """Gets the customer of this Card.  # noqa: E501


        :return: The customer of this Card.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this Card.


        :param customer: The customer of this Card.  # noqa: E501
        :type: str
        """

        self._customer = customer

    @property
    def metadata(self):
        """Gets the metadata of this Card.  # noqa: E501


        :return: The metadata of this Card.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Card.


        :param metadata: The metadata of this Card.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def address_city(self):
        """Gets the address_city of this Card.  # noqa: E501


        :return: The address_city of this Card.  # noqa: E501
        :rtype: str
        """
        return self._address_city

    @address_city.setter
    def address_city(self, address_city):
        """Sets the address_city of this Card.


        :param address_city: The address_city of this Card.  # noqa: E501
        :type: str
        """

        self._address_city = address_city

    @property
    def address_country(self):
        """Gets the address_country of this Card.  # noqa: E501


        :return: The address_country of this Card.  # noqa: E501
        :rtype: str
        """
        return self._address_country

    @address_country.setter
    def address_country(self, address_country):
        """Sets the address_country of this Card.


        :param address_country: The address_country of this Card.  # noqa: E501
        :type: str
        """

        self._address_country = address_country

    @property
    def address_line1(self):
        """Gets the address_line1 of this Card.  # noqa: E501


        :return: The address_line1 of this Card.  # noqa: E501
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """Sets the address_line1 of this Card.


        :param address_line1: The address_line1 of this Card.  # noqa: E501
        :type: str
        """

        self._address_line1 = address_line1

    @property
    def address_line1_check(self):
        """Gets the address_line1_check of this Card.  # noqa: E501


        :return: The address_line1_check of this Card.  # noqa: E501
        :rtype: str
        """
        return self._address_line1_check

    @address_line1_check.setter
    def address_line1_check(self, address_line1_check):
        """Sets the address_line1_check of this Card.


        :param address_line1_check: The address_line1_check of this Card.  # noqa: E501
        :type: str
        """

        self._address_line1_check = address_line1_check

    @property
    def address_line2(self):
        """Gets the address_line2 of this Card.  # noqa: E501


        :return: The address_line2 of this Card.  # noqa: E501
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """Sets the address_line2 of this Card.


        :param address_line2: The address_line2 of this Card.  # noqa: E501
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def address_state(self):
        """Gets the address_state of this Card.  # noqa: E501


        :return: The address_state of this Card.  # noqa: E501
        :rtype: str
        """
        return self._address_state

    @address_state.setter
    def address_state(self, address_state):
        """Sets the address_state of this Card.


        :param address_state: The address_state of this Card.  # noqa: E501
        :type: str
        """

        self._address_state = address_state

    @property
    def address_zip(self):
        """Gets the address_zip of this Card.  # noqa: E501


        :return: The address_zip of this Card.  # noqa: E501
        :rtype: str
        """
        return self._address_zip

    @address_zip.setter
    def address_zip(self, address_zip):
        """Sets the address_zip of this Card.


        :param address_zip: The address_zip of this Card.  # noqa: E501
        :type: str
        """

        self._address_zip = address_zip

    @property
    def address_zip_check(self):
        """Gets the address_zip_check of this Card.  # noqa: E501


        :return: The address_zip_check of this Card.  # noqa: E501
        :rtype: str
        """
        return self._address_zip_check

    @address_zip_check.setter
    def address_zip_check(self, address_zip_check):
        """Sets the address_zip_check of this Card.


        :param address_zip_check: The address_zip_check of this Card.  # noqa: E501
        :type: str
        """

        self._address_zip_check = address_zip_check

    @property
    def available_payout_methods(self):
        """Gets the available_payout_methods of this Card.  # noqa: E501


        :return: The available_payout_methods of this Card.  # noqa: E501
        :rtype: list[str]
        """
        return self._available_payout_methods

    @available_payout_methods.setter
    def available_payout_methods(self, available_payout_methods):
        """Sets the available_payout_methods of this Card.


        :param available_payout_methods: The available_payout_methods of this Card.  # noqa: E501
        :type: list[str]
        """

        self._available_payout_methods = available_payout_methods

    @property
    def brand(self):
        """Gets the brand of this Card.  # noqa: E501


        :return: The brand of this Card.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this Card.


        :param brand: The brand of this Card.  # noqa: E501
        :type: str
        """

        self._brand = brand

    @property
    def country(self):
        """Gets the country of this Card.  # noqa: E501


        :return: The country of this Card.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Card.


        :param country: The country of this Card.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def currency(self):
        """Gets the currency of this Card.  # noqa: E501


        :return: The currency of this Card.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Card.


        :param currency: The currency of this Card.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def cvc_check(self):
        """Gets the cvc_check of this Card.  # noqa: E501


        :return: The cvc_check of this Card.  # noqa: E501
        :rtype: str
        """
        return self._cvc_check

    @cvc_check.setter
    def cvc_check(self, cvc_check):
        """Sets the cvc_check of this Card.


        :param cvc_check: The cvc_check of this Card.  # noqa: E501
        :type: str
        """

        self._cvc_check = cvc_check

    @property
    def default_for_currency(self):
        """Gets the default_for_currency of this Card.  # noqa: E501


        :return: The default_for_currency of this Card.  # noqa: E501
        :rtype: bool
        """
        return self._default_for_currency

    @default_for_currency.setter
    def default_for_currency(self, default_for_currency):
        """Sets the default_for_currency of this Card.


        :param default_for_currency: The default_for_currency of this Card.  # noqa: E501
        :type: bool
        """

        self._default_for_currency = default_for_currency

    @property
    def dynamic_last4(self):
        """Gets the dynamic_last4 of this Card.  # noqa: E501


        :return: The dynamic_last4 of this Card.  # noqa: E501
        :rtype: str
        """
        return self._dynamic_last4

    @dynamic_last4.setter
    def dynamic_last4(self, dynamic_last4):
        """Sets the dynamic_last4 of this Card.


        :param dynamic_last4: The dynamic_last4 of this Card.  # noqa: E501
        :type: str
        """

        self._dynamic_last4 = dynamic_last4

    @property
    def exp_month(self):
        """Gets the exp_month of this Card.  # noqa: E501


        :return: The exp_month of this Card.  # noqa: E501
        :rtype: int
        """
        return self._exp_month

    @exp_month.setter
    def exp_month(self, exp_month):
        """Sets the exp_month of this Card.


        :param exp_month: The exp_month of this Card.  # noqa: E501
        :type: int
        """

        self._exp_month = exp_month

    @property
    def exp_year(self):
        """Gets the exp_year of this Card.  # noqa: E501


        :return: The exp_year of this Card.  # noqa: E501
        :rtype: int
        """
        return self._exp_year

    @exp_year.setter
    def exp_year(self, exp_year):
        """Sets the exp_year of this Card.


        :param exp_year: The exp_year of this Card.  # noqa: E501
        :type: int
        """

        self._exp_year = exp_year

    @property
    def fingerprint(self):
        """Gets the fingerprint of this Card.  # noqa: E501


        :return: The fingerprint of this Card.  # noqa: E501
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this Card.


        :param fingerprint: The fingerprint of this Card.  # noqa: E501
        :type: str
        """

        self._fingerprint = fingerprint

    @property
    def funding(self):
        """Gets the funding of this Card.  # noqa: E501


        :return: The funding of this Card.  # noqa: E501
        :rtype: str
        """
        return self._funding

    @funding.setter
    def funding(self, funding):
        """Sets the funding of this Card.


        :param funding: The funding of this Card.  # noqa: E501
        :type: str
        """

        self._funding = funding

    @property
    def last4(self):
        """Gets the last4 of this Card.  # noqa: E501


        :return: The last4 of this Card.  # noqa: E501
        :rtype: str
        """
        return self._last4

    @last4.setter
    def last4(self, last4):
        """Sets the last4 of this Card.


        :param last4: The last4 of this Card.  # noqa: E501
        :type: str
        """

        self._last4 = last4

    @property
    def name(self):
        """Gets the name of this Card.  # noqa: E501


        :return: The name of this Card.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Card.


        :param name: The name of this Card.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def recipient(self):
        """Gets the recipient of this Card.  # noqa: E501


        :return: The recipient of this Card.  # noqa: E501
        :rtype: str
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """Sets the recipient of this Card.


        :param recipient: The recipient of this Card.  # noqa: E501
        :type: str
        """

        self._recipient = recipient

    @property
    def status(self):
        """Gets the status of this Card.  # noqa: E501


        :return: The status of this Card.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Card.


        :param status: The status of this Card.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def three_d_secure(self):
        """Gets the three_d_secure of this Card.  # noqa: E501


        :return: The three_d_secure of this Card.  # noqa: E501
        :rtype: ThreeDSecure
        """
        return self._three_d_secure

    @three_d_secure.setter
    def three_d_secure(self, three_d_secure):
        """Sets the three_d_secure of this Card.


        :param three_d_secure: The three_d_secure of this Card.  # noqa: E501
        :type: ThreeDSecure
        """

        self._three_d_secure = three_d_secure

    @property
    def tokenization_method(self):
        """Gets the tokenization_method of this Card.  # noqa: E501


        :return: The tokenization_method of this Card.  # noqa: E501
        :rtype: str
        """
        return self._tokenization_method

    @tokenization_method.setter
    def tokenization_method(self, tokenization_method):
        """Sets the tokenization_method of this Card.


        :param tokenization_method: The tokenization_method of this Card.  # noqa: E501
        :type: str
        """

        self._tokenization_method = tokenization_method

    @property
    def description(self):
        """Gets the description of this Card.  # noqa: E501


        :return: The description of this Card.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Card.


        :param description: The description of this Card.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def iin(self):
        """Gets the iin of this Card.  # noqa: E501


        :return: The iin of this Card.  # noqa: E501
        :rtype: str
        """
        return self._iin

    @iin.setter
    def iin(self, iin):
        """Sets the iin of this Card.


        :param iin: The iin of this Card.  # noqa: E501
        :type: str
        """

        self._iin = iin

    @property
    def issuer(self):
        """Gets the issuer of this Card.  # noqa: E501


        :return: The issuer of this Card.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this Card.


        :param issuer: The issuer of this Card.  # noqa: E501
        :type: str
        """

        self._issuer = issuer

    @property
    def type(self):
        """Gets the type of this Card.  # noqa: E501


        :return: The type of this Card.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Card.


        :param type: The type of this Card.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def instance_url(self):
        """Gets the instance_url of this Card.  # noqa: E501


        :return: The instance_url of this Card.  # noqa: E501
        :rtype: str
        """
        return self._instance_url

    @instance_url.setter
    def instance_url(self, instance_url):
        """Sets the instance_url of this Card.


        :param instance_url: The instance_url of this Card.  # noqa: E501
        :type: str
        """

        self._instance_url = instance_url

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
        if not isinstance(other, Card):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
