# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-12 02:50 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | velvet | 125.62% | $100,703,876 | $1.7900 |
| 2 | skyai | 47.08% | $59,252,081 | $0.2708 |
| 3 | xpl | 27.95% | $115,718,656 | $0.0794 |
| 4 | beat | 24.15% | $160,710,401 | $8.7300 |
| 5 | lab | 20.77% | $48,393,368 | $9.4300 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | bdx | -31.55% | $14,643,412 | $0.0539 |
| 2 | siren | -25.03% | $29,040,426 | $0.4951 |
| 3 | home | -12.45% | $257,468,349 | $0.0304 |
| 4 | hash | -9.87% | $6,581 | $0.0096 |
| 5 | ub | -7.89% | $20,706,581 | $0.1279 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $50,689,480,027 | $0.9987 |
| 2 | btc | 2.52% | $30,284,724,936 | $63,522.0000 |
| 3 | usdc | -0.00% | $13,307,543,108 | $0.9997 |
| 4 | eth | 2.59% | $11,837,519,414 | $1,674.1900 |
| 5 | sol | 4.34% | $2,676,490,805 | $67.1300 |


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
