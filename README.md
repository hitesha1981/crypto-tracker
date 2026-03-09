# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-09 01:25 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | dexe | 12.29% | $10,632,201 | $4.0900 |
| 2 | siren | 8.99% | $15,767,861 | $0.4458 |
| 3 | chz | 5.91% | $70,028,861 | $0.0366 |
| 4 | tao | 4.34% | $117,463,825 | $184.8400 |
| 5 | zro | 3.79% | $86,554,318 | $1.9700 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | h | -13.39% | $30,706,673 | $0.1308 |
| 2 | river | -11.13% | $20,932,151 | $13.9200 |
| 3 | lit | -10.45% | $26,309,926 | $1.0050 |
| 4 | om | -9.65% | $103,303 | $0.0343 |
| 5 | kau | -9.65% | $242,321 | $163.1100 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $58,992,183,577 | $0.9999 |
| 2 | btc | -1.35% | $38,469,088,665 | $66,362.0000 |
| 3 | eth | -1.03% | $16,393,272,340 | $1,950.0400 |
| 4 | usdc | -0.01% | $5,512,196,290 | $0.9999 |
| 5 | sol | -0.86% | $2,869,581,060 | $82.4100 |


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
