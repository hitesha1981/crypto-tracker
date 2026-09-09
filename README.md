# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-09-09 02:26 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | useless | 31.42% | $191,375,450 | $0.2939 |
| 2 | vvv | 30.93% | $219,795,207 | $24.8900 |
| 3 | ff | 23.26% | $65,035,583 | $0.1474 |
| 4 | form | 23.11% | $100,040,617 | $0.3102 |
| 5 | dot | 12.75% | $434,890,281 | $1.2000 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | marscoin | -24.04% | $94,914,406 | $0.1182 |
| 2 | tibbir | -9.67% | $4,952,264 | $0.2077 |
| 3 | stonk | -9.39% | $68,269,194 | $0.1503 |
| 4 | virtual | -7.23% | $67,339,960 | $0.7035 |
| 5 | op | -7.15% | $67,745,230 | $0.1044 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $58,389,963,995 | $0.9998 |
| 2 | btc | -0.78% | $37,617,333,064 | $78,787.0000 |
| 3 | usdc | 0.01% | $15,335,859,281 | $1.0000 |
| 4 | eth | -0.31% | $11,928,742,067 | $2,495.7200 |
| 5 | link | -2.47% | $4,534,146,784 | $12.4700 |


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
