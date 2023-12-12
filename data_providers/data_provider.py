from abc import ABC, abstractmethod
from pandas import DataFrame
from eth_typing import ChecksumAddress


class DataProvider(ABC):
    """
    Abstract base class for data providers that fetch transaction data.

    This class defines the structure for data providers, ensuring consistent
    implementation for different data sources.
    """

    def __init__(self, address: ChecksumAddress) -> None:
        """
        Initializes the DataProvider with an Ethereum address.

        Args:
            address (ChecksumAddress): The Ethereum address for which transaction data will be retrieved.
        """
        self._address: ChecksumAddress = address

    @abstractmethod
    def get_transactions(self) -> DataFrame:
        """
        Abstract method to fetch transaction data.

        To be implemented by subclasses to retrieve transaction data for the specified Ethereum address.

        Returns:
            DataFrame: A DataFrame containing the transaction data.
        """
        pass
