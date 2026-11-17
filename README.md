# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-11-17 05:56 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | rain | 73.42% | $20,574,402 | $0.0063 |
| 2 | bp | 20.20% | $33,781,138 | $1.0040 |
| 3 | hash | 16.85% | $116,441 | $0.0075 |
| 4 | dgai | 13.19% | $27,470,330 | $0.7054 |
| 5 | lit | 11.39% | $193,653,994 | $3.0100 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btw | -14.75% | $11,280,346 | $0.3878 |
| 2 | kmno | -5.73% | $8,443,453 | $0.0270 |
| 3 | cap | -4.90% | $10,943,032 | $0.1016 |
| 4 | drv | -4.90% | $10,229,600 | $0.2707 |
| 5 | anvl | -4.66% | $64,502 | $0.0016 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $51,213,752,529 | $0.9993 |
| 2 | btc | 0.61% | $33,258,203,091 | $64,788.0000 |
| 3 | usdc | -0.01% | $13,637,617,192 | $0.9996 |
| 4 | eth | 1.37% | $11,273,913,423 | $1,833.6000 |
| 5 | sol | 2.23% | $2,826,869,160 | $72.7100 |


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
