# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-05-01 02:26 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | bsb | 47.50% | $63,222,862 | $0.6218 |
| 2 | asteroid | 28.85% | $21,229,579 | $0.0004 |
| 3 | skyai | 23.22% | $109,336,472 | $0.3786 |
| 4 | genius | 16.36% | $30,802,708 | $0.5196 |
| 5 | ub | 14.51% | $57,931,055 | $0.0750 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | mega | -26.34% | $475,053,716 | $0.1657 |
| 2 | rave | -11.50% | $23,082,632 | $0.6720 |
| 3 | pieverse | -9.07% | $6,674,911 | $0.6680 |
| 4 | lit | -7.58% | $22,085,194 | $0.8850 |
| 5 | a | -6.71% | $12,454,944 | $0.0886 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $51,501,673,158 | $0.9995 |
| 2 | btc | 0.59% | $31,130,571,216 | $76,589.0000 |
| 3 | eth | 0.07% | $11,532,874,182 | $2,264.7700 |
| 4 | usdc | -0.01% | $11,397,334,484 | $0.9997 |
| 5 | sol | -0.11% | $2,404,139,735 | $83.5000 |


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
