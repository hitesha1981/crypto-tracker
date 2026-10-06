# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-10-06 04:10 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | orca | 18.32% | $101,592,468 | $2.3400 |
| 2 | cards | 17.63% | $18,794,424 | $0.2964 |
| 3 | zro | 12.11% | $170,097,096 | $2.1400 |
| 4 | fluid | 11.48% | $45,842,488 | $1.9800 |
| 5 | shx | 11.41% | $4,975,432 | $0.0084 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | rail | -12.10% | $1,051,012 | $2.4200 |
| 2 | mina | -12.01% | $22,036,118 | $0.1404 |
| 3 | strk | -11.81% | $73,936,974 | $0.0521 |
| 4 | mon | -9.63% | $54,302,929 | $0.0294 |
| 5 | sky | -7.89% | $47,306,425 | $0.0879 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $56,696,972,279 | $0.9998 |
| 2 | btc | -0.54% | $29,199,908,494 | $85,558.0000 |
| 3 | usdc | 0.00% | $18,228,082,125 | $0.9999 |
| 4 | eth | -0.51% | $11,485,761,171 | $2,699.9200 |
| 5 | sol | -0.26% | $2,440,603,313 | $120.1200 |


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
