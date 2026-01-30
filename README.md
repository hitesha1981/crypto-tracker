# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-30 01:21 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | sent | 72.40% | $625,159,451 | $0.0421 |
| 2 | adi | 12.86% | $3,109,436 | $2.4600 |
| 3 | cc | 10.48% | $33,684,128 | $0.1792 |
| 4 | zro | 7.37% | $169,600,429 | $2.1200 |
| 5 | cusd | 3.07% | $95,785 | $1.0170 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pippin | -27.52% | $51,432,529 | $0.2937 |
| 2 | wld | -15.36% | $542,657,415 | $0.4727 |
| 3 | chz | -14.79% | $165,625,117 | $0.0475 |
| 4 | lit | -12.95% | $160,755,999 | $1.6700 |
| 5 | kaia | -12.36% | $25,624,869 | $0.0570 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $114,994,466,447 | $0.9984 |
| 2 | btc | -5.64% | $72,365,023,327 | $83,894.0000 |
| 3 | eth | -6.47% | $39,696,262,680 | $2,804.6400 |
| 4 | usdc | 0.00% | $10,499,804,164 | $0.9996 |
| 5 | sol | -5.82% | $6,323,181,233 | $117.4600 |


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
