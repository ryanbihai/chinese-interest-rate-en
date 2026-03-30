# Chinese Interest Rate Monitor (English Version)

## Overview

This is the English version of the Chinese Interest Rate Monitor skill, designed for international users interested in China's financial markets.

## Features

- **9 Categories of Interest Rates**: Deposit base rates, LPR, government bond yields, SHIBOR, mortgage rates, open market operation rates, and more
- **Daily Automatic Checks**: Runs on a configurable schedule
- **Instant Change Notifications**: Get notified immediately when rates change
- **Silent When Unchanged**: No notifications if nothing changes

## Supported Interest Rate Types

| Category | Data Points |
|----------|-------------|
| 🏦 Bank Deposit Base Rates | 1Y, 3Y, 5Y time deposits |
| 📈 LPR (Loan Prime Rate) | 1Y, 5Y+ |
| 📉 Government Bond Yields | 1Y, 3Y, 10Y |
| 💧 SHIBOR | O/N, 1W, 1M, 3M |
| 🏠 Mortgage Rates | 5Y+ LPR |
| 🔄 Open Market Operations | 7D Repo, 14D Repo, MLF |
| 💰 Reserve Requirement Ratio | Large financial institutions |

## Data Sources

All data is sourced from official Chinese financial authorities:
- People's Bank of China (PBC)
- National Interbank Lending Center
- China Foreign Exchange Trade System
- China Bond Information Network

## Installation

```bash
openclaw skills install chinese-interest-rate-en
```

## Configuration

Set up a daily cron job at 10:00 AM Beijing Time:

```json
{
  "schedule": {
    "kind": "cron",
    "expr": "0 10 * * *",
    "tz": "Asia/Shanghai"
  }
}
```

## For International Users

This skill is essential for:
- **FX Traders**: Monitor PBOC policy direction through interest rate signals
- **China-Focused Investors**: Track LPR changes affecting A-shares and RMB bonds
- **Import/Export Businesses**: Understand financing costs in China
- **Financial Researchers**: Access standardized Chinese rate data in English

## License

MIT License

---

_Track China's interest rates with confidence 📊_
