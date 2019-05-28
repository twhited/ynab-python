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


class CategoryGroup(object):
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
        'id': 'str',
        'name': 'str',
        'hidden': 'bool',
        'deleted': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'hidden': 'hidden',
        'deleted': 'deleted'
    }

    def __init__(self, id=None, name=None, hidden=None, deleted=None):  # noqa: E501
        """CategoryGroup - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._hidden = None
        self._deleted = None
        self.discriminator = None
        self.id = id
        self.name = name
        self.hidden = hidden
        self.deleted = deleted

    @property
    def id(self):
        """Gets the id of this CategoryGroup.  # noqa: E501


        :return: The id of this CategoryGroup.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CategoryGroup.


        :param id: The id of this CategoryGroup.  # noqa: E501
        :type: str
        """
        

        self._id = id

    @property
    def name(self):
        """Gets the name of this CategoryGroup.  # noqa: E501


        :return: The name of this CategoryGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CategoryGroup.


        :param name: The name of this CategoryGroup.  # noqa: E501
        :type: str
        """
        

        self._name = name

    @property
    def hidden(self):
        """Gets the hidden of this CategoryGroup.  # noqa: E501

        Whether or not the category group is hidden  # noqa: E501

        :return: The hidden of this CategoryGroup.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this CategoryGroup.

        Whether or not the category group is hidden  # noqa: E501

        :param hidden: The hidden of this CategoryGroup.  # noqa: E501
        :type: bool
        """
        

        self._hidden = hidden

    @property
    def deleted(self):
        """Gets the deleted of this CategoryGroup.  # noqa: E501

        Whether or not the category group has been deleted.  Deleted category groups will only be included in delta requests.  # noqa: E501

        :return: The deleted of this CategoryGroup.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this CategoryGroup.

        Whether or not the category group has been deleted.  Deleted category groups will only be included in delta requests.  # noqa: E501

        :param deleted: The deleted of this CategoryGroup.  # noqa: E501
        :type: bool
        """
        

        self._deleted = deleted

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
        if issubclass(CategoryGroup, dict):
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
        if not isinstance(other, CategoryGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
