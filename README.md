# Analysis of: 0x99fd1378ca799ed6772fe7bcdc9b30b389518962 address

The address is multi-chain address:
- [Etherscan](https://etherscan.io/address/0x99fd1378ca799ed6772fe7bcdc9b30b389518962)
- [Polygonscan](https://polygonscan.com/address/0x99fd1378ca799ed6772fe7bcdc9b30b389518962)
- [Bscscan](https://bscscan.com/address/0x99fd1378ca799ed6772fe7bcdc9b30b389518962)
- For more info see [this](https://blockscan.com/address/0x99fd1378ca799ed6772fe7bcdc9b30b389518962)

Only ETH transactions are analysed (the majority of transactions).

According to the following sources it seems to me Hodlnaut's trading wallet:

[Link to Tweet](https://twitter.com/FatManTerra/status/1541101976800436225)

Tweet: The majority of Hodlnaut's funds flow to 0x99fd1378ca799ed6772fe7bcdc9b30b389518962, marked by Nansen as Hodlnaut's trading wallet. I traced a few large direct Hodlnaut deposits to here as well. For the time being, we will consider Nansen's tagging to be credible. (9/25)

Other links: 
- [hodlnaut](https://www.hodlnaut.com) staking solution 
- [DUNE dashboard](https://dune.com/georgeai/0x99fd1378ca799ed6772fe7bcdc9b30b389518962-txns)
- [dirtybubblemedia](https://www.dirtybubblemedia.com/p/hodlnaut-may-have-massive-undisclosed)
- [financemagnates](https://www.financemagnates.com/cryptocurrency/terra-luna-how-these-7-wallets-brought-the-ecosystem-to-its-knees/)


## Smart contract function interactions with count > 100, by function:
- approve (564 times): This function is used in ERC-20 tokens to allow another address (like a smart contract) to spend a specific amount of the token on behalf of the token holder.
- transfer (525 times): A standard function in ERC-20 tokens to transfer tokens from the caller's address to another address.
- borrow (520 times): In lending platforms, this function allows a user to borrow assets against their collateral.
- deposit (513 times): Commonly used in various protocols for depositing tokens into a contract, often for staking, providing liquidity, or participating in a lending pool.
- mint (441 times): This can refer to the creation of new tokens or assets in a protocol, or minting new liquidity pool tokens in exchange for providing liquidity.
- repayBorrow (410 times): Used in lending protocols for a borrower to repay their loans.
- add_liquidity (380 times): A function in liquidity protocols for adding assets to a liquidity pool, often in exchange for pool tokens.
- withdraw (370 times): Used to withdraw tokens from a contract. This could be withdrawing staked tokens, liquidity, or other types of deposits.
- getReward (335 times): Typically found in staking or farming protocols, where users claim their rewards earned from staking or providing liquidity.
- mint_many (247 times): Similar to 'mint', but allows minting multiple items or tokens at once.
- remove_liquidity_one_coin (218 times): In liquidity pools, especially those with multiple tokens, this function removes liquidity in the form of a specific token.
- cook (216 times): This function name is less standard and could refer to a custom operation in a specific protocol, often involving multiple steps or actions in a single transaction.
- 0x415565b0 (209 times): Appears to be a function selector (first 4 bytes of the hash of the function signature). The specific function depends on the contract.
- redeemUnderlying (197 times): Found in lending protocols, it's used to redeem underlying assets for their equivalent in other tokens, often in lending pools.
- claimComp (169 times): Likely specific to Compound Finance or similar protocols, for claiming COMP tokens or similar governance tokens.
- stake (150 times): Common in staking protocols, used to lock tokens in a contract to participate in network security or earn rewards.
- exchange (149 times): Used in decentralized exchanges for swapping one token for another.
- swapExactTokensForTokens (148 times): A function in decentralized exchanges like Uniswap, used for token swaps where the exact amount of input tokens is specified.
- claimRewards (145 times): Similar to 'getReward', used in staking or farming protocols to claim earned rewards.
- depositAll (141 times): Allows a user to deposit all of a certain type of token they hold into a contract, often found in liquidity or staking protocols.
- sellToUniswap (141 times): Specific to Uniswap or similar exchanges, used to sell tokens directly to the exchange.
- repayBehalf (106 times): In lending protocols, allows one user to repay the loan of another user.

## Smart contract address interactions with count > 100, by smart contract address:
- 0xdef1c0ded9bec7f1a1670819833240f027b25eff    569
- 0x39aa39c021dfbae8fac545936693ac917d5e7563    384
- 0x99fd1378ca799ed6772fe7bcdc9b30b389518962    378
- 0xd061d61a4d941c39e5453435b6345dc261c2fce0    340
- 0x4ddc2d193948926d02f9b1fe9e1daa0718270ed5    338
- 0xf650c3d88d12db855b8bf7d11be6c55a4e07dcc9    305
- 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48    225
- 0xccf4429db6322d5c611ee964527d42e5d685dd6a    211
- 0x7a250d5630b4cf539739df2c5dacb4c659f2488d    205
- 0x5d3a536e4d6dbd6114cc1ead35777bab948e3643    188
- 0xbebc44782c7db0a1a60cb6fe97d0b483032ff1c7    178
- 0x920d9bd936da4eafb5e25c6bdc9f6cb528953f9f    175
- 0x3d9819210a31b4961b30ef54be2aed79b9c9cd3b    172
- 0xdac17f958d2ee523a2206206994597c13d831ec7    169
- 0xa79828df1850e8a3a3064576f380d90aecdd3359    144
- 0x094d12e5b541784701fd8d65f11fc0598fbc6332    127
- 0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f    118
- 0xd533a949740bb3306d119cc777fa900ba034cd52    108
- 0xf859a1ad94bcf445a406b892ef0d3082f4174088    106
- 0xf403c135812408bfbe8713b5a23a04b3d48aae31    101
- 0x7d2768de32b0b80b7a3454c06bdac94a69ddc7a9    100

### With identification of top smart contract addresses:
- 0xdef1c0ded9bec7f1a1670819833240f027b25eff (569 times): Likely associated with a DeFi protocol, possibly Compound Finance, known for lending and borrowing services.
- 0x39aa39c021dfbae8fac545936693ac917d5e7563 (384 times): This address is connected with the USDC stablecoin, possibly for USDC-related transactions or liquidity operations.
- 0x99fd1378ca799ed6772fe7bcdc9b30b389518962 (378 times): The specific role of this address is unclear without additional context.
- 0xd061d61a4d941c39e5453435b6345dc261c2fce0 (340 times): An Ethereum smart contract address, requiring more context to determine its specific function.
- 0x4ddc2d193948926d02f9b1fe9e1daa0718270ed5 (338 times): Associated with Compound Finance, potentially involved in its lending operations.
- 0xf650c3d88d12db855b8bf7d11be6c55a4e07dcc9 (305 times): The specific purpose of this address is not immediately clear without more information.
- 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48 (225 times): This address is for the USDC stablecoin, a USD-pegged cryptocurrency.
- 0xccf4429db6322d5c611ee964527d42e5d685dd6a (211 times): Additional context needed for identification.
- 0x7a250d5630b4cf539739df2c5dacb4c659f2488d (205 times): The address of Uniswap, a popular decentralized exchange on Ethereum.
- 0x5d3a536e4d6dbd6114cc1ead35777bab948e3643 (188 times): Another address linked to Compound Finance, likely for DeFi operations.
- 0xbebc44782c7db0a1a60cb6fe97d0b483032ff1c7 (178 times): Known as Curve Finance's contract address, significant in the DeFi space for stablecoin trading.
- 0x920d9bd936da4eafb5e25c6bdc9f6cb528953f9f (175 times): Specific role is not identifiable without further details.
- 0x3d9819210a31b4961b30ef54be2aed79b9c9cd3b (172 times): Likely associated with a DeFi protocol, specifics require additional data.
- 0xdac17f958d2ee523a2206206994597c13d831ec7 (169 times): Address for Tether (USDT) stablecoin.
- 0xa79828df1850e8a3a3064576f380d90aecdd3359 (144 times): More information needed for accurate identification.
- 0x094d12e5b541784701fd8d65f11fc0598fbc6332 (127 times): The role of this address within the Ethereum ecosystem is not clear.
- 0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f (118 times): Likely associated with a decentralized exchange or a DeFi protocol.
- 0xd533a949740bb3306d119cc777fa900ba034cd52 (108 times): Possibly part of a DeFi protocol, such as a liquidity pool or staking contract.
- 0xf859a1ad94bcf445a406b892ef0d3082f4174088 (106 times): Additional context required for identification.
- 0xf403c135812408bfbe8713b5a23a04b3d48aae31 (101 times): Specific role not immediately identifiable.
- 0x7d2768de32b0b80b7a3454c06bdac94a69ddc7a9 (100 times): Potentially involved in DeFi services, exact nature unclear without more information.



## 1) ETH transaction analysis:
Based on the analysis of the transaction history for the address 0x99fd1378ca799ed6772fe7bcdc9b30b389518962, here are the key financial insights:

Total Transactions: There were 8,456 transactions involving this address.

Inflow vs. Outflow Transactions: The address was involved in 378 inflow transactions (receiving Ether) and 8,111 outflow transactions (sending Ether).

Total Inflow and Outflow: The total inflow of Ether was approximately 182,894.43 ETH, while the outflow was significantly higher at about 1,424,380.35 ETH.

Average Transaction Values: The average inflow transaction value was approximately 483.85 ETH, which is significantly higher than the average outflow transaction value of about 175.61 ETH.

Transaction Frequency Over Time: The number of transactions per month varied significantly, with peaks observed in several months, indicating periods of high activity.

Error Rate: The error rate in transactions was about 1.38%, which is relatively low.

### Conclusions
High Outflow Volume: The significant difference between total outflow and inflow suggests that this address is more actively used for sending Ether than receiving it. This could indicate a role as a distributor or a funding source in transactions.

Large Average Inflow Value: The much higher average value of inflow transactions compared to outflow transactions suggests that this address might be receiving large funding or payments, which are then distributed in smaller amounts.

Fluctuating Activity Levels: The fluctuating transaction frequency over months could indicate participation in periodic activities such as staking, farming, or regular operational transactions for a business or service.

Low Error Rate: The low error rate in transactions indicates careful and accurate transaction execution, which is indicative of an experienced or automated operator.

Potential Involvement in DeFi: Given the high volume of transactions and the types of transactions (large inflows followed by numerous smaller outflows), it's possible that this address is involved in DeFi protocols, possibly in roles like liquidity provision, staking, or as part of a larger automated strategy such as a smart contract executing a specific DeFi strategy.

In conclusion, this Ethereum address appears to be actively managed with a focus on distributing Ether, possibly as part of a larger financial operation or strategy within the Ethereum ecosystem, potentially within DeFi platforms. The strategy seems to involve receiving large sums of Ether and then distributing them in smaller transactions. ​

## 2) DeFi:
DeFi Total Transactions: There were a total of 4,853 transactions that involved DeFi-related activities.

DeFi Inflow and Outflow Transactions: Interestingly, all 4,853 transactions are categorized as outflow transactions (the address sending Ether), with zero inflow transactions (receiving Ether) in the context of DeFi operations.

DeFi Total Inflow and Outflow: The total inflow is 0 ETH, which aligns with the absence of inflow transactions. The total outflow in DeFi activities is substantial, amounting to approximately 1,123,368.32 ETH.

DeFi Average Transaction Values: Since there are no inflow transactions, the average inflow value is 0 ETH. The average outflow value per transaction is approximately 231.48 ETH, which is quite significant and indicates large transactions in the context of DeFi.

DeFi Transaction Frequency Over Time: The number of transactions per month shows variability, with certain months experiencing higher activity. This pattern could be associated with specific market conditions or strategic operations in DeFi protocols.

### Conclusions:
High DeFi Engagement: The high number of transactions and significant outflows suggest deep engagement in DeFi activities.

Large Scale Outflows: The absence of inflow transactions and the considerable average outflow value per transaction indicate that this address might be functioning as a major liquidity provider, or it could be involved in large-scale yield farming or staking operations.

Periodic Activity Patterns: The fluctuating transaction frequency suggests a strategy that responds to market conditions or specific DeFi protocol opportunities, such as entering and exiting positions in response to yield opportunities or liquidity needs.

Potential Role in DeFi Ecosystem: The financial strategy of this address seems to be highly focused on providing liquidity or engaging in other significant transaction activities within the DeFi ecosystem. This could involve participating in liquidity pools, staking in various protocols, or executing large-scale trades on decentralized exchanges.

Risk Management: The significant outflows and the nature of DeFi interactions indicate a potentially aggressive strategy focusing on capital deployment in the DeFi space. This may also imply a sophisticated approach to risk management, given the large values involved in each transaction.

In summary, this address appears to be heavily involved in DeFi activities, primarily in roles that require significant capital outflow, such as liquidity provision or large-scale trading operations. The absence of inflow transactions in the DeFi context is notable and could suggest a focused strategy rather than diversified DeFi interactions.

