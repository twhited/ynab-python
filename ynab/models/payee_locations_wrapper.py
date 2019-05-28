# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from ynab.models.payee_location import PayeeLocation  # noqa: F401,E501


class PayeeLocationsWrapper(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'payee_locations': 'list[PayeeLocation]'
    }

    attribute_map = {
        'payee_locations': 'payee_locations'
    }

    def __init__(self, payee_locations=None):  # noqa: E501
        """PayeeLocationsWrapper - a model defined in Swagger"""  # noqa: E501
        self._payee_locations = None
        self.discriminator = None
        self.payee_locations = payee_locations

    @property
    def payee_locations(self):
        """Gets the payee_locations of this PayeeLocationsWrapper.  # noqa: E501


        :return: The payee_locations of this PayeeLocationsWrapper.  # noqa: E501
        :rtype: list[PayeeLocation]
        """
        return self._payee_locations

    @payee_locations.setter
    def payee_locations(self, payee_locations):
        """Sets the payee_locations of this PayeeLocationsWrapper.


        :param payee_locations: The payee_locations of this PayeeLocationsWrapper.  # noqa: E501
        :type: list[PayeeLocation]
        """
        

        self._payee_locations = payee_locations

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(PayeeLocationsWrapper, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PayeeLocationsWrapper):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
