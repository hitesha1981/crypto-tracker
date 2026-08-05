# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-08-05 01:51 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | m | 66.70% | $383,597 | $1.2900 |
| 2 | btw | 28.30% | $12,234,313 | $0.1285 |
| 3 | pump | 12.40% | $151,226,945 | $0.0024 |
| 4 | shfl | 12.40% | $1,146,241 | $0.3171 |
| 5 | pieverse | 6.60% | $6,448,473 | $0.7946 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | ub | -36.90% | $12,898,431 | $0.1253 |
| 2 | beat | -16.40% | $22,493,764 | $2.6000 |
| 3 | ldo | -15.90% | $71,868,916 | $0.2763 |
| 4 | peanut | -14.90% | $2 | $0.0006 |
| 5 | ethfi | -13.00% | $43,930,264 | $0.3609 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $35,482,164,396 | $0.9993 |
| 2 | btc | 0.80% | $23,034,332,354 | $64,172.0000 |
| 3 | usdc | 0.00% | $10,436,011,346 | $0.9997 |
| 4 | eth | 0.30% | $6,924,979,366 | $1,870.0700 |
| 5 | sol | 0.00% | $1,420,504,715 | $73.9000 |


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
