# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-08-24 00:50 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | morpho | 27.90% | $72,549,781 | $2.7900 |
| 2 | cashcat | 26.50% | $32,444,316 | $0.1496 |
| 3 | trac | 23.60% | $47,185,894 | $0.3970 |
| 4 | grass | 23.50% | $25,987,047 | $0.3652 |
| 5 | pengu | 18.30% | $372,404,061 | $0.0097 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | b | -7.30% | $3,881,207 | $0.1341 |
| 2 | h | -4.30% | $4,952,675 | $0.0690 |
| 3 | genius | -3.70% | $8,781,300 | $0.3212 |
| 4 | ake | -3.70% | $2,478,594 | $0.0086 |
| 5 | btw | -3.40% | $14,293,097 | $0.4320 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | sand | 1.40% | $2,711,409,611,214 | $0.0454 |
| 2 | usdt | 0.00% | $57,357,069,954 | $0.9999 |
| 3 | btc | 0.90% | $29,914,471,825 | $77,290.0000 |
| 4 | eth | 2.10% | $16,668,026,642 | $2,447.7400 |
| 5 | usdc | 0.00% | $13,859,981,611 | $0.9999 |


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
