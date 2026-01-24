# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-24 01:08 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | kaia | 38.60% | $94,916,694 | $0.0729 |
| 2 | 0g | 22.55% | $279,374,191 | $1.0890 |
| 3 | 2z | 10.44% | $55,331,379 | $0.1390 |
| 4 | cc | 8.03% | $20,158,134 | $0.1560 |
| 5 | kag | 6.85% | $2,394,591 | $103.9300 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | river | -37.92% | $121,273,552 | $41.2000 |
| 2 | pendle | -7.25% | $63,073,033 | $2.0100 |
| 3 | xdc | -6.39% | $33,235,239 | $0.0412 |
| 4 | lit | -6.14% | $123,303,691 | $1.6700 |
| 5 | sand | -6.09% | $202,420,094 | $0.1561 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.03% | $79,186,299,642 | $0.9987 |
| 2 | btc | -0.20% | $42,849,349,771 | $89,347.0000 |
| 3 | eth | -0.17% | $22,662,128,471 | $2,948.3300 |
| 4 | usdc | -0.01% | $7,624,348,918 | $0.9996 |
| 5 | usd1 | -0.03% | $6,771,821,661 | $1.0000 |


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
