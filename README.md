# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-03 02:09 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | lunc | 38.11% | $162,771,652 | $0.0001 |
| 2 | tag | 35.17% | $78,976,450 | $0.0011 |
| 3 | bsb | 26.37% | $41,113,826 | $0.6581 |
| 4 | ub | 22.77% | $150,716,253 | $0.1547 |
| 5 | genius | 19.33% | $18,232,516 | $0.5984 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | mega | -18.48% | $142,105,180 | $0.1281 |
| 2 | rave | -8.95% | $23,868,461 | $0.6437 |
| 3 | arb | -3.98% | $50,594,109 | $0.1192 |
| 4 | siren | -3.46% | $5,810,690 | $0.6912 |
| 5 | dash | -3.43% | $58,606,039 | $37.1900 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $32,841,387,147 | $0.9998 |
| 2 | btc | -0.09% | $18,192,041,532 | $78,268.0000 |
| 3 | eth | 0.29% | $6,677,133,056 | $2,305.4200 |
| 4 | usdc | 0.01% | $5,215,045,019 | $0.9999 |
| 5 | sol | -0.20% | $1,655,652,909 | $83.7600 |


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
