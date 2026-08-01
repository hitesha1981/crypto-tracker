# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-08-01 02:06 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | m | 66.70% | $383,597 | $1.2900 |
| 2 | tag | 29.20% | $7,183,371 | $0.0014 |
| 3 | glidr | 25.10% | $57,150 | $1.2700 |
| 4 | us | 23.50% | $6,710,952 | $0.0555 |
| 5 | btw | 23.20% | $7,855,924 | $0.1052 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | peanut | -14.90% | $2 | $0.0006 |
| 2 | edge | -11.20% | $4,048,375 | $0.3609 |
| 3 | cards | -10.30% | $1,774,352 | $0.1454 |
| 4 | lit | -9.10% | $34,395,110 | $2.0800 |
| 5 | kag | -9.00% | $176,270 | $52.6800 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $43,249,671,895 | $0.9991 |
| 2 | btc | -3.00% | $28,459,836,832 | $62,930.0000 |
| 3 | usdc | 0.00% | $11,070,617,243 | $0.9996 |
| 4 | eth | -2.90% | $8,399,392,967 | $1,865.5400 |
| 5 | sol | -2.30% | $1,470,677,696 | $72.9800 |


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
