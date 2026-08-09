# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-08-09 01:07 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | glidr | 82.60% | $2,719 | $1.3300 |
| 2 | m | 66.70% | $383,597 | $1.2900 |
| 3 | beat | 39.60% | $37,452,898 | $3.0200 |
| 4 | cashcat | 37.50% | $17,111,232 | $0.1257 |
| 5 | tel | 14.60% | $1,559,124 | $0.0017 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | kag | -16.50% | $105,736 | $52.8500 |
| 2 | peanut | -14.90% | $2 | $0.0006 |
| 3 | kaito | -11.30% | $79,655,826 | $0.7288 |
| 4 | fgrs | -10.10% | $26,008 | $26.0100 |
| 5 | b | -8.70% | $4,673,849 | $0.1525 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $20,230,305,914 | $0.9994 |
| 2 | btc | 0.10% | $12,255,600,705 | $64,952.0000 |
| 3 | usdc | 0.00% | $4,138,315,092 | $0.9997 |
| 4 | eth | 0.20% | $3,413,715,564 | $1,918.2100 |
| 5 | sol | 3.20% | $1,416,445,528 | $75.9700 |


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
