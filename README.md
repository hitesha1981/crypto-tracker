# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-02-20 01:23 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | rave | 29.94% | $61,200,637 | $0.4989 |
| 2 | snx | 15.73% | $107,551,457 | $0.3453 |
| 3 | kite | 12.96% | $107,985,735 | $0.2522 |
| 4 | lunc | 8.70% | $17,897,872 | $0.0000 |
| 5 | night | 8.61% | $21,372,278 | $0.0626 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | awe | -39.54% | $75,183,143 | $0.0627 |
| 2 | op | -16.07% | $217,407,572 | $0.1372 |
| 3 | hnt | -14.83% | $15,041,030 | $1.4200 |
| 4 | arb | -9.14% | $104,450,393 | $0.0977 |
| 5 | m | -5.91% | $8,888,323 | $1.3400 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $57,479,243,215 | $0.9996 |
| 2 | btc | 0.89% | $34,455,237,549 | $67,246.0000 |
| 3 | eth | -0.26% | $19,664,744,412 | $1,957.4200 |
| 4 | usdc | 0.00% | $4,358,261,044 | $0.9999 |
| 5 | sol | 1.50% | $3,166,774,324 | $82.9100 |


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
