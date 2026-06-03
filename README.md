# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-03 03:26 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | dexe | 22.37% | $49,494,525 | $22.1400 |
| 2 | genius | 21.70% | $57,633,367 | $0.5441 |
| 3 | lit | 15.35% | $125,546,634 | $1.6300 |
| 4 | 币安人生 | 12.25% | $60,033,725 | $0.6816 |
| 5 | zec | 10.79% | $1,319,433,754 | $624.0100 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ub | -34.15% | $48,600,126 | $0.1257 |
| 2 | skyai | -30.31% | $116,546,714 | $0.1560 |
| 3 | lab | -24.88% | $183,733,110 | $14.1100 |
| 4 | ethfi | -14.73% | $41,246,165 | $0.3293 |
| 5 | ff | -14.12% | $19,731,914 | $0.0949 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.02% | $94,037,095,393 | $0.9987 |
| 2 | btc | -6.39% | $62,523,190,686 | $66,342.0000 |
| 3 | eth | -7.54% | $23,650,416,006 | $1,846.9900 |
| 4 | usdc | 0.00% | $20,437,369,443 | $0.9997 |
| 5 | sol | -8.21% | $3,985,322,542 | $74.0600 |


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
