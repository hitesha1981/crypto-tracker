# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2025-12-22 01:11 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | beat | 58.97% | $116,942,525 | $3.7600 |
| 2 | h | 25.65% | $114,470,711 | $0.1445 |
| 3 | night | 16.03% | $5,584,386,755 | $0.0917 |
| 4 | m | 9.48% | $16,881,575 | $1.4900 |
| 5 | myx | 9.47% | $36,543,990 | $3.2100 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | aave | -9.06% | $427,650,862 | $162.5200 |
| 2 | cc | -7.65% | $35,810,717 | $0.0950 |
| 3 | icp | -6.95% | $107,931,645 | $3.0800 |
| 4 | xdc | -5.98% | $40,363,514 | $0.0459 |
| 5 | dcr | -5.21% | $1,794,860 | $15.8300 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.01% | $49,256,544,873 | $0.9998 |
| 2 | btc | 0.58% | $25,003,189,037 | $88,824.0000 |
| 3 | eth | 1.75% | $14,228,628,742 | $3,029.4100 |
| 4 | usdc | 0.01% | $5,710,069,316 | $1.0000 |
| 5 | night | 16.03% | $5,584,386,755 | $0.0917 |


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
