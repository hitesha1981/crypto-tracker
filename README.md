# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-09-02 02:16 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | uai | 53.98% | $11,929,599 | $0.5806 |
| 2 | useless | 19.01% | $75,245,018 | $0.1105 |
| 3 | ff | 17.75% | $41,920,460 | $0.0992 |
| 4 | fil | 13.05% | $184,998,212 | $0.7703 |
| 5 | uni | 11.58% | $920,360,798 | $5.8500 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | skr | -34.05% | $63,365,821 | $0.0207 |
| 2 | cards | -14.86% | $4,539,786 | $0.1776 |
| 3 | safe | -11.69% | $6,346,870 | $0.1966 |
| 4 | flr | -9.24% | $7,687,793 | $0.0065 |
| 5 | cc | -7.75% | $10,630,670 | $0.1135 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $53,355,015,614 | $0.9996 |
| 2 | btc | -1.47% | $30,216,399,308 | $77,057.0000 |
| 3 | usdc | -0.01% | $16,031,477,439 | $0.9998 |
| 4 | eth | -2.22% | $13,076,111,967 | $2,400.3500 |
| 5 | sol | -3.71% | $3,501,199,404 | $99.0200 |


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
