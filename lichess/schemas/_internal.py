"""
Internal for managing JSON
"""

import json


class JsonSerializable:
    """
    Subclasses of this class are guaranteed to be able to be converted to JSON format.
    All subclasses of this class must override `to_json`.
    """

    def to_json(self):
        """
        Returns a JSON string representation of this class.

        :meta private:

        This function must be overridden by subclasses.
        :return: a JSON formatted string.
        """
        raise NotImplementedError


class Dictionaryable:
    """
    Subclasses of this class are guaranteed to be able to be converted to dictionary.
    All subclasses of this class must override `to_dict`.
    """

    def to_dict(self):
        """
        Returns a DICT with class field values

        :meta private:

        This function must be overridden by subclasses.
        :return: a DICT
        """
        raise NotImplementedError


class JsonDeserializable:
    """
    Subclasses of this class are guaranteed to be able to be created from a json-style dict or json formatted string.
    All subclasses of this class must override `de_json`.
    """

    @classmethod
    def de_json(cls, json_string):
        """
        Returns an instance of this class from the given json dict or string.

        :meta private:

        This function must be overridden by subclasses.
        :return: an instance of this class created from the given json dict or string.
        """
        raise NotImplementedError

    @staticmethod
    def check_json(json_type: str | dict, dict_copy=True):
        """
        Checks whether `json_type` is a dict or a string. If it is already a `dict`, it is returned as-is.
        If it is not, it is converted to a dict by means of `json.loads(json_type)`

        :meta private:

        :param json_type: input json or parsed dict
        :param dict_copy: if dict is passed and it is changed outside - should be True!
        :return: Dictionary parsed from json or original dict
        """
        if isinstance(json_type, dict):
            return json_type.copy() if dict_copy else json_type
        elif isinstance(json_type, str):
            return json.loads(json_type)
        else:
            raise ValueError("json_type should be a json dict or string.")

    def __str__(self):
        d = {x: y.__dict__ if hasattr(y, "__dict__") else y for x, y in self.__dict__.items()}
        return str(d)


__all__ = ["JsonSerializable", "Dictionaryable", "JsonDeserializable"]
