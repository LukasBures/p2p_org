import argparse
import logging
from typing import Final

from pandas import DataFrame

from analysis.defi_analysis import DefiAnalysis
from analysis.transaction_analysis import TransactionAnalysis
from common.logging_setup import logging_setup
from data_providers.etherscan_provider import EtherscanProvider
from web3 import Web3
from eth_typing import ChecksumAddress


# Ethereum address for analysis (constant)
ADDRESS: Final[ChecksumAddress] = Web3.to_checksum_address("0x99FD1378ca799ED6772Fe7bCDC9B30B389518962")


def main(address: ChecksumAddress) -> None:
    """
    Executes the main analysis workflow.

    Retrieves and analyzes Ethereum transaction data for a given address.

    @param address: Ethereum address for data retrieval and analysis.
    @return: None. Outputs results via logging.
    """
    logging_setup()

    logging.info(f"Retrieving data for address: {address} ...")
    transactions: DataFrame = EtherscanProvider(address=address).get_transactions()

    logging.info("Analyzing transactions ...")
    txs_analysis = TransactionAnalysis().get_analysis(transactions, ADDRESS)
    defi_analysis = DefiAnalysis().get_analysis(transactions, ADDRESS)

    logging.info("Transaction Analysis:")
    [logging.info(f"{k}: {v}") for k, v in txs_analysis.items()]

    logging.info("DeFi Analysis:")
    [logging.info(f"{k}: {v}") for k, v in defi_analysis.items()]


if __name__ == "__main__":
    """
    Script entry point.

    Parses command-line arguments to specify Ethereum address.
    Executes main function using the parsed address.
    """
    parser = argparse.ArgumentParser(description="Ethereum transaction analysis tool.")
    parser.add_argument("--address", help="Ethereum address to analyze", default=ADDRESS)

    args = parser.parse_args()
    main(address=Web3.to_checksum_address(args.address))
