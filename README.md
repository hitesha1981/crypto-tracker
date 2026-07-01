# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-07-01 02:46 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btw | 22.68% | $24,553,375 | $0.0635 |
| 2 | m | 21.38% | $9,254,241 | $0.7947 |
| 3 | dydx | 17.55% | $15,153,119 | $0.1850 |
| 4 | h | 17.46% | $36,229,016 | $0.0846 |
| 5 | drv | 14.88% | $1,921,906 | $0.1163 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | gwei | -26.88% | $15,124,223 | $0.1180 |
| 2 | ub | -15.85% | $47,970,379 | $0.0896 |
| 3 | lab | -15.55% | $38,662,268 | $12.4600 |
| 4 | bas | -15.08% | $38,274,346 | $0.0464 |
| 5 | xpl | -11.82% | $77,438,342 | $0.0898 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $53,003,501,615 | $0.9984 |
| 2 | btc | -1.52% | $35,154,061,058 | $59,036.0000 |
| 3 | usdc | -0.01% | $14,602,214,831 | $0.9996 |
| 4 | eth | -0.31% | $8,907,679,018 | $1,586.2200 |
| 5 | sol | 0.60% | $2,755,688,601 | $74.8000 |


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
