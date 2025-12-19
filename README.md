# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2025-12-19 01:09 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ftn | 169.63% | $15,965,852 | $1.3100 |
| 2 | bch | 3.46% | $589,808,646 | $568.3600 |
| 3 | tomi | 3.00% | $42,841 | $0.0000 |
| 4 | zec | 2.94% | $796,817,990 | $387.6400 |
| 5 | beat | 2.45% | $79,958,044 | $2.4700 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | fartcoin | -21.86% | $164,646,204 | $0.2398 |
| 2 | myx | -15.26% | $37,321,527 | $2.8300 |
| 3 | kaia | -13.01% | $25,593,231 | $0.0545 |
| 4 | pump | -11.66% | $115,309,325 | $0.0018 |
| 5 | leo | -9.74% | $5,332,089 | $6.7300 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.03% | $95,215,054,953 | $0.9995 |
| 2 | btc | -0.61% | $58,534,819,136 | $85,356.0000 |
| 3 | eth | 0.04% | $30,365,581,194 | $2,824.8000 |
| 4 | usdc | -0.02% | $14,168,446,213 | $0.9997 |
| 5 | sol | -4.19% | $6,587,266,727 | $118.0600 |


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
