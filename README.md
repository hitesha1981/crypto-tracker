# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-10-26 02:34 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | cap | 38.85% | $130,220,876 | $0.1146 |
| 2 | xcn | 10.59% | $57,543,001 | $0.0043 |
| 3 | hash | 8.19% | $3,796 | $0.0068 |
| 4 | pyth | 4.65% | $32,938,523 | $0.0742 |
| 5 | kmno | 4.50% | $12,623,752 | $0.0418 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | q | -27.31% | $53,293,787 | $0.0558 |
| 2 | comp | -10.67% | $35,326,374 | $21.0200 |
| 3 | beam | -7.38% | $9,742,869 | $0.0030 |
| 4 | cards | -7.18% | $4,713,717 | $0.2916 |
| 5 | useless | -7.04% | $14,552,156 | $0.1652 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $27,488,277,415 | $0.9989 |
| 2 | btc | -1.60% | $15,923,958,026 | $79,512.0000 |
| 3 | eth | -2.54% | $7,105,063,115 | $2,303.5500 |
| 4 | usdc | 0.02% | $6,099,223,199 | $0.9997 |
| 5 | sol | -1.65% | $1,608,804,086 | $100.6300 |


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
