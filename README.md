# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-10 01:08 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pol | 13.04% | $353,833,950 | $0.1568 |
| 2 | pippin | 9.27% | $44,893,740 | $0.4138 |
| 3 | render | 6.43% | $165,981,243 | $2.3100 |
| 4 | atom | 5.89% | $84,020,511 | $2.5800 |
| 5 | m | 5.83% | $10,121,514 | $1.7100 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | night | -11.15% | $33,089,875 | $0.0661 |
| 2 | cc | -9.34% | $16,035,164 | $0.1253 |
| 3 | zec | -7.80% | $690,917,268 | $401.0700 |
| 4 | mon | -6.65% | $130,504,027 | $0.0259 |
| 5 | hash | -6.52% | $19,401 | $0.0243 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.04% | $69,116,675,298 | $0.9988 |
| 2 | btc | -0.76% | $43,082,303,483 | $90,517.0000 |
| 3 | eth | -1.01% | $19,045,509,696 | $3,082.2900 |
| 4 | usdc | -0.01% | $11,349,503,408 | $0.9999 |
| 5 | sol | -2.35% | $5,402,568,943 | $135.7900 |


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
