# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-10-14 02:58 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btw | 31.88% | $133,380,616 | $2.3600 |
| 2 | q | 26.60% | $30,945,384 | $0.0462 |
| 3 | hash | 22.73% | $38,437 | $0.0075 |
| 4 | prl | 22.41% | $8,883,312 | $1.8400 |
| 5 | op | 20.34% | $221,228,111 | $0.1595 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | cap | -7.26% | $14,322,100 | $0.0866 |
| 2 | m | -6.33% | $1,417,557 | $0.8405 |
| 3 | br | -6.11% | $2,416,812 | $0.4272 |
| 4 | kcs | -5.98% | $4,932,072 | $7.3400 |
| 5 | pyth | -5.07% | $68,095,820 | $0.0796 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btc | 0.73% | $1,348,931,482,540 | $83,571.0000 |
| 2 | eth | 0.82% | $1,330,571,801,452 | $2,512.1500 |
| 3 | usdt | 0.01% | $52,856,247,986 | $0.9994 |
| 4 | usdc | 0.00% | $17,445,479,673 | $0.9998 |
| 5 | sol | 0.92% | $3,021,768,532 | $107.7700 |


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
