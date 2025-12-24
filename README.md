# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2025-12-24 01:07 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pippin | 31.36% | $67,803,517 | $0.4612 |
| 2 | btse | 13.17% | $5,727,956 | $1.5300 |
| 3 | rain | 11.32% | $64,580,172 | $0.0080 |
| 4 | hash | 8.21% | $151,887 | $0.0335 |
| 5 | mon | 7.77% | $170,656,150 | $0.0210 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | beat | -34.44% | $87,727,426 | $2.5200 |
| 2 | h | -21.98% | $239,109,432 | $0.1617 |
| 3 | night | -20.17% | $238,340,179 | $0.0800 |
| 4 | ftn | -11.01% | $12,965,313 | $1.1200 |
| 5 | pump | -10.51% | $99,059,761 | $0.0017 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $65,934,461,971 | $0.9995 |
| 2 | btc | -1.28% | $47,601,447,864 | $87,658.0000 |
| 3 | eth | -1.77% | $21,185,145,795 | $2,971.9200 |
| 4 | usdc | -0.00% | $19,686,047,441 | $0.9999 |
| 5 | sol | -2.16% | $3,402,092,995 | $123.8500 |


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
