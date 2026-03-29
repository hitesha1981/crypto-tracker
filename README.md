# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-29 01:49 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | siren | 56.32% | $148,153,943 | $1.5500 |
| 2 | hash | 21.19% | $5,713 | $0.0138 |
| 3 | chz | 14.64% | $149,326,009 | $0.0406 |
| 4 | wld | 10.68% | $194,999,571 | $0.2716 |
| 5 | kau | 10.68% | $6,842 | $157.6700 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | kite | -3.79% | $87,290,601 | $0.1725 |
| 2 | dexe | -3.47% | $7,559,433 | $7.2000 |
| 3 | grass | -2.82% | $5,827,533 | $0.2912 |
| 4 | gala | -2.78% | $17,365,122 | $0.0028 |
| 5 | xcn | -2.72% | $4,981,386 | $0.0050 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $38,876,427,218 | $0.9992 |
| 2 | btc | 0.39% | $24,329,193,764 | $66,386.0000 |
| 3 | eth | 0.54% | $9,089,762,829 | $1,999.4000 |
| 4 | usdc | 0.01% | $4,031,299,627 | $0.9998 |
| 5 | sol | -0.44% | $2,130,560,651 | $82.1900 |


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
