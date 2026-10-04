#!/usr/bin/python3
"""Module that defines the LockedClass class."""


class LockedClass:
    """Class that only allows the instance attribute first_name."""
    __slots__ = ["first_name"]
