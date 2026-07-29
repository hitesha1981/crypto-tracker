# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-07-29 01:54 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | btw | 39.04% | $18,901,928 | $0.0889 |
| 2 | beat | 23.20% | $47,704,871 | $3.5100 |
| 3 | ub | 17.58% | $16,346,409 | $0.1412 |
| 4 | cheems | 10.72% | $1,485,664 | $0.0000 |
| 5 | bp | 6.58% | $1,631,911 | $0.4586 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | xec | -10.21% | $13,699,676 | $0.0000 |
| 2 | kaito | -6.40% | $83,608,579 | $1.2300 |
| 3 | us | -6.37% | $5,101,484 | $0.0426 |
| 4 | b | -6.09% | $6,364,375 | $0.1692 |
| 5 | pyth | -5.92% | $16,846,563 | $0.0406 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.02% | $40,597,841,478 | $0.9988 |
| 2 | btc | 0.77% | $23,543,427,409 | $63,654.0000 |
| 3 | usdc | 0.00% | $11,833,346,053 | $0.9999 |
| 4 | eth | 1.66% | $9,663,945,379 | $1,905.0500 |
| 5 | sol | 0.08% | $1,640,258,491 | $73.2900 |


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
