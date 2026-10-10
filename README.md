# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-10-10 03:41 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | kaia | 52.29% | $128,486,135 | $0.0574 |
| 2 | bat | 25.86% | $88,331,695 | $0.1332 |
| 3 | zk | 19.98% | $67,073,750 | $0.0140 |
| 4 | drv | 19.44% | $111,590,225 | $0.5458 |
| 5 | cap | 17.11% | $41,433,373 | $0.0856 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | sent | -16.79% | $22,570,731 | $0.0204 |
| 2 | hash | -16.41% | $9,504 | $0.0063 |
| 3 | br | -8.93% | $5,456,897 | $0.4797 |
| 4 | ray | -7.75% | $59,501,004 | $2.2700 |
| 5 | met | -7.57% | $169,536,799 | $0.4054 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $45,831,826,987 | $0.9993 |
| 2 | btc | 0.33% | $24,378,499,106 | $82,496.0000 |
| 3 | usdc | 0.02% | $14,744,922,856 | $0.9998 |
| 4 | eth | -0.04% | $8,597,026,952 | $2,488.4400 |
| 5 | sol | -0.42% | $2,514,533,433 | $109.5800 |


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
