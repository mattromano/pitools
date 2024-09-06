# Vertex Protocol Overview

### Vertex UI

- **User Experience**: 
  - Similar to centralized exchanges; users send collateral and trade quickly without signing each transaction.
  - Features one-click trading.
  - Shared order book across Vertex and Blitz, synchronized across separate L2 chains.

### Main Differentiators

#### Edge - Synchronous Liquidity

- **Function**: Allows cross-chain trading by connecting orders via Vertex's sequencer.
- **Liquidity Management**: Balances trades across chains, solving fragmented liquidity issues.
- **Current Integration**: Combines liquidity from Arbitrum and Blast, with plans for expansion.

#### Speed

- **Mission Statement**: "Trade like a centralized exchange, self-custody like a DEX."
- **Off-Chain Sequencer**: Executes trades in less than 10 ms, matching centralized exchange speed.
- **Gas Optimization**: Trades are batched and published on-chain, reducing gas costs and minimizing exposure to MEV.

#### Cross-Portfolio Margin

- **Benefit**: Considers total account value for liquidation risk, unlike other exchanges that assess individual positions.

## Flipside Curation

### Curation Phases

1. **Core Tables**: Include on-chain data essential to Vertex trading.
2. **Curated Tables**: Provide analytical and aggregate data, such as funding rates and market depth.

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

