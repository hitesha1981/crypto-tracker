# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-23 02:35 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | dexe | 64.70% | $79,283,205 | $22.3700 |
| 2 | gwei | 15.27% | $5,069,261 | $0.1201 |
| 3 | lab | 11.90% | $42,505,034 | $16.9700 |
| 4 | rain | 11.43% | $39,140,765 | $0.0160 |
| 5 | kag | 9.05% | $388,828 | $64.3400 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | h | -36.15% | $30,923,780 | $0.1218 |
| 2 | ub | -17.96% | $50,960,582 | $0.0980 |
| 3 | btw | -13.44% | $47,609,341 | $0.0835 |
| 4 | skyai | -12.22% | $17,282,575 | $0.3323 |
| 5 | re | -11.16% | $188,178,123 | $0.7969 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $46,100,138,552 | $0.9988 |
| 2 | btc | -0.55% | $25,813,719,070 | $64,115.0000 |
| 3 | eth | -0.59% | $12,732,333,883 | $1,729.3400 |
| 4 | usdc | -0.01% | $10,875,877,850 | $0.9997 |
| 5 | sol | -3.03% | $2,441,327,894 | $71.8300 |


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
