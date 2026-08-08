# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-08-08 01:02 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | m | 66.70% | $383,597 | $1.2900 |
| 2 | spcxb | 16.30% | $179,205,131 | $132.8300 |
| 3 | btw | 16.00% | $25,145,274 | $0.2242 |
| 4 | cys | 14.30% | $34,269,475 | $0.9493 |
| 5 | gomining | 13.20% | $7,841,200 | $0.2916 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ub | -16.90% | $27,900,613 | $0.1391 |
| 2 | peanut | -14.90% | $2 | $0.0006 |
| 3 | us | -10.90% | $10,630,022 | $0.0508 |
| 4 | bonk | -10.60% | $78,886,621 | $0.0000 |
| 5 | cards | -9.30% | $1,696,627 | $0.1417 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $35,273,031,901 | $0.9995 |
| 2 | btc | 0.90% | $21,746,691,674 | $64,880.0000 |
| 3 | usdc | 0.00% | $9,191,894,842 | $0.9997 |
| 4 | eth | 0.60% | $7,885,158,138 | $1,913.0500 |
| 5 | xrp | -0.90% | $1,551,174,052 | $1.0240 |


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
