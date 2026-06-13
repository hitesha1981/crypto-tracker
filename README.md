# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-06-13 02:42 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | bdx | 39.23% | $8,258,512 | $0.0767 |
| 2 | trump | 32.48% | $855,739,218 | $2.3200 |
| 3 | h | 19.57% | $87,461,179 | $0.2283 |
| 4 | cheems | 13.30% | $1,391,497 | $0.0000 |
| 5 | pieverse | 13.17% | $13,910,110 | $0.6965 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | velvet | -74.15% | $136,769,052 | $0.4648 |
| 2 | siren | -24.32% | $45,788,093 | $0.3764 |
| 3 | xmr | -11.15% | $251,873,592 | $346.2300 |
| 4 | dexe | -10.65% | $48,579,102 | $18.9800 |
| 5 | inj | -9.26% | $118,954,637 | $5.0800 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.08% | $47,593,764,926 | $0.9994 |
| 2 | btc | 0.23% | $26,807,992,551 | $63,662.0000 |
| 3 | usdc | 0.02% | $12,631,404,427 | $0.9999 |
| 4 | eth | -0.31% | $9,457,049,594 | $1,668.7500 |
| 5 | sol | 0.07% | $2,713,063,987 | $67.0700 |


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
