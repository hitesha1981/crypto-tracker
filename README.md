# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-07 01:48 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | river | 21.98% | $32,889,119 | $13.0600 |
| 2 | ultima | 14.95% | $9,676,669 | $3,535.3000 |
| 3 | kite | 14.16% | $111,997,504 | $0.1570 |
| 4 | siren | 10.12% | $47,506,427 | $0.6127 |
| 5 | grx | 8.06% | $26,590,587 | $11.4500 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btse | -18.03% | $14,439,575 | $1.2000 |
| 2 | vvv | -8.02% | $18,606,201 | $6.6100 |
| 3 | fet | -7.75% | $105,674,519 | $0.2267 |
| 4 | avax | -7.34% | $321,777,756 | $8.7500 |
| 5 | akt | -7.23% | $5,212,150 | $0.4225 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.02% | $68,186,627,835 | $0.9999 |
| 2 | btc | -0.36% | $45,220,654,342 | $68,580.0000 |
| 3 | eth | -0.37% | $17,498,611,621 | $2,108.4400 |
| 4 | usdc | 0.00% | $11,731,249,055 | $0.9999 |
| 5 | sol | -2.35% | $2,849,611,559 | $79.9200 |


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
