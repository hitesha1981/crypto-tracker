# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-23 02:26 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | beat | 70.21% | $84,813,881 | $1.2900 |
| 2 | genius | 36.51% | $119,468,293 | $0.6058 |
| 3 | usda | 26.50% | $11 | $0.9828 |
| 4 | rail | 25.64% | $3,874,420 | $2.4000 |
| 5 | ub | 17.74% | $28,505,394 | $0.1129 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | nex | -21.50% | $50,519,864 | $0.0000 |
| 2 | lit | -16.76% | $60,398,219 | $1.1900 |
| 3 | kite | -16.42% | $59,861,030 | $0.1946 |
| 4 | edge | -13.93% | $11,428,302 | $1.2400 |
| 5 | cfg | -12.87% | $30,379,401 | $0.2755 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $55,399,268,447 | $0.9988 |
| 2 | btc | -2.78% | $31,691,523,458 | $75,413.0000 |
| 3 | usdc | 0.01% | $13,964,170,428 | $0.9998 |
| 4 | eth | -3.27% | $13,134,595,626 | $2,064.4900 |
| 5 | sol | -3.13% | $2,713,493,959 | $84.2200 |


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
