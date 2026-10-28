# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-10-28 03:23 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btw | 41.91% | $15,108,037 | $1.7500 |
| 2 | pons | 21.38% | $37,882,133 | $0.2887 |
| 3 | pepe | 13.30% | $432,486,703 | $0.0000 |
| 4 | grass | 12.26% | $27,689,908 | $0.7563 |
| 5 | m | 10.82% | $2,292,427 | $1.0820 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | q | -74.50% | $104,917,836 | $0.0541 |
| 2 | ake | -27.77% | $36,351,693 | $0.0224 |
| 3 | dgai | -6.29% | $29,742,233 | $0.7952 |
| 4 | kmno | -5.33% | $8,972,081 | $0.0397 |
| 5 | pearl | -5.28% | $5,432,593 | $1.6600 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $42,164,468,141 | $0.9988 |
| 2 | btc | 1.56% | $23,850,884,677 | $80,875.0000 |
| 3 | usdc | 0.01% | $10,496,449,391 | $0.9994 |
| 4 | eth | 2.04% | $9,588,810,401 | $2,356.2200 |
| 5 | sol | 1.68% | $2,007,103,363 | $101.6400 |


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
