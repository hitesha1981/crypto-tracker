# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-02-03 01:26 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | stx | 14.42% | $46,326,722 | $0.2977 |
| 2 | m | 13.60% | $12,934,065 | $1.4900 |
| 3 | stable | 13.18% | $76,377,889 | $0.0300 |
| 4 | whype | 11.56% | $312,301,547 | $34.3400 |
| 5 | tel | 11.17% | $3,225,148 | $0.0031 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | zk | -17.62% | $179,537,016 | $0.0243 |
| 2 | enzobtc | -11.26% | $0 | $77,988.0000 |
| 3 | axs | -9.25% | $140,835,287 | $1.5600 |
| 4 | ip | -8.86% | $101,327,804 | $1.4300 |
| 5 | btse | -8.16% | $14,878,185 | $1.4100 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $140,128,150,696 | $0.9992 |
| 2 | btc | 1.53% | $82,821,236,924 | $78,753.0000 |
| 3 | eth | 2.90% | $49,037,717,884 | $2,344.0000 |
| 4 | usdc | 0.01% | $21,279,281,615 | $0.9998 |
| 5 | sol | 2.15% | $7,369,407,388 | $103.7900 |


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
