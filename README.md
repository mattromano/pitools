# Vertex Protocol Overview

## Trading Overview

- **Start with DeFi Llama**: Vertex is categorized under derivatives exchanges.
- **Competitors**: Vertex competes with DYDX, GMX, and Hyperliquid, focusing on perpetual futures trading via a Central Limit Order Book (CLOB). This is different from Automated Market Maker (AMM) DEXs like Uniswap or Curve.

### AMMs vs. CLOBs

| Feature                | AMMs (Automated Market Makers)                | CLOBs (Central Limit Order Books)              |
|------------------------|-----------------------------------------------|------------------------------------------------|
| **Mechanism**          | Liquidity pools managed by formulas          | Order book with set price levels               |
| **Trading Options**    | Primarily market buys                        | Allows stop-loss, limit orders, etc.           |
| **Throughput Needs**   | Lower                                          | High, requiring L2 for fast execution          |
| **Innovation**         | Crypto-native, popularized by Uniswap         | Used in traditional and crypto exchanges       |

### Centralized vs. Decentralized Exchanges

- **Centralized Exchanges**: Binance and the now-defunct FTX were known for their perpetual futures products.
- **Perpetual Futures Contracts (Perps)**:
  - **Definition**: Contracts allowing bets on future asset prices without owning the asset.
  - **Trading Basis**: Mainly traded in USDC; not actual assets like LINK or ETH.
  - **Advantages**: Enables shorting, longing, and using leverage.
  - **Leverage**: Increases potential profits and risks, with the possibility of liquidation.

## Vertex Protocol

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

### Suggestions for Improvement

- **Structure**: Use sections and subheadings to clearly delineate concepts and features.
- **Clarity**: Simplify technical jargon and provide brief explanations for complex terms.
- **Consistency**: Use consistent terminology, such as "AMMs" or "Automated Market Makers."
- **Simplification**: Break down long sentences to improve readability and comprehension.

These adjustments help present the key features and advantages of the Vertex Protocol in a clear, structured format.
