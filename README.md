# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-04-20 02:01 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pieverse | 76.53% | $248,255,897 | $1.0860 |
| 2 | btse | 10.05% | $2,988,072 | $1.2400 |
| 3 | jst | 8.12% | $35,055,603 | $0.0746 |
| 4 | cfg | 7.58% | $53,595,419 | $0.2741 |
| 5 | enj | 7.02% | $225,907,966 | $0.0599 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | rave | -78.12% | $365,607,091 | $0.5266 |
| 2 | ultima | -14.06% | $7,947,389 | $3,239.8800 |
| 3 | ip | -11.31% | $37,188,120 | $0.5028 |
| 4 | kau | -6.82% | $34,763 | $153.5400 |
| 5 | 币安人生 | -6.78% | $170,204,002 | $0.4225 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.02% | $84,722,532,458 | $1.0000 |
| 2 | btc | -1.31% | $56,305,347,293 | $74,617.0000 |
| 3 | eth | -2.57% | $16,600,319,678 | $2,287.0400 |
| 4 | usdc | 0.01% | $13,935,354,490 | $0.9999 |
| 5 | sol | -1.55% | $3,820,712,379 | $84.3800 |


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
