# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-05 01:51 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | siren | 145.02% | $288,307,616 | $0.4192 |
| 2 | kite | 13.56% | $106,012,597 | $0.1563 |
| 3 | zbcn | 12.26% | $10,234,160 | $0.0028 |
| 4 | dexe | 10.13% | $18,161,428 | $8.9100 |
| 5 | bsv | 9.25% | $26,082,576 | $16.3400 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | edge | -20.39% | $144,889,245 | $0.8532 |
| 2 | gas | -8.44% | $25,332,702 | $1.7800 |
| 3 | bananas31 | -7.57% | $12,715,108 | $0.0120 |
| 4 | m | -5.39% | $10,735,642 | $2.5600 |
| 5 | b | -4.98% | $3,614,527 | $0.1731 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $32,514,939,280 | $0.9999 |
| 2 | btc | 0.38% | $15,310,413,187 | $67,098.0000 |
| 3 | eth | 0.35% | $5,897,992,733 | $2,058.2100 |
| 4 | usdc | -0.00% | $3,737,425,032 | $1.0000 |
| 5 | sol | 0.61% | $1,647,930,518 | $80.6000 |


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
