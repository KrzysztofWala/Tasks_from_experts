"""Exceptions for DBPool."""

class ConnectionMissingInPool(Exception):
    pass

class ConnectionFromOutsidePool(Exception):
    pass