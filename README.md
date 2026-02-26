# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-02-26 01:24 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | power | 32.27% | $26,269,187 | $0.9112 |
| 2 | dot | 28.64% | $784,278,284 | $1.6600 |
| 3 | near | 16.77% | $311,756,057 | $1.1700 |
| 4 | apt | 15.13% | $256,489,219 | $0.9868 |
| 5 | uni | 14.62% | $582,640,149 | $4.0200 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | skr | -11.94% | $37,917,933 | $0.0221 |
| 2 | h | -8.33% | $54,838,795 | $0.1319 |
| 3 | pippin | -8.03% | $61,043,125 | $0.7417 |
| 4 | ar | -7.88% | $100,195,323 | $1.7700 |
| 5 | m | -6.60% | $8,333,859 | $1.3300 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $94,540,296,606 | $1.0000 |
| 2 | btc | 3.69% | $54,655,268,583 | $68,482.0000 |
| 3 | eth | 7.42% | $28,669,676,044 | $2,058.2000 |
| 4 | usdc | 0.00% | $14,015,601,442 | $1.0000 |
| 5 | sol | 8.50% | $6,225,719,541 | $88.9400 |


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
