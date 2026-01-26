# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-01-26 01:17 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | river | 23.90% | $87,475,925 | $73.1800 |
| 2 | kag | 3.46% | $1,813,969 | $107.5500 |
| 3 | cusd | 2.91% | $11,769 | $1.0290 |
| 4 | apepe | 2.77% | $11,209,245 | $0.0000 |
| 5 | stable | 1.53% | $30,011,187 | $0.0205 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | kaia | -23.40% | $65,026,630 | $0.0719 |
| 2 | axs | -19.10% | $352,569,453 | $1.9600 |
| 3 | pippin | -17.76% | $52,182,583 | $0.3169 |
| 4 | myx | -13.25% | $25,831,707 | $5.9800 |
| 5 | 2z | -12.30% | $23,185,301 | $0.1210 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.04% | $74,887,203,816 | $0.9990 |
| 2 | btc | -2.10% | $42,576,400,933 | $87,258.0000 |
| 3 | eth | -2.86% | $25,929,538,248 | $2,868.3200 |
| 4 | sol | -4.82% | $5,986,417,957 | $120.9400 |
| 5 | usdc | -0.01% | $5,283,345,547 | $0.9996 |


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
