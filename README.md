# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-23 01:29 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | siren | 161.30% | $157,754,230 | $2.4300 |
| 2 | bananas31 | 46.36% | $118,014,189 | $0.0135 |
| 3 | river | 18.49% | $53,531,784 | $30.1700 |
| 4 | dexe | 12.06% | $28,344,552 | $7.2600 |
| 5 | kite | 7.05% | $56,824,254 | $0.2224 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | fluid | -17.34% | $11,327,293 | $1.8800 |
| 2 | zbcn | -8.65% | $6,042,403 | $0.0023 |
| 3 | ip | -8.55% | $41,993,954 | $0.6645 |
| 4 | lit | -8.50% | $19,466,789 | $0.9403 |
| 5 | ath | -8.38% | $27,774,378 | $0.0072 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $47,315,131,394 | $0.9999 |
| 2 | btc | -1.34% | $28,509,546,439 | $68,079.0000 |
| 3 | eth | -1.46% | $14,525,484,800 | $2,059.6100 |
| 4 | usdc | -0.00% | $6,068,831,782 | $1.0000 |
| 5 | sol | -1.04% | $2,541,490,011 | $86.4900 |


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
