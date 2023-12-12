import os
from pathlib import Path

import pandas as pd
import requests
from pandas import DataFrame
from web3 import Web3

from common.config import ETHERSCAN_API_KEY
from data_providers.data_provider import DataProvider
from eth_typing import ChecksumAddress


class EtherscanProvider(DataProvider):
    """
    A data provider class for fetching Ethereum transaction data from Etherscan.

    Extends the DataProvider abstract base class, tailored to interact with the Etherscan API.
    """

    def __init__(self, address: ChecksumAddress) -> None:
        """
        Initializes the EtherscanProvider with an Ethereum address.

        Validates the Ethereum address and sets up paths and URLs for data retrieval.

        Args:
            address (ChecksumAddress): The Ethereum address for which transaction data will be retrieved.

        Raises:
            ValueError: If the provided address is not a valid Ethereum address.
        """
        if not Web3.is_address(address):
            raise ValueError("Invalid Ethereum address")
        super().__init__(address=address)
        self._address: ChecksumAddress = Web3.to_checksum_address(address)
        self._txs_data_path: Path = Path(f"./data/txs_{self._address}.csv")
        self._base_url: str = "https://api.etherscan.io"

    def _fetch_transactions(self) -> dict:
        """
        Fetches transactions for the specified address from Etherscan.

        Returns:
            dict: A dictionary containing the transaction data from Etherscan API.
        """
        url: str = (
            f"{self._base_url}/api?"
            f"module=account&"
            f"action=txlist&"
            f"address={self._address}&"
            f"startblock=0&"
            f"endblock=99999999&"
            f"sort=asc&"
            f"apikey={ETHERSCAN_API_KEY}"
        )

        response = requests.get(url)
        return response.json() if response.status_code == 200 else {}

    def get_transactions(self) -> DataFrame:
        """
        Retrieves Ethereum transaction data either from a local CSV file or the Etherscan API.

        If the data is not locally available, it fetches data from Etherscan and saves it locally.

        Returns:
            DataFrame: A DataFrame containing the Ethereum transaction data.
        """
        if os.path.exists(self._txs_data_path):
            return pd.read_csv(self._txs_data_path)
        else:
            data = self._fetch_transactions()
            if data and data["status"] == "1":
                transactions = data["result"]
                df = DataFrame(transactions)
                df["from"] = df["from"].apply(Web3.to_checksum_address)
                df["to"] = df["to"].apply(Web3.to_checksum_address)
                df.to_csv(self._txs_data_path, index=False)
                return df
            else:
                return DataFrame()
