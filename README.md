# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-08-16 00:51 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | h | 26.60% | $30,414,622 | $0.1556 |
| 2 | ansem | 20.50% | $17,137,945 | $0.2488 |
| 3 | hash | 10.80% | $5,724 | $0.0083 |
| 4 | q | 8.60% | $4,530,250 | $0.0235 |
| 5 | tibbir | 7.10% | $2,721,818 | $0.1815 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | beat | -40.80% | $40,982,229 | $0.3607 |
| 2 | cys | -33.50% | $121,882,546 | $0.7793 |
| 3 | tag | -22.80% | $4,247,953 | $0.0010 |
| 4 | velvet | -18.40% | $36,307,949 | $0.8497 |
| 5 | fgrs | -14.70% | $26,690 | $26.6900 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $17,637,735,704 | $0.9992 |
| 2 | btc | 0.30% | $10,326,766,716 | $63,016.0000 |
| 3 | usdc | 0.00% | $3,150,960,935 | $0.9996 |
| 4 | eth | 0.10% | $2,835,390,751 | $1,880.2900 |
| 5 | sol | 0.20% | $643,418,392 | $75.3600 |


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
