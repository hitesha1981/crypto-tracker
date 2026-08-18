# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-08-18 00:47 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ansem | 22.50% | $39,869,876 | $0.2799 |
| 2 | hash | 13.60% | $58,608 | $0.0084 |
| 3 | vvv | 13.30% | $17,952,545 | $13.2800 |
| 4 | pieverse | 10.70% | $8,371,775 | $0.9721 |
| 5 | comp | 10.50% | $33,378,268 | $17.8800 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | velvet | -43.70% | $24,143,427 | $0.5846 |
| 2 | beat | -32.90% | $48,102,360 | $0.3128 |
| 3 | h | -9.40% | $19,951,862 | $0.1195 |
| 4 | ake | -9.00% | $14,636,558 | $0.0091 |
| 5 | btw | -7.20% | $43,114,016 | $0.3558 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $33,726,005,274 | $0.9993 |
| 2 | btc | 2.50% | $21,474,696,812 | $64,345.0000 |
| 3 | usdc | 0.00% | $9,196,499,214 | $0.9997 |
| 4 | eth | 2.00% | $6,844,694,439 | $1,908.1300 |
| 5 | sol | 1.90% | $1,278,033,759 | $75.8400 |


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
