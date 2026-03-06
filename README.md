# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-06 01:26 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | bard | 55.37% | $343,126,566 | $1.6700 |
| 2 | h | 43.36% | $96,265,423 | $0.1793 |
| 3 | okb | 27.44% | $395,538,948 | $99.2400 |
| 4 | siren | 26.80% | $30,657,776 | $0.4622 |
| 5 | kite | 25.61% | $153,103,061 | $0.2807 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | vvv | -9.72% | $36,162,573 | $6.1000 |
| 2 | lit | -9.33% | $28,718,511 | $1.2200 |
| 3 | hash | -8.14% | $15,096 | $0.0138 |
| 4 | exod | -8.06% | $0 | $11.1800 |
| 5 | mwc | -6.90% | $136,730 | $10.8600 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.03% | $83,012,306,927 | $1.0000 |
| 2 | btc | -2.87% | $54,107,484,769 | $70,840.0000 |
| 3 | eth | -2.35% | $21,993,651,586 | $2,076.3400 |
| 4 | usdc | -0.00% | $13,457,881,110 | $1.0000 |
| 5 | sol | -2.20% | $4,646,087,973 | $88.6600 |


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
