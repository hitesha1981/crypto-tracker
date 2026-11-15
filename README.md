# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-11-15 04:07 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pieverse | 15.87% | $29,054,330 | $1.9300 |
| 2 | night | 5.09% | $59,169,441 | $0.0484 |
| 3 | vvv | 4.24% | $57,118,697 | $19.5100 |
| 4 | 币安人生 | 3.20% | $7,105,202 | $0.4698 |
| 5 | borg | 3.05% | $552,237 | $0.1352 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | pengu | -15.96% | $154,585,599 | $0.0050 |
| 2 | ake | -15.60% | $181,972,313 | $0.0106 |
| 3 | aster | -15.35% | $224,778,179 | $0.5243 |
| 4 | pump | -13.18% | $161,713,681 | $0.0030 |
| 5 | cards | -13.13% | $12,762,958 | $0.1682 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | 0.04% | $76,752,083,307 | $0.9995 |
| 2 | btc | -2.97% | $51,368,864,335 | $64,739.0000 |
| 3 | eth | -3.68% | $20,617,489,028 | $1,815.7900 |
| 4 | usdc | 0.02% | $18,220,282,498 | $0.9997 |
| 5 | sol | -5.30% | $4,693,657,602 | $71.1800 |


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
