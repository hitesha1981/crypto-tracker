# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-02-24 01:24 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | river | 20.19% | $18,081,998 | $9.0000 |
| 2 | power | 19.16% | $28,041,954 | $0.5365 |
| 3 | pippin | 18.90% | $61,801,737 | $0.7388 |
| 4 | sent | 14.20% | $82,989,656 | $0.0240 |
| 5 | dexe | 12.29% | $18,517,601 | $2.9100 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | h | -17.84% | $49,769,207 | $0.1348 |
| 2 | myx | -15.00% | $72,905,514 | $0.5779 |
| 3 | fartcoin | -12.25% | $82,138,582 | $0.1428 |
| 4 | bch | -11.38% | $506,981,301 | $492.9000 |
| 5 | mwc | -9.84% | $73,891 | $12.4900 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $86,082,688,695 | $0.9998 |
| 2 | btc | -1.75% | $51,080,313,292 | $64,032.0000 |
| 3 | eth | -1.92% | $21,502,353,660 | $1,837.3100 |
| 4 | sol | -2.23% | $5,097,328,613 | $77.2300 |
| 5 | usdc | -0.01% | $4,735,152,010 | $0.9999 |


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
