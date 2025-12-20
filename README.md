# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2025-12-20 01:04 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | h | 34.59% | $87,803,541 | $0.1304 |
| 2 | chz | 23.07% | $195,748,879 | $0.0353 |
| 3 | leo | 18.58% | $4,332,754 | $7.9900 |
| 4 | zbcn | 17.32% | $15,121,308 | $0.0028 |
| 5 | zec | 15.93% | $812,639,066 | $450.1800 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | beat | -15.82% | $90,137,998 | $2.0800 |
| 2 | m | -9.93% | $19,121,690 | $1.4100 |
| 3 | ftn | -2.29% | $12,750,495 | $1.2800 |
| 4 | hash | -2.00% | $15,650 | $0.0303 |
| 5 | twt | -1.85% | $21,468,892 | $0.8362 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $90,146,087,046 | $0.9996 |
| 2 | btc | 3.08% | $51,180,188,638 | $87,985.0000 |
| 3 | eth | 5.29% | $28,216,901,985 | $2,973.0400 |
| 4 | usdc | 0.00% | $13,309,969,967 | $0.9999 |
| 5 | bnb | 2.73% | $5,611,667,771 | $853.0200 |


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
