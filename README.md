# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-07-27 02:11 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | b | 17.82% | $10,508,657 | $0.1897 |
| 2 | ub | 16.89% | $12,803,085 | $0.1445 |
| 3 | kaito | 15.70% | $98,880,060 | $1.1700 |
| 4 | pump | 12.82% | $80,374,266 | $0.0020 |
| 5 | aave | 9.34% | $294,173,506 | $100.7100 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | grx | -38.54% | $381,878 | $13.0400 |
| 2 | dexe | -22.81% | $256,018,558 | $3.2900 |
| 3 | velvet | -8.57% | $6,350,612 | $0.4555 |
| 4 | kag | -8.55% | $425,715 | $51.9300 |
| 5 | xec | -6.12% | $7,628,660 | $0.0000 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.01% | $28,883,613,195 | $0.9989 |
| 2 | btc | 1.12% | $15,423,377,461 | $65,123.0000 |
| 3 | usdc | -0.01% | $7,298,221,375 | $0.9999 |
| 4 | eth | 3.63% | $6,448,760,920 | $1,945.6000 |
| 5 | sol | 2.23% | $1,057,760,376 | $76.4300 |


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
