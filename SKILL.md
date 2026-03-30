# 📊 Chinese Interest Rate Monitor

Comprehensive tracking of China's interest rate data with daily checks and instant change notifications.

> Monitor China interest rates comprehensively. Daily check with change alerts.

## Metadata

- **name**: chinese-interest-rate-en
- **version**: 2.0.0
- **description**: Comprehensive tracking of China's interest rates: LPR, bank deposit base rates, government bond yields, SHIBOR, mortgage rates, and more. Instant notifications when changes occur.
- **language**: en
- **tags**: finance, china, interest-rate, LPR, SHIBOR, bank-deposit, bond-yield, mortgage, monitor, international, china-finance, PBC, loan-prime-rate

---

## Overview

| Feature | Description |
|---------|-------------|
| 🏦 Base Rates | 1Y/3Y/5Y Time Deposit Base Rates |
| 📈 LPR | 1Y/5Y Loan Prime Rate |
| 📉 Bond Yields | 1Y/3Y/10Y Government Bond Yields |
| 💧 SHIBOR | O/N, 1W, 1M, 3M Interbank Offered Rates |
| 🏠 Mortgage Rate | LPR for 5Y+ (Base Mortgage Rate) |
| 🔄 Repo Rates | 7D/14D Open Market Operation Rates |
| 💰 RRR | Reserve Requirement Ratio for Large Financial Institutions |
| Daily Check | Automatic daily check |
| Change Alert | Instant push on changes, silent when unchanged |

---

## Data Points Tracked

### 🏦 Bank Deposit Rates (Base)

| Tenor | Description |
|-------|-------------|
| 1 year | 1-Year Time Deposit Base Rate |
| 3 years | 3-Year Time Deposit Base Rate |
| 5 years | 5-Year Time Deposit Base Rate |

### 📊 LPR (Loan Prime Rate)

| Tenor | Description |
|-------|-------------|
| 1-Year | Loan Prime Rate (Real Economy) |
| 5-Year+ | Loan Prime Rate (Real Estate) |

### 📉 Government Bond Yields

| Tenor | Description |
|-------|-------------|
| 1-Year | 1-Year Government Bond Yield |
| 3-Year | 3-Year Government Bond Yield |
| 10-Year | 10-Year Government Bond Yield (Key Indicator) |

### 💧 SHIBOR (Shanghai Interbank Offered Rate)

| Tenor | Description |
|-------|-------------|
| O/N Overnight | Overnight Lending Rate (Shortest Funding Cost) |
| 1W One-Week | 1-Week Tenor |
| 1M One-Month | 1-Month Tenor |
| 3M Three-Month | 3-Month Tenor (Important Reference) |

### 🏠 Mortgage Rate

| Tenor | Description |
|-------|-------------|
| 5-Year+ | LPR for loans 5 years and above, benchmark for mortgage rates |

### 🔄 Open Market Operation Rates

| Tenor | Description |
|-------|-------------|
| 7-Day Reverse Repo | 7-Day Open Market Reverse Repo Rate |
| 14-Day Reverse Repo | 14-Day Open Market Reverse Repo Rate |
| MLF | Medium-Term Lending Facility Rate (1-Year) |

---

## Data Sources

| Type | Source |
|------|--------|
| Deposit Base Rates | People's Bank of China (PBC) |
| LPR | National Interbank Lending Center |
| Bond Yields | China Bond Information Network / CFETS |
| SHIBOR | China Foreign Exchange Trade System |
| Repo Rates | People's Bank of China |
| RRR | People's Bank of China |

---

## Notification Format

### When Changes Occur

```
📊 China Interest Rate Daily Report | {Date}

🏦 Bank Deposit Rates (Base)
- 1Y: X.XX% (±Xbp)
- 3Y: X.XX% (±Xbp)
- 5Y: X.XX% (±Xbp)

📊 LPR Loan Prime Rate
- 1Y: X.XX% (±Xbp)
- 5Y+: X.XX% (±Xbp)

📉 Government Bond Yields
- 1Y: X.XX% (±Xbp)
- 3Y: X.XX% (±Xbp)
- 10Y: X.XX% (±Xbp)

💧 SHIBOR Interbank Offered Rates
- O/N: X.XX% (±Xbp)
- 1W: X.XX% (±Xbp)
- 1M: X.XX% (±Xbp)
- 3M: X.XX% (±Xbp)

🏠 Mortgage Related
- 5Y+ LPR: X.XX% (±Xbp)

🔄 Open Market Operations
- 7D Repo: X.XX% (±Xbp)
- 14D Repo: X.XX% (±Xbp)

💡 Impact Analysis: Brief explanation of the changes' economic implications
```

### When No Changes

Silent — no notification sent.

---

## Data File Format

`data/rates.json`:

```json
{
  "updateDate": "2026-03-30",
  "depositRates": {
    "1year": "1.50",
    "3year": "2.00",
    "5year": "2.25"
  },
  "LPR": {
    "1year": "3.45",
    "5yearPlus": "4.20"
  },
  "bondYields": {
    "1year": "1.60",
    "3year": "1.85",
    "10year": "2.30"
  },
  "SHIBOR": {
    "ON": "1.75",
    "1W": "1.85",
    "1M": "2.00",
    "3M": "2.10"
  },
  "mortgageLPR": {
    "5yearPlus": "4.20"
  },
  "OMO": {
    "repo7d": "1.80",
    "repo14d": "1.95",
    "MLF1Y": "2.50"
  }
}
```

---

## Installation

```bash
openclaw skills install chinese-interest-rate-en
```

---

## Scheduled Tasks

Recommended daily execution at 10:00 AM (Beijing Time):

```json
{
  "schedule": {
    "kind": "cron",
    "expr": "0 10 * * *",
    "tz": "Asia/Shanghai"
  }
}
```

---

## File Structure

```
chinese-interest-rate-en/
├── SKILL.md              # This file
├── _meta.json            # Version info
├── README.md             # English documentation
├── data/
│   └── rates.json        # Historical rate data
└── scripts/
    └── check_rates.py    # Rate checking script
```

---

## Extension Notes

To add more rate indicators, modify:
1. `data/rates.json` — Add new rate fields
2. `scripts/check_rates.py` — Add new rate data sources
3. SKILL.md — Update this documentation

---

## Use Cases

- 📊 Financial Professionals (Banking, Securities, Funds)
- 🏠 Mortgage Holders (LPR changes directly affect monthly payments)
- 💼 Investment & Wealth Management (LPR is a key capital market indicator)
- 📈 Economic Researchers (Interest rates are core macroeconomic variables)

---

## License

MIT License

---

_Track interest rate changes, stay ahead of the market 📊_
