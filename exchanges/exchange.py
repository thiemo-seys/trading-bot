# This file contains the abstract class for an exchange
# An exchange is a place where you can buy and sell cryptocurrency assets
# This class is meant to be extended by a specific exchange
# The exchange class communicate by calling an external REST API

from abc import ABC, abstractmethod

class ExchangeAdapter(ABC):
    pass
