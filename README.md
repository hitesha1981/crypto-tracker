# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-10 02:12 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | bill | 33.32% | $522,347,109 | $0.1107 |
| 2 | pros | 23.41% | $24,205,495 | $1.0440 |
| 3 | zano | 8.67% | $1,372,123 | $11.0200 |
| 4 | bsb | 8.55% | $28,051,475 | $0.5798 |
| 5 | jasmy | 8.29% | $85,896,419 | $0.0071 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | cfg | -11.90% | $50,334,342 | $0.2934 |
| 2 | ondo | -11.24% | $353,117,109 | $0.4127 |
| 3 | icp | -9.08% | $166,806,495 | $3.5500 |
| 4 | ar | -8.22% | $32,246,925 | $2.4900 |
| 5 | virtual | -7.55% | $94,625,537 | $0.8882 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $38,327,389,047 | $0.9998 |
| 2 | btc | 0.24% | $19,476,493,619 | $80,616.0000 |
| 3 | eth | 0.20% | $10,726,484,384 | $2,321.7100 |
| 4 | usdc | -0.01% | $6,804,176,509 | $0.9998 |
| 5 | sol | -0.65% | $2,476,201,124 | $92.9200 |


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
