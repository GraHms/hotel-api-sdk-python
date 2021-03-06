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


class ApiDestination(object):
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
        'zone': 'int'
    }

    attribute_map = {
        'code': 'code',
        'zone': 'zone'
    }

    def __init__(self, code=None, zone=None):
        """
        ApiDestination - a model defined in Swagger
        """

        self._code = None
        self._zone = None

        self.code = code
        if zone is not None:
          self.zone = zone

    @property
    def code(self):
        """
        Gets the code of this ApiDestination.

        :return: The code of this ApiDestination.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ApiDestination.

        :param code: The code of this ApiDestination.
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")
        if code is not None and len(code) > 3:
            raise ValueError("Invalid value for `code`, length must be less than or equal to `3`")
        if code is not None and len(code) < 1:
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `1`")

        self._code = code

    @property
    def zone(self):
        """
        Gets the zone of this ApiDestination.

        :return: The zone of this ApiDestination.
        :rtype: int
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """
        Sets the zone of this ApiDestination.

        :param zone: The zone of this ApiDestination.
        :type: int
        """

        self._zone = zone

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
        if not isinstance(other, ApiDestination):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
