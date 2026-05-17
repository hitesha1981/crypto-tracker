# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-17 02:28 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | xp | 79.02% | $3,072,680 | $0.0651 |
| 2 | h | 10.09% | $30,254,214 | $0.2387 |
| 3 | stable | 8.81% | $30,813,110 | $0.0356 |
| 4 | asteroid | 7.93% | $15,956,432 | $0.0004 |
| 5 | kaia | 4.98% | $11,170,535 | $0.0483 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ub | -32.57% | $49,860,014 | $0.1563 |
| 2 | bill | -22.99% | $780,911,608 | $0.1381 |
| 3 | b | -9.69% | $37,740,166 | $0.3905 |
| 4 | pendle | -9.54% | $36,561,027 | $1.8100 |
| 5 | glm | -9.12% | $23,947,624 | $0.1349 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $43,311,747,197 | $0.9995 |
| 2 | btc | -1.66% | $26,123,221,636 | $77,823.0000 |
| 3 | eth | -2.47% | $10,669,565,000 | $2,172.7900 |
| 4 | usdc | -0.00% | $6,622,650,359 | $0.9998 |
| 5 | sol | -3.55% | $2,361,655,867 | $85.9700 |


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
