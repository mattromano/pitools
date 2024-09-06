# Vertex Protocol Overview

## 1. Features

1. **Hybrid CLOB/AMM Design**:
   - Vertex combines a Central Limit Order Book (CLOB) and Automated Market Maker (AMM) design.
   - Most trades are matched via an off-chain sequencer, with a typical matching time of 10-30 milliseconds, providing a latency similar to centralized exchanges (CEXs).
   - Matched trades are passed to the on-chain risk engine along with deposit/withdrawal instructions, batching over 200 orders into a single transaction.
     - This approach makes trading cheaper, faster, and resistant to Miner Extractable Value (MEV).
     - Future plans include decentralizing this layer, essentially creating a "Layer 3" solution.
   - The AMM serves as a backup, and all liquidations are processed on-chain.

2. **Cross-Portfolio Margin (Default Setting)**:
   - Margin is shared across all positions, including perpetuals, spot trades, and liquidity pools.
   - Creating liquidation events is challenging, even at 20x leverage, due to robust risk management.
     - Liquidation involves a step-by-step process across different products used for margin.
   - Automatic risk management transfers margin between open positions to maintain required levels.
   - **Isolated Margin**: Margin is based solely on the liability of an individual position, standard in most DeFi applications.

3. **Edge Sequencer**:
   - The sequencer matches orders across all chains where a Vertex instance is running.
   - **How it Works**:
     - If a long position is taken on one chain, it is matched with a short position on another chain. Edge pairs these trades and takes the opposite side of the matched orders.
     - Liquidity between chains is periodically aggregated and settled on the backend.

4. **Integrated Money Market**:
   - Earn yield on all deposits instantly, which ties into Vertex's liquidation process. In extreme cases, losses may be socialized across the platform.


## 2. Curation

### Curation Levels

1. **Core Tables**: Include on-chain data essential to Vertex trading.
2. **Curated Tables**: Provide analytical and aggregate data, such as funding rates and market depth. Combines both on-chain data with API data.

### Specific Curation for Blitz on Blast

| Data Type         | Description                                                                                 |
|-------------------|---------------------------------------------------------------------------------------------|
| **EZ Core**       |                                                                                             |
| Perp Trades       | Includes USD amounts, wallet data, and order types.                                         |
| Spot Trades       | Details on spot market trades.                                                             |
| Products          | Ensures all trading symbols are up-to-date via API.                                         |
| Liquidations      | Captures all liquidation events, with some binary decoding.                                 |
| Clearinghouse     | Tracks collateral deposits and withdrawals.                                                 |
| **Curated Vertex**|                                                                                             |
| Market Stats      | Combines on-chain data with API metrics like funding rates, trader counts, and open interest.|
| Market Depth      | Displays the full order book, showing liquidity at each price level.                        |
| Staking Actions   | Tracks VRTX staking, withdrawals, and rewards.                                              |
| Account Aggregation| Provides aggregated metrics at the subaccount level.                                        |
| Edge Specific     | Pairs Edge trades with opposite trades to capture net trading activity.                     |

---

