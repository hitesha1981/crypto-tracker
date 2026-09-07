# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-09-07 02:12 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | zcat | 171.71% | $59,180,695 | $0.1650 |
| 2 | stonk | 141.13% | $136,639,312 | $0.1637 |
| 3 | ray | 29.99% | $313,152,639 | $1.2300 |
| 4 | jup | 18.08% | $198,681,301 | $0.2654 |
| 5 | rail | 16.52% | $884,155 | $2.3400 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | marscoin | -32.64% | $105,496,720 | $0.1653 |
| 2 | ake | -19.36% | $47,656,241 | $0.0145 |
| 3 | pons | -18.11% | $200,535,061 | $0.7818 |
| 4 | useless | -17.82% | $119,763,090 | $0.2165 |
| 5 | skr | -12.31% | $10,521,964 | $0.0194 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdc | -0.01% | $5,046,402,698,373 | $0.9999 |
| 2 | usdt | -0.01% | $44,708,599,140 | $0.9999 |
| 3 | btc | -0.19% | $20,526,383,198 | $79,807.0000 |
| 4 | eth | -0.32% | $9,803,441,556 | $2,499.1500 |
| 5 | sol | 0.81% | $3,826,522,238 | $104.9700 |


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
