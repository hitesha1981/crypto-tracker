# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-18 02:39 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | mbtc | 192.23% | $47,514 | $0.1604 |
| 2 | bill | 11.55% | $230,607,818 | $0.1551 |
| 3 | hype | 10.53% | $656,289,669 | $45.8000 |
| 4 | akt | 8.25% | $9,864,739 | $0.7424 |
| 5 | 币安人生 | 7.48% | $21,307,250 | $0.4223 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | xp | -8.40% | $3,248,975 | $0.0618 |
| 2 | lunc | -8.06% | $53,913,374 | $0.0001 |
| 3 | gwei | -7.14% | $5,217,755 | $0.1377 |
| 4 | cfx | -7.09% | $15,343,196 | $0.0604 |
| 5 | bch | -6.65% | $235,388,888 | $386.0200 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $41,102,482,552 | $0.9994 |
| 2 | btc | -1.29% | $24,284,975,750 | $76,879.0000 |
| 3 | eth | -2.68% | $11,063,658,383 | $2,116.2600 |
| 4 | usdc | -0.01% | $7,646,819,154 | $0.9997 |
| 5 | sol | -1.27% | $2,352,633,124 | $84.9400 |


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
