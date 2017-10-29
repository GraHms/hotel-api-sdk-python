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


class ApiReviewFilter(object):
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
        'type': 'str',
        'min_rate': 'float',
        'max_rate': 'float',
        'min_review_count': 'int'
    }

    attribute_map = {
        'type': 'type',
        'min_rate': 'minRate',
        'max_rate': 'maxRate',
        'min_review_count': 'minReviewCount'
    }

    def __init__(self, type=None, min_rate=None, max_rate=None, min_review_count=None):
        """
        ApiReviewFilter - a model defined in Swagger
        """

        self._type = None
        self._min_rate = None
        self._max_rate = None
        self._min_review_count = None

        self.type = type
        if min_rate is not None:
          self.min_rate = min_rate
        if max_rate is not None:
          self.max_rate = max_rate
        if min_review_count is not None:
          self.min_review_count = min_review_count

    @property
    def type(self):
        """
        Gets the type of this ApiReviewFilter.

        :return: The type of this ApiReviewFilter.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ApiReviewFilter.

        :param type: The type of this ApiReviewFilter.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")
        allowed_values = ["TRIPADVISOR", "HOTELBEDS"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def min_rate(self):
        """
        Gets the min_rate of this ApiReviewFilter.

        :return: The min_rate of this ApiReviewFilter.
        :rtype: float
        """
        return self._min_rate

    @min_rate.setter
    def min_rate(self, min_rate):
        """
        Sets the min_rate of this ApiReviewFilter.

        :param min_rate: The min_rate of this ApiReviewFilter.
        :type: float
        """
        if min_rate is not None and min_rate > 5:
            raise ValueError("Invalid value for `min_rate`, must be a value less than or equal to `5`")
        if min_rate is not None and min_rate < 0:
            raise ValueError("Invalid value for `min_rate`, must be a value greater than or equal to `0`")

        self._min_rate = min_rate

    @property
    def max_rate(self):
        """
        Gets the max_rate of this ApiReviewFilter.

        :return: The max_rate of this ApiReviewFilter.
        :rtype: float
        """
        return self._max_rate

    @max_rate.setter
    def max_rate(self, max_rate):
        """
        Sets the max_rate of this ApiReviewFilter.

        :param max_rate: The max_rate of this ApiReviewFilter.
        :type: float
        """
        if max_rate is not None and max_rate > 5:
            raise ValueError("Invalid value for `max_rate`, must be a value less than or equal to `5`")
        if max_rate is not None and max_rate < 0:
            raise ValueError("Invalid value for `max_rate`, must be a value greater than or equal to `0`")

        self._max_rate = max_rate

    @property
    def min_review_count(self):
        """
        Gets the min_review_count of this ApiReviewFilter.

        :return: The min_review_count of this ApiReviewFilter.
        :rtype: int
        """
        return self._min_review_count

    @min_review_count.setter
    def min_review_count(self, min_review_count):
        """
        Sets the min_review_count of this ApiReviewFilter.

        :param min_review_count: The min_review_count of this ApiReviewFilter.
        :type: int
        """

        self._min_review_count = min_review_count

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
        if not isinstance(other, ApiReviewFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other