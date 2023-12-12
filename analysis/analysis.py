from abc import ABC, abstractmethod

from pandas import DataFrame


class Analysis(ABC):
    """
    Abstract base class for performing different types of analyses on transaction data.

    This class defines a structure that all specific analysis classes should follow,
    ensuring consistency and providing a clear template for implementation.
    """

    @abstractmethod
    def __init__(self) -> None:
        """
        Initializes the Analysis class.

        As an abstract method, it should be implemented by all subclasses
        to initialize any necessary attributes specific to the analysis type.
        """
        pass

    @abstractmethod
    def get_analysis(self, transactions: DataFrame, analysed_address: str) -> dict:
        """
        Abstract method to perform analysis on transaction data.

        This method should be implemented by subclasses to provide specific analysis
        based on the transaction data and the address being analyzed.

        Args:
            transactions (DataFrame): The DataFrame containing transaction data.
            analysed_address (str): The Ethereum address whose transactions are being analyzed.

        Returns:
            dict: A dictionary containing the results of the analysis.
        """
        pass
