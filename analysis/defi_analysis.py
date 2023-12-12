from typing import Any, Optional

from pandas import DataFrame

from analysis.analysis import Analysis


class DefiAnalysis(Analysis):
    """
    A class for analyzing DeFi-related transactions.

    This class extends the Analysis base class and focuses on transactions
    related to decentralized finance (DeFi) activities.

    Attributes:
        _top_n_addresses (int): The number of top addresses to analyze.
        _defi_functions (list[str]): List of function names typical in DeFi operations.
    """

    def __init__(self, top_n_addresses: Optional[int] = None) -> None:
        """
        Initializes the DefiAnalysis class with optional top N addresses parameter.

        Args:
            top_n_addresses (Optional[int]): The number of top addresses to include in the analysis.
                                            Defaults to 100 if not specified.
        """
        self._top_n_addresses = top_n_addresses if top_n_addresses else 100

        # List of common DeFi-related function names
        self._defi_functions = [
            "swap",
            "addLiquidity",
            "removeLiquidity",
            "borrow",
            "repayBorrow",
            "stake",
            "unstake",
            "mint",
            "burn",
            "enter",
            "leave",
            "claimRewards",
            "getReward",
            "deposit",
            "withdraw",
            "openPosition",
            "closePosition",
            "liquidate",
            "deposit",
        ]

    def get_analysis(self, transactions: DataFrame, analysed_address: str) -> dict[str, Any]:
        """
        Performs analysis on DeFi-related transactions.

        Filters and analyzes transactions based on DeFi-related functions and calculates various metrics.

        Args:
            transactions (DataFrame): DataFrame containing transaction data.
            analysed_address (str): The Ethereum address to analyze.

        Returns:
            dict: A dictionary containing various insights from the DeFi transactions analysis.
        """
        # Filtering transactions for DeFi-related activities
        defi_transactions = transactions[
            transactions["functionName"].str.contains("|".join(self._defi_functions), na=False)
        ]

        # Calculating various metrics for DeFi transactions
        defi_inflow = defi_transactions[defi_transactions["to"] == analysed_address]["value"].sum()
        defi_outflow = defi_transactions[defi_transactions["from"] == analysed_address]["value"].sum()
        defi_total_transactions = len(defi_transactions)
        defi_in_transactions = len(defi_transactions[defi_transactions["to"] == analysed_address])
        defi_out_transactions = len(defi_transactions[defi_transactions["from"] == analysed_address])
        defi_avg_inflow_value = defi_inflow / defi_in_transactions if defi_in_transactions > 0 else 0
        defi_avg_outflow_value = defi_outflow / defi_out_transactions if defi_out_transactions > 0 else 0

        # Frequency analysis by month
        defi_transactions_per_month = (
            defi_transactions["date"]
            .groupby([defi_transactions.date.dt.year, defi_transactions.date.dt.month])
            .agg("count")
        )

        # Returning summarized DeFi insights
        return {
            "DeFi Total Transactions": defi_total_transactions,
            "DeFi Inflow Transactions": defi_in_transactions,
            "DeFi Outflow Transactions": defi_out_transactions,
            "DeFi Total Inflow (ETH)": defi_inflow,
            "DeFi Total Outflow (ETH)": defi_outflow,
            "DeFi Average Inflow Value (ETH)": defi_avg_inflow_value,
            "DeFi Average Outflow Value (ETH)": defi_avg_outflow_value,
            "DeFi Transactions Per Month": defi_transactions_per_month,
        }
