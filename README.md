# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-31 01:18 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | sent | 10.14% | $760,286,222 | $0.0464 |
| 2 | fluid | 8.66% | $17,142,013 | $2.9100 |
| 3 | whype | 5.40% | $250,282,519 | $31.4200 |
| 4 | kite | 5.19% | $39,746,051 | $0.1447 |
| 5 | pi | 5.09% | $21,192,631 | $0.1729 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | kag | -23.94% | $10,564,976 | $88.3300 |
| 2 | river | -19.32% | $58,141,079 | $35.4600 |
| 3 | pippin | -19.28% | $61,029,534 | $0.2371 |
| 4 | zro | -12.92% | $128,685,459 | $1.8400 |
| 5 | ip | -11.01% | $93,994,139 | $1.7400 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $127,204,492,657 | $0.9985 |
| 2 | btc | 0.23% | $77,479,119,138 | $84,072.0000 |
| 3 | eth | -3.45% | $41,310,135,165 | $2,707.9600 |
| 4 | usdc | 0.00% | $13,369,332,798 | $0.9997 |
| 5 | sol | 0.37% | $7,125,782,231 | $117.8600 |


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
