# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-05 01:24 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | mantra | 59.96% | $327,119,325 | $0.0238 |
| 2 | shfl | 23.77% | $716,364 | $0.3106 |
| 3 | mwc | 19.99% | $74,921 | $11.7600 |
| 4 | qrl | 13.45% | $103,116 | $1.6200 |
| 5 | b | 13.40% | $9,548,709 | $0.2228 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | near | -7.66% | $380,475,166 | $1.2700 |
| 2 | siren | -7.64% | $36,085,651 | $0.3664 |
| 3 | hash | -7.26% | $26,330 | $0.0150 |
| 4 | form | -7.09% | $57,176,861 | $0.3033 |
| 5 | m | -6.32% | $8,990,636 | $1.3500 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $124,194,655,405 | $1.0000 |
| 2 | btc | 7.18% | $82,591,942,318 | $72,889.0000 |
| 3 | eth | 7.67% | $34,604,125,576 | $2,124.1100 |
| 4 | usdc | 0.01% | $11,837,694,519 | $1.0000 |
| 5 | sol | 4.70% | $7,426,122,253 | $90.8100 |


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
