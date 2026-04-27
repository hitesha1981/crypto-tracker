# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-27 02:05 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | om | 361.00% | $7,842 | $0.0644 |
| 2 | umxm | 32.79% | $9,916,914 | $1.9500 |
| 3 | gwei | 28.85% | $23,055,562 | $0.1233 |
| 4 | ldo | 23.03% | $261,682,516 | $0.4529 |
| 5 | lunc | 22.28% | $61,168,596 | $0.0001 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ray | -7.05% | $220,133,063 | $0.7418 |
| 2 | ape | -5.48% | $134,784,409 | $0.1464 |
| 3 | kau | -4.96% | $20,474 | $147.0500 |
| 4 | rave | -3.81% | $67,257,059 | $0.8987 |
| 5 | h | -3.20% | $18,677,013 | $0.1479 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $43,376,730,761 | $1.0000 |
| 2 | btc | 2.17% | $26,681,702,286 | $79,198.0000 |
| 3 | eth | 3.29% | $11,581,604,280 | $2,390.9400 |
| 4 | usdc | 0.01% | $8,042,641,123 | $0.9999 |
| 5 | sol | 2.07% | $2,630,737,748 | $87.7700 |


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
