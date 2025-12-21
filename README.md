# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2025-12-21 01:12 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | cc | 23.16% | $51,130,848 | $0.1034 |
| 2 | night | 21.01% | $3,444,633,140 | $0.0786 |
| 3 | uni | 17.27% | $919,536,736 | $6.1900 |
| 4 | beat | 14.73% | $69,573,573 | $2.3700 |
| 5 | icp | 12.91% | $151,456,348 | $3.3100 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | bch | -4.14% | $389,851,907 | $592.7100 |
| 2 | m | -3.52% | $12,315,475 | $1.3500 |
| 3 | ip | -3.20% | $18,164,898 | $1.6200 |
| 4 | wif | -3.13% | $88,096,177 | $0.3450 |
| 5 | comp | -3.01% | $22,207,029 | $24.2400 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.02% | $34,149,235,638 | $0.9997 |
| 2 | btc | 0.24% | $16,507,300,584 | $88,307.0000 |
| 3 | eth | -0.10% | $8,343,331,682 | $2,977.0100 |
| 4 | usdc | 0.00% | $3,888,539,451 | $0.9999 |
| 5 | night | 21.01% | $3,444,633,140 | $0.0786 |


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
