# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-08-06 01:52 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | m | 66.70% | $383,597 | $1.2900 |
| 2 | cys | 38.30% | $187,345,977 | $0.7885 |
| 3 | btw | 20.70% | $21,104,388 | $0.1644 |
| 4 | zbt | 17.30% | $30,996,625 | $0.1298 |
| 5 | ub | 14.60% | $115,753,735 | $0.1483 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | peanut | -14.90% | $2 | $0.0006 |
| 2 | meta | -9.70% | $7,246,983 | $5.5300 |
| 3 | beat | -7.90% | $20,448,748 | $2.3200 |
| 4 | cc | -5.10% | $12,861,427 | $0.1027 |
| 5 | tel | -3.50% | $1,073,688 | $0.0016 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $37,240,776,280 | $0.9992 |
| 2 | btc | 0.90% | $22,893,834,423 | $64,590.0000 |
| 3 | usdc | 0.00% | $10,251,215,037 | $0.9996 |
| 4 | eth | 2.20% | $8,651,311,698 | $1,907.4600 |
| 5 | sol | 0.50% | $1,631,700,260 | $73.8500 |


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
