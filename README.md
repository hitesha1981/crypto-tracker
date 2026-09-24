# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-09-24 02:31 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | meta | 22.01% | $21,169,888 | $6.7600 |
| 2 | btw | 16.52% | $27,793,690 | $1.0610 |
| 3 | dbr | 13.05% | $13,471,372 | $0.0207 |
| 4 | zro | 12.29% | $210,119,949 | $1.5700 |
| 5 | stonk | 9.68% | $42,836,736 | $0.3453 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | spx | -17.02% | $30,560,082 | $0.4317 |
| 2 | ai | -14.70% | $13,981,120 | $0.2258 |
| 3 | useless | -12.51% | $78,820,001 | $0.2947 |
| 4 | zen | -11.98% | $34,730,005 | $7.2500 |
| 5 | wld | -11.69% | $484,946,954 | $0.4082 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $81,170,790,525 | $0.9998 |
| 2 | btc | -2.79% | $43,926,364,054 | $84,137.0000 |
| 3 | usdc | -0.00% | $21,111,410,995 | $0.9999 |
| 4 | eth | -2.86% | $17,337,092,281 | $2,679.2400 |
| 5 | xrp | -5.66% | $6,166,103,138 | $1.5000 |


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
