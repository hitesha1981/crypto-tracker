# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-02-21 01:21 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | myx | 21.76% | $119,764,283 | $1.1900 |
| 2 | 9bit | 16.58% | $5,396,563 | $0.0163 |
| 3 | vvv | 15.37% | $30,149,809 | $4.3700 |
| 4 | rave | 14.17% | $107,932,574 | $0.5698 |
| 5 | zro | 14.00% | $110,746,098 | $1.7100 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | qrl | -16.77% | $113,874 | $1.5300 |
| 2 | aave | -8.49% | $442,151,139 | $114.7900 |
| 3 | mwc | -6.87% | $140,463 | $13.8800 |
| 4 | op | -6.71% | $200,357,811 | $0.1280 |
| 5 | chz | -6.65% | $77,711,382 | $0.0360 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.00% | $80,672,034,523 | $0.9996 |
| 2 | btc | 0.96% | $52,714,312,763 | $67,849.0000 |
| 3 | eth | 0.43% | $21,738,420,678 | $1,964.2100 |
| 4 | usdc | -0.00% | $11,036,541,276 | $0.9999 |
| 5 | sol | 2.03% | $4,052,642,742 | $84.5500 |


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
