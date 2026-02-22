# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-02-22 01:27 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | hunt | 49.62% | $134,093 | $6.0000 |
| 2 | 9bit | 27.04% | $8,379,380 | $0.0208 |
| 3 | tibbir | 15.32% | $9,867,859 | $0.1776 |
| 4 | siren | 15.04% | $13,400,106 | $0.2698 |
| 5 | rave | 14.45% | $62,130,894 | $0.6522 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | myx | -15.88% | $50,073,457 | $1.0010 |
| 2 | kite | -15.20% | $186,290,298 | $0.2207 |
| 3 | sent | -10.96% | $27,262,105 | $0.0214 |
| 4 | hash | -5.92% | $1,732 | $0.0174 |
| 5 | bmx | -5.19% | $5,772,102 | $0.3408 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.02% | $36,873,026,714 | $0.9998 |
| 2 | btc | 0.33% | $20,384,634,913 | $68,071.0000 |
| 3 | eth | 0.71% | $11,955,262,925 | $1,976.9100 |
| 4 | usdc | 0.00% | $3,263,881,454 | $1.0000 |
| 5 | sol | 0.85% | $2,103,078,895 | $85.2100 |


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
