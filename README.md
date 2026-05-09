# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-09 02:11 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | siren | 34.43% | $54,033,256 | $1.2800 |
| 2 | ondo | 33.78% | $749,579,953 | $0.4650 |
| 3 | icp | 30.18% | $339,736,072 | $3.9100 |
| 4 | akt | 22.30% | $29,073,388 | $0.7746 |
| 5 | strk | 21.97% | $346,354,786 | $0.0553 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ub | -11.79% | $30,455,500 | $0.1139 |
| 2 | m | -5.90% | $15,294,033 | $3.5400 |
| 3 | lab | -5.50% | $73,919,671 | $4.3500 |
| 4 | ton | -5.01% | $872,709,826 | $2.5500 |
| 5 | dydx | -2.70% | $47,205,219 | $0.1815 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $64,574,948,852 | $0.9999 |
| 2 | btc | 1.05% | $33,630,472,684 | $80,440.0000 |
| 3 | eth | 1.77% | $19,076,061,981 | $2,317.8700 |
| 4 | usdc | 0.02% | $14,103,410,655 | $1.0000 |
| 5 | sol | 6.56% | $3,954,788,090 | $93.6800 |


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
