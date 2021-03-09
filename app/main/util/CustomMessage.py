from enum import Enum


class CustomSuccess(Enum):
    pass


class CustomError(Enum):
    pass


class ResponseStatus(Enum):
    SUCCESS = "Success"
    FAILURE = "Failure"
    PENDING = "Pending"
