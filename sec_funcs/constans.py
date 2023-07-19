from enum import Enum, unique


@unique
class Order(str, Enum):
    ASC = 'asc'
    DESC = 'desc'
