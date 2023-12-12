from typing import Any, Optional

import pandas as pd
from pandas import DataFrame, Series

from analysis.analysis import Analysis


class TransactionAnalysis(Analysis):
    """
    A class for conducting analysis on Ethereum transaction data.

    Extends the Analysis base class, focusing on metrics like inflow,
    outflow, average transaction values, and frequency analysis of transactions.
    """

    def __init__(self) -> None:
        """
        Initializes the TransactionAnalysis class.
        """
        super().__init__()

    def get_analysis(self, transactions: DataFrame, analysed_address: str) -> dict[str, Any]:
        """
        Performs detailed analysis on Ethereum transactions.

        Args:
            transactions (DataFrame): DataFrame containing transaction data.
            analysed_address (str): Ethereum address for which the analysis is conducted.

        Returns:
            Dict[str, Optional[float]]: A dictionary containing key insights and metrics
                                         from the transaction analysis.
        """
        # Preprocessing and data conversion
        transactions["date"] = pd.to_datetime(transactions["timeStamp"], unit="s")
        transactions["value"] = transactions["value"].astype(float) / 10**18  # Convert from Wei to Ether

        # Analysis of inflow and outflow
        inflow: float = transactions[transactions["to"] == analysed_address]["value"].sum()
        outflow: float = transactions[transactions["from"] == analysed_address]["value"].sum()

        # Counting transactions and calculating averages
        total_transactions: int = len(transactions)
        in_transactions: int = len(transactions[transactions["to"] == analysed_address])
        out_transactions: int = len(transactions[transactions["from"] == analysed_address])
        avg_inflow_value: Optional[float] = inflow / in_transactions if in_transactions > 0 else 0
        avg_outflow_value: Optional[float] = outflow / out_transactions if out_transactions > 0 else 0

        # Frequency and error rate analysis
        transactions_per_month: Series = (
            transactions["date"].groupby([transactions.date.dt.year, transactions.date.dt.month]).agg("count")
        )
        error_rate: float = len(transactions[transactions["isError"] == 1]) / total_transactions

        # Analyzing "claim reward" calls
        claim_reward_pattern: str = "claim|reward"
        claim_rewards_transactions: DataFrame = transactions[
            transactions["functionName"].str.contains(claim_reward_pattern, case=False, na=False)
        ]
        claim_reward_count: int = len(claim_rewards_transactions)
        total_claimed_rewards: float = claim_rewards_transactions["value"].sum()

        # Compiling insights
        financial_strategy_insights: dict[str, Optional[float]] = {
            "Total Transactions": total_transactions,
            "Inflow Transactions": in_transactions,
            "Outflow Transactions": out_transactions,
            "Total Inflow (ETH)": inflow,
            "Total Outflow (ETH)": outflow,
            "Average Inflow Value (ETH)": avg_inflow_value,
            "Average Outflow Value (ETH)": avg_outflow_value,
            "Transactions Per Month": transactions_per_month,
            "Error Rate": error_rate,
            "Claim Reward Transactions Count": claim_reward_count,
            "Total Claimed Rewards (ETH)": total_claimed_rewards,
        }

        return financial_strategy_insights
