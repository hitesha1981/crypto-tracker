# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-08-11 01:07 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | m | 66.70% | $383,597 | $1.2900 |
| 2 | cys | 22.20% | $54,677,923 | $1.3100 |
| 3 | tibbir | 20.00% | $3,765,787 | $0.1363 |
| 4 | kag | 13.50% | $502,308 | $62.7900 |
| 5 | cards | 13.30% | $2,543,318 | $0.1474 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | beat | -61.10% | $84,078,286 | $1.3700 |
| 2 | peanut | -14.90% | $2 | $0.0006 |
| 3 | koge | -12.40% | $21,846 | $52.4800 |
| 4 | btw | -7.70% | $28,644,758 | $0.2000 |
| 5 | tel | -6.50% | $1,142,406 | $0.0015 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $33,560,439,841 | $0.9991 |
| 2 | btc | -1.40% | $20,832,089,460 | $63,957.0000 |
| 3 | usdc | 0.00% | $8,538,776,824 | $0.9996 |
| 4 | eth | -1.90% | $7,287,468,375 | $1,873.3200 |
| 5 | sol | -0.60% | $1,370,212,777 | $75.7300 |


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
