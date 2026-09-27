# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-09-27 02:54 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | qnt | 69.74% | $385,097,184 | $169.6500 |
| 2 | q | 45.19% | $64,741,000 | $0.0350 |
| 3 | rain | 22.21% | $14,982,612 | $0.0128 |
| 4 | 2z | 19.98% | $102,727,324 | $0.0696 |
| 5 | rune | 19.26% | $404,822,182 | $0.7909 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | h | -9.45% | $6,424,622 | $0.0700 |
| 2 | stonk | -9.34% | $37,252,334 | $0.2823 |
| 3 | cashcat | -6.53% | $10,713,704 | $0.1845 |
| 4 | ai | -5.42% | $8,317,073 | $0.2429 |
| 5 | aioz | -5.37% | $6,976,174 | $0.1206 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $34,953,059,368 | $0.9998 |
| 2 | btc | 0.51% | $17,842,269,006 | $84,458.0000 |
| 3 | usdc | -0.00% | $8,101,142,046 | $0.9999 |
| 4 | eth | 0.30% | $6,100,691,341 | $2,699.3800 |
| 5 | sol | -0.26% | $2,848,232,141 | $121.3800 |


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
