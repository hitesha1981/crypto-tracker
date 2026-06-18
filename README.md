# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-18 02:51 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | bsb | 26.19% | $55,727,649 | $0.5948 |
| 2 | tag | 23.79% | $8,496,249 | $0.0013 |
| 3 | home | 23.12% | $34,958,481 | $0.0333 |
| 4 | hash | 15.25% | $62,224 | $0.0100 |
| 5 | xpl | 13.78% | $358,666,542 | $0.1095 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | beat | -34.79% | $62,959,247 | $1.7800 |
| 2 | h | -27.97% | $47,955,788 | $0.2435 |
| 3 | dexe | -25.26% | $29,919,917 | $13.6700 |
| 4 | skyai | -19.75% | $41,432,474 | $0.3642 |
| 5 | velvet | -14.95% | $13,143,653 | $0.3445 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $54,655,243,724 | $0.9990 |
| 2 | btc | -1.71% | $31,711,103,550 | $64,664.0000 |
| 3 | usdc | 0.01% | $13,763,489,805 | $0.9998 |
| 4 | eth | -2.05% | $13,449,655,153 | $1,754.9100 |
| 5 | sol | -1.82% | $2,769,590,833 | $72.4700 |


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
