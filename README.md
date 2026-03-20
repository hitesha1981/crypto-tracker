# Crypto Tracker (24h)
Author: Hitesh Agrawal

This repository automatically tracks the top 5 gaining, top 5 losing, and top 5 highest volume cryptocurrencies in the last 24 hours using the CoinGecko API, Python, Matplotlib, and GitHub Actions updates the below content everyday at midnight.

<!-- START_DYNAMIC_CONTENT -->
Last updated: 2026-03-20 01:24 UTC

![Crypto Movers Plot](crypto_movers_plot.png)

**🚀 Top 5 Gainers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | uai | 47.22% | $9,769,260 | $0.6008 |
| 2 | zano | 19.83% | $2,190,604 | $8.6900 |
| 3 | kite | 14.17% | $214,949,700 | $0.2143 |
| 4 | zbcn | 12.75% | $11,256,757 | $0.0023 |
| 5 | dexe | 9.41% | $21,550,192 | $6.2100 |


**👇 Top 5 Losers (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | sos | -25.38% | $268,158 | $0.0011 |
| 2 | bard | -11.48% | $113,528,138 | $0.5725 |
| 3 | siren | -9.40% | $22,775,216 | $0.8046 |
| 4 | wld | -9.34% | $194,860,484 | $0.3323 |
| 5 | akt | -8.73% | $20,268,080 | $0.5010 |


**💎 Top 5 by Trade Volume (24h)**

| Rank | Coin | Price Change (24h %) | Volume (USD) | Current Price (USD) |
| :--: | :--: | :------------------: | :----------: | :-----------------: |
| 1 | usdt | -0.00% | $77,121,881,977 | $1.0000 |
| 2 | btc | -0.82% | $45,831,048,452 | $70,404.0000 |
| 3 | eth | -1.81% | $23,133,684,120 | $2,149.4300 |
| 4 | usdc | -0.01% | $10,692,205,320 | $0.9999 |
| 5 | sol | -0.62% | $3,629,472,774 | $89.5300 |


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
