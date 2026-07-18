# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-07-18 01:49 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | xec | 15.31% | $74,875,885 | $0.0000 |
| 2 | ub | 11.86% | $12,970,624 | $0.0910 |
| 3 | pi | 9.82% | $20,116,351 | $0.0832 |
| 4 | edge | 7.21% | $7,710,513 | $0.4404 |
| 5 | dexe | 6.58% | $108,244,331 | $36.3800 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | trac | -11.85% | $14,985,523 | $0.2656 |
| 2 | stable | -9.55% | $19,675,916 | $0.0355 |
| 3 | bonk | -8.44% | $59,993,251 | $0.0000 |
| 4 | night | -7.97% | $29,767,770 | $0.0275 |
| 5 | kite | -7.91% | $56,668,700 | $0.1128 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.02% | $41,455,859,324 | $0.9994 |
| 2 | btc | 0.50% | $27,255,387,359 | $63,921.0000 |
| 3 | usdc | 0.01% | $10,456,118,073 | $1.0000 |
| 4 | eth | -0.70% | $9,518,707,516 | $1,841.0200 |
| 5 | sol | -0.01% | $1,513,635,199 | $75.1100 |


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
