# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-01 01:16 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btse | 9.33% | $13,478,420 | $1.6000 |
| 2 | myx | 7.79% | $14,733,711 | $3.8500 |
| 3 | chz | 7.58% | $314,259,737 | $0.0427 |
| 4 | ftn | 6.03% | $10,745,470 | $1.0850 |
| 5 | cc | 5.84% | $44,219,807 | $0.1573 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | lit | -14.65% | $18,080,850 | $2.3200 |
| 2 | night | -10.54% | $68,537,486 | $0.0868 |
| 3 | h | -7.29% | $71,007,664 | $0.1696 |
| 4 | tel | -7.27% | $3,126,237 | $0.0039 |
| 5 | merl | -7.11% | $17,589,323 | $0.2960 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.04% | $57,937,658,863 | $0.9986 |
| 2 | btc | -0.40% | $36,562,390,861 | $87,858.0000 |
| 3 | eth | 0.51% | $16,344,864,924 | $2,981.1900 |
| 4 | usdc | -0.00% | $9,864,586,689 | $0.9999 |
| 5 | sol | 0.28% | $3,833,252,047 | $125.4000 |


<!-- END_DYNAMIC_CONTENT -->

## How to generate the coingecko demo public api key

[coingecko-api-key-docs](https://support.coingecko.com/hc/en-us/articles/21880397454233-User-Guide-How-to-sign-up-for-CoinGecko-Demo-API-and-generate-an-API-key)

## Requirements to setup
## 1. Install uv

```bash
brew install uv
✔︎ JSON API cask.jws.json                                                                                                                                                       [Downloaded   15.1MB/ 15.1MB]
✔︎ JSON API formula.jws.json                                                                                                                                                    [Downloaded   32.1MB/ 32.1MB]
# or Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## 2. Setup Python Environment (uv)

From the project root:

```bash
uv python install 3.12
uv venv --python 3.12
source .venv/bin/activate
```

Install dependencies (locked):
```bash
uv add pandas requests matplotlib python-dotenv
```


---

## 4. Update coingecko demo key in .env ( I have provided in .env.sample)
```bash
cat .env
CGK_API_DEMO_KEY="Your-coingecko-demo-api-key-here"
```

---

## 3. To manually run the script
```bash
python3.12 main.py
```
---
