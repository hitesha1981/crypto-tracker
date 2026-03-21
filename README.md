# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-21 01:20 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | zano | 15.11% | $2,125,314 | $9.9900 |
| 2 | zbcn | 14.86% | $15,192,213 | $0.0027 |
| 3 | siren | 13.29% | $8,991,504 | $0.9102 |
| 4 | ath | 9.49% | $64,324,142 | $0.0076 |
| 5 | akt | 9.36% | $18,496,881 | $0.5466 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | lit | -11.66% | $17,675,004 | $1.0710 |
| 2 | river | -9.89% | $51,862,729 | $22.0700 |
| 3 | b | -9.14% | $5,429,359 | $0.2224 |
| 4 | m | -9.01% | $8,805,785 | $1.6400 |
| 5 | btse | -8.66% | $6,986,394 | $1.4600 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $60,835,614,230 | $0.9999 |
| 2 | btc | 0.32% | $37,155,654,123 | $70,596.0000 |
| 3 | eth | 0.14% | $16,757,194,356 | $2,152.4000 |
| 4 | usdc | -0.01% | $8,636,716,451 | $0.9999 |
| 5 | sol | 0.62% | $2,879,178,523 | $90.0900 |


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
