# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-10-15 02:38 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | wal | 45.58% | $317,201,674 | $0.0615 |
| 2 | q | 16.29% | $15,791,827 | $0.0512 |
| 3 | ake | 6.18% | $8,824,392 | $0.0267 |
| 4 | pyth | 6.16% | $86,403,236 | $0.0838 |
| 5 | cards | 5.11% | $11,725,385 | $0.2831 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | hash | -16.63% | $4,694 | $0.0062 |
| 2 | op | -15.52% | $154,807,798 | $0.1338 |
| 3 | zama | -15.50% | $17,608,419 | $0.0675 |
| 4 | grass | -15.05% | $41,623,862 | $0.6186 |
| 5 | drv | -13.73% | $13,898,664 | $0.3845 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.03% | $64,773,455,514 | $0.9991 |
| 2 | btc | -2.59% | $37,206,004,361 | $81,079.0000 |
| 3 | usdc | -0.02% | $19,288,553,525 | $0.9997 |
| 4 | eth | -5.45% | $15,900,954,635 | $2,366.4800 |
| 5 | sol | -4.19% | $3,519,764,967 | $102.8500 |


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
