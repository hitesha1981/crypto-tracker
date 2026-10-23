# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-10-23 02:48 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ake | 49.13% | $28,498,868 | $0.0333 |
| 2 | m | 13.68% | $3,895,502 | $0.8526 |
| 3 | btw | 10.94% | $26,947,934 | $1.8700 |
| 4 | rail | 9.22% | $488,677 | $2.4900 |
| 5 | hash | 9.22% | $4,064 | $0.0071 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | bp | -9.77% | $4,137,476 | $1.0180 |
| 2 | geod | -9.37% | $3,221,662 | $0.2564 |
| 3 | kmno | -8.83% | $6,589,270 | $0.0384 |
| 4 | pearl | -8.10% | $11,040,984 | $2.1800 |
| 5 | zk | -8.00% | $9,734,109 | $0.0131 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.05% | $53,176,550,919 | $0.9988 |
| 2 | btc | -1.34% | $32,044,576,805 | $81,787.0000 |
| 3 | usdc | -0.03% | $12,607,077,820 | $0.9994 |
| 4 | eth | -1.19% | $12,533,432,548 | $2,409.6500 |
| 5 | sol | -1.00% | $2,371,074,204 | $104.4600 |


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
