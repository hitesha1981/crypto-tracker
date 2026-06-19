# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-19 03:37 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | velvet | 48.91% | $34,374,902 | $0.5020 |
| 2 | lab | 30.34% | $51,834,314 | $18.0400 |
| 3 | btw | 27.88% | $73,907,994 | $0.0559 |
| 4 | bp | 26.52% | $10,004,015 | $0.6140 |
| 5 | dexe | 20.38% | $28,561,806 | $16.5000 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | nex | -16.71% | $3,835,913 | $0.0000 |
| 2 | rail | -14.38% | $635,235 | $2.3900 |
| 3 | tag | -14.11% | $5,212,352 | $0.0011 |
| 4 | h | -11.47% | $46,337,330 | $0.2168 |
| 5 | xpl | -10.90% | $160,262,107 | $0.0964 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $53,048,865,331 | $0.9990 |
| 2 | btc | -2.47% | $31,611,201,465 | $62,676.0000 |
| 3 | eth | -2.76% | $12,706,419,029 | $1,695.1800 |
| 4 | usdc | 0.00% | $12,681,134,171 | $0.9999 |
| 5 | sol | -3.61% | $2,471,890,739 | $69.0700 |


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
