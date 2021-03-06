# coding: utf-8

"""
    APITUDE BOOKINGAPI

    BOOKINGAPI is designed to book hotels in real time as fast as in two steps. It covers the complete booking process; it allows generating lists of hotels, confirming bookings, getting lists of bookings, obtaining booking information, making cancellations and modify existing bookings.   BOOKINGAPI works in combination with CONTENTAPI to obtain content information from the hotels, such as pictures, description, facilities, services, etc. Please refer to the ContentAPI documentation and IO/DOCS for related information.    BOOKINGAPI has been designed for a two steps confirmation, but due the the complexity of client and providers systems a third method has been designed.

    OpenAPI spec version: 1.0
    Contact: apitude@hotelbeds.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ApiRateSupplement(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code': 'str',
        'name': 'str',
        '_from': 'date',
        'to': 'date',
        'amount': 'float',
        'nights': 'int',
        'pax_number': 'int'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name',
        '_from': 'from',
        'to': 'to',
        'amount': 'amount',
        'nights': 'nights',
        'pax_number': 'paxNumber'
    }

    def __init__(self, code=None, name=None, _from=None, to=None, amount=None, nights=None, pax_number=None):
        """
        ApiRateSupplement - a model defined in Swagger
        """

        self._code = None
        self._name = None
        self.__from = None
        self._to = None
        self._amount = None
        self._nights = None
        self._pax_number = None

        if code is not None:
          self.code = code
        if name is not None:
          self.name = name
        if _from is not None:
          self._from = _from
        if to is not None:
          self.to = to
        if amount is not None:
          self.amount = amount
        if nights is not None:
          self.nights = nights
        if pax_number is not None:
          self.pax_number = pax_number

    @property
    def code(self):
        """
        Gets the code of this ApiRateSupplement.

        :return: The code of this ApiRateSupplement.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ApiRateSupplement.

        :param code: The code of this ApiRateSupplement.
        :type: str
        """

        self._code = code

    @property
    def name(self):
        """
        Gets the name of this ApiRateSupplement.

        :return: The name of this ApiRateSupplement.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ApiRateSupplement.

        :param name: The name of this ApiRateSupplement.
        :type: str
        """

        self._name = name

    @property
    def _from(self):
        """
        Gets the _from of this ApiRateSupplement.

        :return: The _from of this ApiRateSupplement.
        :rtype: date
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this ApiRateSupplement.

        :param _from: The _from of this ApiRateSupplement.
        :type: date
        """

        self.__from = _from

    @property
    def to(self):
        """
        Gets the to of this ApiRateSupplement.

        :return: The to of this ApiRateSupplement.
        :rtype: date
        """
        return self._to

    @to.setter
    def to(self, to):
        """
        Sets the to of this ApiRateSupplement.

        :param to: The to of this ApiRateSupplement.
        :type: date
        """

        self._to = to

    @property
    def amount(self):
        """
        Gets the amount of this ApiRateSupplement.

        :return: The amount of this ApiRateSupplement.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this ApiRateSupplement.

        :param amount: The amount of this ApiRateSupplement.
        :type: float
        """

        self._amount = amount

    @property
    def nights(self):
        """
        Gets the nights of this ApiRateSupplement.

        :return: The nights of this ApiRateSupplement.
        :rtype: int
        """
        return self._nights

    @nights.setter
    def nights(self, nights):
        """
        Sets the nights of this ApiRateSupplement.

        :param nights: The nights of this ApiRateSupplement.
        :type: int
        """

        self._nights = nights

    @property
    def pax_number(self):
        """
        Gets the pax_number of this ApiRateSupplement.

        :return: The pax_number of this ApiRateSupplement.
        :rtype: int
        """
        return self._pax_number

    @pax_number.setter
    def pax_number(self, pax_number):
        """
        Sets the pax_number of this ApiRateSupplement.

        :param pax_number: The pax_number of this ApiRateSupplement.
        :type: int
        """

        self._pax_number = pax_number

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ApiRateSupplement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
