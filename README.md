# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-22 01:12 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | river | 31.88% | $58,003,926 | $46.5700 |
| 2 | pippin | 30.07% | $51,069,726 | $0.3705 |
| 3 | tel | 25.64% | $5,783,491 | $0.0041 |
| 4 | axs | 18.19% | $829,803,878 | $2.5200 |
| 5 | shmeegus | 16.18% | $1,169,169 | $0.5433 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ip | -9.89% | $177,332,925 | $2.4000 |
| 2 | hash | -6.22% | $44,522 | $0.0248 |
| 3 | h | -4.95% | $22,788,777 | $0.1579 |
| 4 | kag | -4.27% | $2,226,891 | $91.2700 |
| 5 | night | -4.04% | $24,509,106 | $0.0600 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.03% | $101,803,416,674 | $0.9992 |
| 2 | btc | 1.05% | $60,803,274,365 | $89,874.0000 |
| 3 | eth | 1.71% | $36,579,929,877 | $3,013.1800 |
| 4 | usdc | 0.00% | $8,989,432,695 | $0.9998 |
| 5 | sol | 2.04% | $5,800,948,491 | $129.9600 |


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
